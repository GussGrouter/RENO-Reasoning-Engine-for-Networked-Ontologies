      9.8 Experimentation
      This section describes tools for actively testing disk I/O performance. See Section 9.5.9, Micro-
      Benchmarking, for a suggested methodology to follow.

      When using these tools, it’s a good idea to leave iostat(1) continually running so that any result
      can be immediately double-checked. Some micro-benchmarking tools may require a “direct”
      mode of operation to bypass the file system cache, and focus on disk device performance.


      9.8.1     Ad Hoc
      The dd(1) command (device-to-device copy) can be used to perform ad hoc tests of sequential
      disk performance. For example, testing sequential read with a 1 Mbyte I/O size:

      # dd if=/dev/sda1 of=/dev/null bs=1024k count=1k
      1024+0 records in
      1024+0 records out
      1073741824 bytes (1.1 GB) copied, 7.44024 s, 144 MB/s

      Since the kernel can cache and buffer data, the dd(1) measured throughput can be of the cache
      and disk and not the disk alone. To test only the disk’s performance, you can use a character
      special device for the disk: On Linux, the raw(8) command (where available) can create these
      under /dev/raw. Sequential write can be tested similarly; however, beware of destroying all data
      on disk, including the master boot record and partition table!

      A safer approach is to use the direct I/O flag with dd(1) and file system files instead of disk
      devices. Bear in mind that the test now includes some file system overheads. For example, doing
      a write test to a file called out1:
                                                                               9.8   Experimentation      491



# dd if=/dev/zero of=out1 bs=1024k count=1000 oflag=direct
1000+0 records in
1000+0 records out
1048576000 bytes (1.0 GB, 1000 MiB) copied, 1.79189 s, 585 MB/s

iostat(1) in another terminal session confirmed that the disk I/O write throughput was around
585 Mbytes/sec.

Use iflag=direct for direct I/O with input files.

