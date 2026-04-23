8.7.3

Cache Flushing

Linux provides a way to flush (drop entries from) file system caches, which may be useful for
benchmarking performance from a consistent and “cold” cache state, as you would have after
system boot. This mechanism is described very simply in the kernel source documentation
(Documentation/sysctl/vm.txt) as:
To free pagecache:
echo 1 > /proc/sys/vm/drop_caches
To free reclaimable slab objects (includes dentries and inodes):
echo 2 > /proc/sys/vm/drop_caches
To free slab objects and pagecache:
echo 3 > /proc/sys/vm/drop_caches

It can be especially useful to free everything (3) before other benchmark runs, so that the system
begins in a consistent state (a cold cache), helping to provide consistent benchmark results.
