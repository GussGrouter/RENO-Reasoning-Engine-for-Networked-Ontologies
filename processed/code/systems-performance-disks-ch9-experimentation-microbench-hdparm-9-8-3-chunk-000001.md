9.8.3     Micro-Benchmark Tools
Available disk benchmark tools include, for example, hdparm(8) on Linux:

# hdparm -Tt /dev/sdb


/dev/sdb:
 Timing cached reads:        16718 MB in    2.00 seconds = 8367.66 MB/sec
 Timing buffered disk reads:        846 MB in    3.00 seconds = 281.65 MB/sec

The -T option tests cached reads, and -t tests disk device reads. The results show the dramatic
difference between on-disk cache hits and misses.

Study the tool documentation to understand any caveats, and see Chapter 12, Benchmarking,
for more background on micro-benchmarking. Also see Chapter 8, File Systems, for tools that
test disk performance via the file system (for which many more are available).

