fio
The Flexible IO Tester (fio) by Jens Axboe is a customizable file system benchmark tool with
many advanced features [Axboe 20]. Two that have led me to use it instead of other benchmark
tools are:
Non-uniform random distributions, which can more accurately simulate a real-world
access pattern (e.g., -random_distribution=pareto:0.9)

■

Reporting of latency percentiles, including 99.00, 99.50, 99.90, 99.95, 99.99

■

Here is an example command line for a random read workload with an 8 Kbyte I/O size, a 5 Gbyte
working set size, and a non-uniform access pattern (pareto:0.9):
# fio --runtime=60 --time_based --clocksource=clock_gettime --name=randread -numjobs=1 --rw=randread --random_distribution=pareto:0.9 --bs=8k --size=5g -filename=fio.tmp

(Omitted in this processed extract: full fio ASCII report — see PDF.)

Summary numbers from Gregg’s example include completion latency stats and clat percentiles;
the 99.99th percentile shows a 63 ms latency in his walkthrough.

The latency percentiles (clat) show very low latencies up to the 50th percentile, which I would
assume, based on the latency (5 to 7 microseconds), to be cache hits. The remaining percentiles
show the effect of cache misses, including the tail of the queue; in this case, the 99.99th percentile is showing a 63 ms latency.

While these percentiles lack information to really understand what is probably a multimode
distribution, they do focus on the most interesting part: the tail of the slower mode (disk I/O).
For a similar but simpler tool, you can try SysBench (an example of using SysBench for CPU
analysis in Chapter 6, Section 6.8.2, SysBench). On the other hand, if you want even more control,
try FileBench.
