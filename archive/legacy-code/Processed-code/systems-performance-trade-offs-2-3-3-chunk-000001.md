# systems-performance-trade-offs-2-3-3 (chunk 000001)

# Systems Performance — 2.3.3 Trade-Offs (PDF pages 64–71)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-concepts-2-3-3-to-2-3-6-p64-71.md
- Slice: 2.3.3 Trade-Offs

---

2.3.3       Trade-Offs
     You should be aware of some common performance trade-offs. The good/fast/cheap “pick two”
     trade-off is shown in Figure 2.4, alongside the terminology adjusted for IT projects.




     Figure 2.4 Trade-offs: pick two
                                                                                   2.3    Concepts   27


Many IT projects choose on-time and inexpensive, leaving performance to be fixed later. This
choice can become problematic when earlier decisions inhibit improving performance, such as
choosing and populating a suboptimal storage architecture, using a programming language or
operating system that is implemented inefficiently, or selecting a component that lacks compre-
hensive performance analysis tools.

A common trade-off in performance tuning is the one between CPU and memory, as memory
can be used to cache results, reducing CPU usage. On modern systems with an abundance of
CPU, the trade may work the other way: CPU time may be spent compressing data to reduce
memory usage.

Tunable parameters often come with trade-offs. Here are a couple of examples:

   ■    File system record size (or block size): Small record sizes, close to the application I/O
        size, will perform better for random I/O workloads and make more efficient use of the file
        system cache while the application is running. Large record sizes will improve streaming
        workloads, including file system backups.
   ■    Network buffer size: Small buffer sizes will reduce the memory overhead per connection,
        helping the system scale. Large sizes will improve network throughput.

Look for such trade-offs when making changes to the system.
