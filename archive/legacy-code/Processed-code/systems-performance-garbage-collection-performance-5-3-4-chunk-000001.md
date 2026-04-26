5.3.4 Garbage Collection
Some languages use automatic memory management, where allocated memory does not need
to be explicitly freed, leaving that to an asynchronous garbage collection process. While this
makes programs easier to write, there can be disadvantages:
■

■

Memory growth: There is less control of the application’s memory usage, which may
grow when objects are not identified automatically as eligible to be freed. If the application grows too large, it may either hit its own limits or encounter system paging (Linux
swapping), severely harming performance.
CPU cost: GC will typically run intermittently and involves searching or scanning objects
in memory. This consumes CPU resources, reducing what is available to the application
for short periods. As the memory of the application grows, CPU consumption by GC may
also grow. In some cases this can reach the point where GC continually consumes an
entire CPU.

185

186

Chapter 5 Applications

■

Latency outliers: Application execution may be paused while GC executes, causing
occasional application responses with high latency that were interrupted by GC.8 This
depends on the GC type: stop-the-world, incremental, or concurrent.

GC is a common target for performance tuning to reduce CPU cost and occurrence of latency
outliers. For example, the Java VM provides many tunable parameters to set the GC type, number of GC threads, maximum heap size, target heap free ratio, and more.
If tuning is not effective, the problem may be the application creating too much garbage, or
leaking references. These are issues for the application developer to resolve. One approach is
to allocate fewer objects, when possible, to reduce the GC load. Observability tools that show
object allocations and their code paths can be used to find potential targets for elimination.

