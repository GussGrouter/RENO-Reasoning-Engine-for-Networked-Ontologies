      9.6.13      smartctl
      The disk has logic to control disk operation, including queueing, caching, and error handling.
      Similarly to disk controllers, the internal behavior of the disk is not directly observable by the
      operating system and instead is usually inferred by observing I/O requests and their latency.
                                                                           9.6 Observability Tools      485


Many modern drives provide SMART (Self-Monitoring, Analysis and Reporting Technology)
data, which provides various health statistics. The following output of smartctl(8) on Linux
shows the sort of data available (this is accessing the first disk in a virtual RAID device, using -d
megaraid,0):

# smartctl --all -d megaraid,0 /dev/sdb
smartctl 5.40 2010-03-16 r3077 [x86_64-unknown-linux-gnu] (local build)
Copyright (C) 2002-10 by Bruce Allen, http://smartmontools.sourceforge.net


Device: SEAGATE      ST3600002SS          Version: ER62
Serial number: 3SS0LM01
Device type: disk
Transport protocol: SAS
Local Time is: Sun Jun 17 10:11:31 2012 UTC
Device supports SMART and is Enabled
Temperature Warning Disabled or Not Supported
SMART Health Status: OK


Current Drive Temperature:           23 C
Drive Trip Temperature:              68 C
Elements in grown defect list: 0
Vendor (Seagate) cache information
  Blocks sent to initiator = 3172800756
  Blocks received from initiator = 2618189622
  Blocks read from cache and sent to initiator = 854615302
  Number of read and write commands whose size <= segment size = 30848143
  Number of read and write commands whose size > segment size = 0
Vendor (Seagate/Hitachi) factory information
  number of hours powered up = 12377.45
  number of minutes until next internal SMART test = 56


Error counter log:
             Errors Corrected by                Total    Correction    Gigabytes    Total
                 ECC            rereads/       errors    algorithm     processed uncorrected
             fast | delayed rewrites         corrected invocations [10^9 bytes] errors
read:     7416197           0         0      7416197     7416197      1886.494            0
write:           0          0         0             0           0     1349.999            0
verify: 142475069            0           0   142475069    142475069    22222.134            0


Non-medium error count:           2661


SMART Self-test log
Num   Test                 Status         segment    LifeTime    LBA_first_err [SK ASC ASQ]
      Description                         number     (hours)
486   Chapter 9 Disks


      # 1   Background long      Completed        16         3                    - [-     -     -]
      # 2   Background short     Completed        16         0                    - [-     -     -]


      Long (extended) Self Test duration: 6400 seconds [106.7 minutes]

      While this is very useful, it does not have the resolution to answer questions about individual
      slow disk I/O, as kernel tracing frameworks do. The corrected errors information should be use-
      ful for monitoring, to help predict disk failure before it happens, as well as to confirm that a disk
      has failed or is failing.


