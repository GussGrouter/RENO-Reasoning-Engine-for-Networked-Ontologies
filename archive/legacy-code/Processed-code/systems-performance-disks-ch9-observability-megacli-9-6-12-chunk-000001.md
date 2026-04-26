      9.6.12      MegaCli
      Disk controllers (host bus adapters) consist of hardware and firmware that are external to the
      system. Operating system analysis tools, even dynamic tracers, cannot directly observe their
      internals. Sometimes their workings can be inferred by observing the input and output carefully
      (including via kernel static or dynamic instrumentation), to see how the disk controller responds
      to a series of I/O.

      There are some analysis tools for specific disk controllers, such as LSI’s MegaCli. The following
      shows recent controller events:

      # MegaCli -AdpEventLog -GetLatest 50 -f lsi.log -aALL
      # more lsi.log
      seqNum: 0x0000282f
      Time: Sat Jun 16 05:55:05 2012
      Code: 0x00000023
      Class: 0
      Locale: 0x20
      Event Description: Patrol Read complete
      Event Data:
      ===========
      None


      seqNum: 0x000027ec
      Time: Sat Jun 16 03:00:00 2012
      Code: 0x00000027
      Class: 0
      Locale: 0x20
      Event Description: Patrol Read started
      [...]

      The last two events show that a patrol read (which can affect performance) occurred between
      3:00 and 5:55 a.m. Patrol reads were mentioned in Section 9.4.3, Storage Types; they read disk
      blocks and verify their checksums.

      MegaCli has many other options, which can show the adapter information, disk device informa-
      tion, virtual device information, enclosure information, battery status, and physical errors. These
      help identify issues of configuration and errors. Even with this information, some types of issues
      can’t be analyzed easily, such as exactly why a particular I/O took hundreds of milliseconds.

      Check the vendor documentation to see what interface, if any, exists for disk controller analysis.


