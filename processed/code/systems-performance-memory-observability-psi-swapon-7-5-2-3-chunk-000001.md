7.5.2 PSI
Linux pressure stall information (PSI), added in Linux 4.20, includes statistics for memory saturation. These not only show if there is memory pressure, but how it is changing in the last five
minutes. Example output:

7.5 Observability Tools

# cat /proc/pressure/memory
some avg10=2.84 avg60=1.23 avg300=0.32 total=1468344
full avg10=1.85 avg60=0.66 avg300=0.16 total=702578

This output shows that memory pressure is increasing, with a higher 10-second average (2.84)
than the 300-second average (0.32). These averages are percentages of time that a task was
memory stalled. The some line shows when some tasks (threads) were affected, and the full line
shows when all runnable tasks were affected.
PSI statistics are also tracked per cgroup2 (cgroups are covered in Chapter 11, Cloud Computing)
[Facebook 19].

7.5.3

swapon

swapon(1) can show whether swap devices have been configured and how much of their volume
is in use. For example:
$ swapon
NAME

TYPE

SIZE

USED PRIO

/dev/dm-2 partition 980M 611.6M

-2

/swap1

-3

file

30G

10.9M

This output shows two swap devices: a physical disk partition of 980 Mbytes, and a file named
/swap1 of 30 Gbytes. The output also shows how much both are in use. Many systems nowadays
do not have swap configured; in this case, swapon(1) will not print any output.
If a swap device has active I/O, that can be seen in the si and so columns in vmstat(1), and as
device I/O in iostat(1) (Chapter 9).

