7.5.1

vmstat

The virtual memory statistics command, vmstat(8), provides a high-level view of system memory
health, including current free memory and paging statistics. CPU statistics are also included, as
described in Chapter 6, CPUs.
When it was introduced by Bill Joy and Ozalp Babaoglu in 1979 for BSD, the original man page
included:
BUGS: So many numbers print out that it’s sometimes hard to figure out what to watch.
Here is example output from the Linux version:
$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu---swpd

free

buff

cache

si

so

r

b

bi

bo

in

cs us sy id wa

4

0

0 34454064 111516 13438596

0

0

0

5

2

0

0 100

0

4

0

0 34455208 111516 13438596

0

0

0

0 2262 15303 16 12 73

0

5

0

0 34455588 111516 13438596

0

0

0

0 1961 15221 15 11 74

0

4

0

0 34456300 111516 13438596

0

0

0

0 2343 15294 15 11 73

0

[...]

0

329

330

Chapter 7 Memory

This version of vmstat(8) does not print summary-since-boot values for the procs or memory
columns on the first line of output, instead showing current status immediately. The columns
are in kilobytes by default and are:
■

swpd: Amount of swapped-out memory

■

free: Free available memory

■

buff: Memory in the buffer cache

■

cache: Memory in the page cache

■

si: Memory swapped in (paging)

■

so: Memory swapped out (paging)

The buffer and page caches are described in Chapter 8, File Systems. It is normal for the free
memory in the system to drop after boot and be used by these caches to improve performance. It
can be released for application use when needed.
If the si and so columns are continually nonzero, the system is under memory pressure and is
swapping to a swap device or file (see swapon(8)). Other tools, including those that show memory
by process (e.g., top(1), ps(1)), can be used to investigate what is consuming memory.
On systems with large amounts of memory, the columns can become unaligned and a little
difficult to read. You can try changing the output units to megabytes using the -S option (use m
for 1000000, and M for 1048576):
$ vmstat -Sm 1
procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu---r

b

swpd

free

buff

cache

si

so

bi

bo

in

cs us sy id wa

4

0

0

35280

114

13761

0

0

0

5

2

1

0 100

0

4

0

0

35281

114

13761

0

0

0

0 2027 15146 16 13 70

0

0

[...]

There is also a -a option to print a breakdown of inactive and active memory from the page cache:
$ vmstat -a 1
procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu---swpd

free

inact active

r

b

si

so

bo

in

5

0

0 34453536 10358040 3201540

0

0

bi
0

5

2

cs us sy id wa
0 100

0

4

0

0 34453228 10358040 3200648

0

0

0

0 2464 15261 16 12 71

0

0

0

[...]

These memory statistics can be printed as a list using the lowercase -s option.

