9.9        Tuning
Many tuning approaches were covered in Section 9.5, Methodology, including cache tuning,
scaling, and workload characterization, which can help you identify and eliminate unnecessary
work. Another important area of tuning is the storage configuration, which can be studied as
part of a static performance tuning methodology.

The following sections show areas that can be tuned: the operating system, disk devices, and
disk controller. Available tunable parameters vary between versions of an operating system,
models of disks, disk controllers, and their firmware; see their respective documentation. While
changing tunables can be easy to do, the default settings are usually reasonable and rarely need
much adjusting.


9.9.1      Operating System Tunables
These include ionice(1), resource controls, and kernel tunable parameters.


ionice
On Linux, the ionice(1) command can be used to set an I/O scheduling class and priority for a
process. The scheduling classes are identified numerically:
    ■   0, none: No class specified, so the kernel will pick a default—best effort, with a priority
        based on the process nice value.
    ■   1, real-time: Highest-priority access to the disk. If misused, this can starve other processes
        (just like the RT CPU scheduling class).
    ■   2, best effort: Default scheduling class, supporting priorities 0–7, with 0 being the
        highest.
    ■   3, idle: Disk I/O allowed only after a grace period of disk idleness.
494   Chapter 9 Disks


      Example usage:

      # ionice -c 3 -p 1623

      This puts process ID 1623 in the idle I/O scheduling class. This may be desirable for long-running
      backup jobs so that they are less likely to interfere with the production workload.

