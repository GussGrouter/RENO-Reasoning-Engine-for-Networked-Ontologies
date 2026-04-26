9.6.3

PSI

Linux pressure stall information (PSI), added in Linux 4.20, includes statistics for I/O saturation.
These not only show if there is I/O pressure, but how it is changing over the last five minutes.
Example output:
# cat /proc/pressure/io
some avg10=63.11 avg60=32.18 avg300=8.62 total=667212021
full avg10=60.76 avg60=31.13 avg300=8.35 total=622722632

This output shows that I/O pressure is increasing, with a higher 10-second average (63.11) than
the 300-second average (8.62). These averages are percentages of time that a task was I/O stalled.
The some line shows when some tasks (threads) were affected, and the full line shows when all
runnable tasks were affected.
As with load averages, this can be a high-level metric used for alerting. Once you become aware
that there is a disk performance issue, you can use other tools to find the root causes, including
pidstat(8) for disk statistics by process.

