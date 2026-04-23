<!-- pdftotext -f 321 -l 360 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continued) -->

6.8 Experimentation
This section describes tools for actively testing CPU performance. See Section 6.5.11, MicroBenchmarking, for background.
When using these tools, it’s a good idea to leave mpstat(1) continually running to confirm CPU
usage and parallelism.

6.8.1

Ad Hoc

While this is trivial and doesn’t measure anything, it can be a useful known workload for confirming that observability tools show what they claim to show. This creates a single-threaded
workload that is CPU-bound (“hot on one CPU”):
# while :; do :; done &

This is a Bourne shell program that performs an infinite loop in the background. It will need to
be killed once you no longer need it.

293

294

Chapter 6 CPUs

6.8.2 SysBench
The SysBench system benchmark suite has a simple CPU benchmark tool that calculates prime
numbers. For example:
# sysbench --num-threads=8 --test=cpu --cpu-max-prime=100000 run
sysbench 0.4.12:

multi-threaded system evaluation benchmark

Running the test with following options:
Number of threads: 8
Doing CPU performance benchmark
Threads started!
Done.
Maximum prime number checked in CPU test: 100000

Test execution summary:
total time:

30.4125s

total number of events:

10000

total time taken by event execution: 243.2310
per-request statistics:
min:

24.31ms

avg:

24.32ms

max:
approx.

32.44ms
95 percentile:

24.32ms

Threads fairness:
events (avg/stddev):

1250.0000/1.22

execution time (avg/stddev):

30.4039/0.01

This executed eight threads, with a maximum prime number of 100,000. The runtime was
30.4 s, which can be used for comparison with the results from other systems or configurations
(assuming many things, such as that identical compiler options were used to build the software;
see Chapter 12, Benchmarking).
