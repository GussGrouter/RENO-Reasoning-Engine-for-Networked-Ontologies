7.5.5 slabtop
The Linux slabtop(1) command prints kernel slab cache usage from the slab allocator. Like
top(1), it refreshes the screen in real time.
Here is some example output:
# slabtop -sc
Active / Total Objects (% used)

: 686110 / 867574 (79.1%)

Active / Total Slabs (% used)

: 30948 / 30948 (100.0%)

Active / Total Caches (% used)

: 99 / 164 (60.4%)

Active / Total Size (% used)

: 157680.28K / 200462.06K (78.7%)

Minimum / Average / Maximum Object : 0.01K / 0.23K / 12.00K

333

334

Chapter 7 Memory

OBJS ACTIVE

USE OBJ SIZE

SLABS OBJ/SLAB CACHE SIZE NAME

45450

33712

74%

1.05K

3030

15

48480K ext4_inode_cache

161091

81681

50%

0.19K

7671

21

30684K dentry

222963 196779

88%

0.10K

5717

39

22868K buffer_head

35763

35471

99%

0.58K

2751

13

22008K inode_cache

26033

13859

53%

0.57K

1860

14

14880K radix_tree_node

93330

80502

86%

0.13K

3111

30

12444K kernfs_node_cache

2104

2081

98%

4.00K

263

8

8416K kmalloc-4k

528

431

81%

7.50K

132

4

4224K task_struct

[...]

The output has a summary at the top and a list of slabs, including their object count (OBJS), how
many are active (ACTIVE), percent used (USE), the size of the objects (OBJ SIZE, bytes), and the
total size of the cache (CACHE SIZE, bytes). In this example, the -sc option was used to sort by
cache size, with the largest at the top: ext4_inode_cache.
The slab statistics are from /proc/slabinfo and can also be printed by vmstat -m.

7.5.6

numastat

The numastat(8)8 tool provides statistics for non-uniform memory access (NUMA) systems, typically those with multiple CPU sockets. Here is some example output from a two-socket system:
# numastat
node0

node1

numa_hit

210057224016

151287435161

numa_miss

9377491084

291611562

numa_foreign

291611562

9377491084

36476

36665

local_node

210056887752

151286964112

other_node

9377827348

292082611

interleave_hit

This system has two NUMA nodes, one for each memory bank attached to each socket. Linux
tries to allocate memory on the nearest NUMA node, and numastat(8) shows how successful this
is. Key statistics are:
■

■

■

8

numa_hit: Memory allocations on the intended NUMA node.
numa_miss + numa_foreign: Memory allocations not on the preferred NUMA node.
(numa_miss shows local allocations that should have been elsewhere, and numa_foreign
shows remote allocations that should have been local.)
other_node: Memory allocations on this node while the process was running elsewhere.

Origin: Andi Kleen wrote the original numastat tool as a perl script around 2003; Bill Gray wrote the current version
in 2012.

7.5 Observability Tools

The example output shows the NUMA allocation policy performing well: a high number of hits
compared to other statistics. If the hit ratio is much lower, you may consider adjusting NUMA
tunables in sysctl(8), or using other approaches to improve memory locality (e.g., partitioning
workloads or the system, or choosing a different system with fewer NUMA nodes). If there is no
way to improve NUMA, numastat(8) does at least help explain poor memory I/O performance.
numastat(8) supports -n to print statistics in Mbytes, and -m to print the output in the style
of /proc/meminfo. Depending on your Linux distribution, numastat(8) may be available in a
numactl package.

