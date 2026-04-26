      9.9.3      Disk Controller Tunables
      The available disk controller tunable parameters depend on the disk controller model and
      vendor. To give you an idea of what these may include, the following shows some of the settings
      from a Dell PERC 6 card, viewed using the MegaCli command:

      # MegaCli -AdpAllInfo -aALL
      [...]
      Predictive Fail Poll Interval           : 300sec
      Interrupt Throttle Active Count         : 16
                                                                                    9.10   Exercises   495


Interrupt Throttle Completion          : 50us
Rebuild Rate                           : 30%
PR Rate                                : 0%
BGI Rate                               : 1%
Check Consistency Rate                 : 1%
Reconstruction Rate                    : 30%
Cache Flush Interval                   : 30s
Max Drives to Spinup at One Time : 2
Delay Among Spinup Groups              : 12s
Physical Drive Coercion Mode           : 128MB
Cluster Mode                           : Disabled
Alarm                                  : Disabled
Auto Rebuild                           : Enabled
Battery Warning                        : Enabled
Ecc Bucket Size                        : 15
Ecc Bucket Leak Rate                   : 1440 Minutes
Load Balance Mode                      : Auto
[...]

Each setting has a reasonably descriptive name and is described in more detail in the vendor
documentation.


