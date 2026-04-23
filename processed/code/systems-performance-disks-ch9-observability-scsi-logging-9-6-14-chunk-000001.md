      9.6.14      SCSI Logging
      Linux has a built-in facility for SCSI event logging. It can be enabled via sysctl(8) or /proc. For
      example, both of these commands set the logging to the maximum for all event types (warning:
      depending on your disk workload, this may flood your system log):

      # sysctl -w dev.scsi.logging_level=03333333333
      # echo 03333333333 > /proc/sys/dev/scsi/logging_level

      The format of the number is a bitfield that sets the logging level from 1 to 7 for 10 different event
      types (written here in octal; as hexadecimal it is 0x1b6db6db). This bitfield is defined in drivers/
      scsi/scsi_logging.h. The sg3-utils package provides a scsi_logging_level(8) tool for setting these.
      For example:

      # scsi_logging_level -s --all 3

      Example events:

      # dmesg
      [...]
      [542136.259412] sd 0:0:0:0: tag#0 Send: scmd 0x0000000001fb89dc
      [542136.259422] sd 0:0:0:0: tag#0 CDB: Test Unit Ready 00 00 00 00 00 00
      [542136.261103] sd 0:0:0:0: tag#0 Done: SUCCESS Result: hostbyte=DID_OK
      driverbyte=DRIVER_OK
      [542136.261110] sd 0:0:0:0: tag#0 CDB: Test Unit Ready 00 00 00 00 00 00
      [542136.261115] sd 0:0:0:0: tag#0 Sense Key : Not Ready [current]
      [542136.261121] sd 0:0:0:0: tag#0 Add. Sense: Medium not present
      [542136.261127] sd 0:0:0:0: tag#0 0 sectors total, 0 bytes done.
      [...]

      This can be used to help debug errors and timeouts. While timestamps are provided (the first
      column), using them to calculate I/O latency is difficult without unique identifying details.
                                                                                 9.7   Visualizations   487


