9.8.2       Custom Load Generators
To test custom workloads, you can write your own load generator and measure resulting perfor-
mance using iostat(1). A custom load generator can be a short C program that opens the device
path and applies the intended workload. On Linux, the block special devices files can be opened
with O_DIRECT, to avoid buffering. If you use higher-level languages, try to use system-level
interfaces that avoid library buffering (e.g., sysread() in Perl) at least, and preferably avoid kernel
buffering as well (e.g., O_DIRECT).

