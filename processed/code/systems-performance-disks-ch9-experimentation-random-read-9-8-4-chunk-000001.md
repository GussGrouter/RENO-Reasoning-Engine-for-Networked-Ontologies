9.8.4     Random Read Example
As an example experiment, I wrote a custom tool to perform a random 8 Kbyte read workload of
a disk device path. From one to five instances of the tool were run concurrently, with iostat(1)
running. The write columns, which contained zeros, have been removed:

Device:      rrqm/s        r/s      rkB/s   avgrq-sz      aqu-sz r_await     svctm   %util
sda          878.00     234.00   2224.00        19.01       1.00      4.27    4.27 100.00
[...]
492   Chapter 9 Disks


      Device:     rrqm/s          r/s     rkB/s   avgrq-sz    aqu-sz r_await       svctm   %util
      sda        1233.00     311.00     3088.00      19.86        2.00      6.43    3.22 100.00
      [...]
      Device:     rrqm/s          r/s     rkB/s   avgrq-sz    aqu-sz r_await       svctm   %util
      sda        1366.00     358.00     3448.00      19.26        3.00      8.44    2.79 100.00
      [...]
      Device:     rrqm/s          r/s     rkB/s   avgrq-sz    aqu-sz r_await       svctm   %util
      sda        1775.00     413.00     4376.00      21.19        4.01      9.66    2.42 100.00
      [...]
      Device:     rrqm/s          r/s     rkB/s   avgrq-sz    aqu-sz r_await       svctm   %util
      sda        1977.00     423.00     4800.00      22.70        5.04     12.08    2.36 100.00

      Note the stepped increases in aqu-sz, and the increased latency of r_await.


