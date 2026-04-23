      Resource Controls
      Modern operating systems provide resource controls for managing disk or file system I/O usage
      in custom ways.

      For Linux, the container groups (cgroups) block I/O (blkio) subsystem provides storage device
      resource controls for processes or process groups. This can be a proportional weight (like a
      share) or a fixed limit. Limits can be set for read and write independently, and for either IOPS or
      throughput (bytes per second). For more detail, see Chapter 11, Cloud Computing.


      Tunable Parameters
      Example Linux tunables include:

          ■   /sys/block/*/queue/scheduler: To select the I/O scheduler policy: these may include
              noop, deadline, cfq, etc. See the earlier descriptions of these in Section 9.4, Architecture.
          ■   /sys/block/*/queue/nr_requests: The number of read or write requests that can be
              allocated by the block layer.
          ■   /sys/block/*/queue/read_ahead_kb: Maximum read ahead Kbytes for file systems to
              request.

      As with other kernel tunables, check the documentation for the full list, descriptions, and
      warnings. In the Linux source, see Documentation/block/queue-sysfs.txt.

