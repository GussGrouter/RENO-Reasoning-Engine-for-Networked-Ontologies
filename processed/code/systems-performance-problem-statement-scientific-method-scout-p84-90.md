                                                                                  2.5 Methodology      45


systems, predicting that cache misses will be higher on the smaller system. An experimental test
would be to increase the cache size (adding RAM), predicting that performance will improve.
Another, perhaps easier, experimental test is to artificially reduce the cache size (using tunable
parameters), predicting that performance will be worse.

The following are some more examples.


Example (Observational)
   1. Question: What is causing slow database queries?

   2. Hypothesis: Noisy neighbors (other cloud computing tenants) are performing disk I/O,
      contending with database disk I/O (via the file system).

   3. Prediction: If file system I/O latency is measured during a query, it will show that the file
      system is responsible for the slow queries.

   4. Test: Tracing of database file system latency as a ratio of query latency shows that less than
      5% of the time is spent waiting for the file system.

   5. Analysis: The file system and disks are not responsible for slow queries.

Although the issue is still unsolved, some large components of the environment have been
ruled out. The person conducting this investigation can return to step 2 and develop a new
hypothesis.


Example (Experimental)
   1. Question: Why do HTTP requests take longer from host A to host C than from host B to
      host C?

   2. Hypothesis: Host A and host B are in different data centers.

   3. Prediction: Moving host A to the same data center as host B will fix the problem.

   4. Test: Move host A and measure performance.
   5. Analysis: Performance has been fixed—consistent with the hypothesis.

If the problem wasn’t fixed, reverse the experimental change (move host A back, in this case)
before beginning a new hypothesis—changing multiple factors at once makes it harder to iden-
tify which one mattered!


Example (Experimental)
   1. Question: Why did file system performance degrade as the file system cache grew in size?

   2. Hypothesis: A larger cache stores more records, and more compute is required to manage a
      larger cache than a smaller one.

   3. Prediction: Making the record size progressively smaller, and therefore causing more
      records to be used to store the same amount of data, will make performance progressively
      worse.

   4. Test: Test the same workload with progressively smaller record sizes.
46   Chapter 2 Methodologies


        5. Analysis: Results are graphed and are consistent with the prediction. Drill-down analysis
           is now performed on the cache management routines.

     This is an example of a negative test—deliberately hurting performance to learn more about the
     target system.


     2.5.7 Diagnosis Cycle
     Similar to the scientific method is the diagnosis cycle:

          hypothesis → instrumentation → data → hypothesis

     Like the scientific method, this method also deliberately tests a hypothesis through the collec-
     tion of data. The cycle emphasizes that the data can lead quickly to a new hypothesis, which is
     tested and refined, and so on. This is similar to a doctor making a series of small tests to diagnose a
     patient and refining the hypothesis based on the result of each test.

     Both of these approaches have a good balance of theory and data. Try to move from hypothe-
     sis to data quickly, so that bad theories can be identified early and discarded, and better ones
     developed.


     2.5.8 Tools Method
     A tools-oriented approach is as follows:

        1. List available performance tools (optionally, install or purchase more).

        2. For each tool, list useful metrics it provides.

        3. For each metric, list possible ways to interpret it.

     The result of this is a prescriptive checklist showing which tool to run, which metrics to read,
     and how to interpret them. While this can be fairly effective, it relies exclusively on available
     (or known) tools, which can provide an incomplete view of the system, similar to the streetlight
     anti-method. Worse, the user is unaware that they have an incomplete view—and may remain
     unaware. Issues that require custom tooling (e.g., dynamic tracing) may never be identified
     and solved.

     In practice, the tools method does identify certain resource bottlenecks, errors, and other types
     of problems, though it may not do this efficiently.

     When a large number of tools and metrics are available, it can be time-consuming to iterate
     through them. The situation gets worse when multiple tools appear to have the same functional-
     ity and you spend additional time trying to understand the pros and cons of each. In some cases,
     such as file system micro-benchmark tools, there are over a dozen tools to choose from, when
     you may need only one.4


     4
       As an aside, an argument I’ve encountered to support multiple overlapping tools is that “competition is good.”
     I would be cautious about this: while it can be helpful to have overlapping tools for cross-checking results (and I fre-
     quently cross-check BPF tools using Ftrace), multiple overlapping tools can become a waste of developer time that
     could be more effectively used elsewhere, as well as a waste of time for end users who must evaluate each choice.
                                                                                 2.5 Methodology        47



2.5.9      The USE Method
The utilization, saturation, and errors (USE) method should be used early in a performance
investigation to identify systemic bottlenecks [Gregg 13b]. It is a methodology that focuses on
system resources and can be summarized as:

    For every resource, check utilization, saturation, and errors.

These terms are defined as follows:
    ■   Resources: All physical server functional components (CPUs, buses, . . .). Some software
        resources can also be examined, provided that the metrics make sense.
    ■   Utilization: For a set time interval, the percentage of time that the resource was busy
        servicing work. While busy, the resource may still be able to accept more work; the degree
        to which it cannot do so is identified by saturation.
    ■   Saturation: The degree to which the resource has extra work that it can’t service, often
        waiting on a queue. Another term for this is pressure.
    ■   Errors: The count of error events.

For some resource types, including main memory, utilization is the capacity of the resource that is
used. This is different from the time-based definition and was explained earlier in Section 2.3.11,
Utilization. Once a capacity resource reaches 100% utilization, more work cannot be accepted,
and the resource either queues the work (saturation) or returns errors, which are also identified
using the USE method.

Errors should be investigated because they can degrade performance but may not be immedi-
ately noticed when the failure mode is recoverable. This includes operations that fail and are
retried, and devices that fail in a pool of redundant devices.

In contrast with the tools method, the USE method involves iterating over system resources
instead of tools. This helps you create a complete list of questions to ask, and only then do you
search for tools to answer them. Even when tools cannot be found to answer some questions, the
knowledge that these questions are unanswered can be extremely useful for the performance
analyst: they are now “known-unknowns.”

The USE method also directs analysis to a limited number of key metrics, so that all system resources
are checked as quickly as possible. After this, if no issues have been found, other methodologies
can be used.


Procedure
The USE method is pictured as the flowchart in Figure 2.12. Errors are checked first because they
are usually quick to interpret (they are usually an objective and not subjective metric), and it can
be time-efficient to rule them out before investigating the other metrics. Saturation is checked
second because it is quicker to interpret than utilization: any level of saturation can be an issue.
48   Chapter 2 Methodologies




     Figure 2.12 The USE method flow

     This method identifies problems that are likely to be system bottlenecks. Unfortunately, a sys-
     tem may be suffering from more than one performance problem, so the first thing you find may
     be a problem but not the problem. Each discovery can be investigated using further methodolo-
     gies, before returning to the USE method as needed to iterate over more resources.


     Expressing Metrics
     The USE method metrics are usually expressed as follows:

        ■   Utilization: As a percent over a time interval (e.g., “One CPU is running at 90%
            utilization”)
        ■   Saturation: As a wait-queue length (e.g., “The CPUs have an average run-queue length
            of four”)
        ■   Errors: Number of errors reported (e.g., “This disk drive has had 50 errors”)
                                                                                  2.5 Methodology       49


Though it may seem counterintuitive, a short burst of high utilization can cause saturation and
performance issues, even though the overall utilization is low over a long interval. Some mon-
itoring tools report utilization over 5-minute averages. CPU utilization, for example, can vary
dramatically from second to second, so a 5-minute average may disguise short periods of 100%
utilization and, therefore, saturation.

Consider a toll plaza on a highway. Utilization can be defined as how many tollbooths were
busy servicing a car. Utilization at 100% means you can’t find an empty booth and must
queue behind someone (saturation). If I told you the booths were at 40% utilization across the
entire day, could you tell me whether any cars had queued at any time during that day? They
probably did during rush hour, when utilization was at 100%, but that isn’t visible in the daily
average.


Resource List
The first step in the USE method is to create a list of resources. Try to be as complete as possible.
Here is a generic list of server hardware resources, along with specific examples:
    ■   CPUs: Sockets, cores, hardware threads (virtual CPUs)
    ■   Main memory: DRAM
    ■   Network interfaces: Ethernet ports, Infiniband
    ■   Storage devices: Disks, storage adapters
    ■   Accelerators: GPUs, TPUs, FPGAs, etc., if in use
    ■   Controllers: Storage, network
    ■   Interconnects: CPU, memory, I/O

Each component typically acts as a single resource type. For example, main memory is a capacity
resource, and network interfaces are an I/O resource (which can mean either IOPS or throughput).
Some components can behave as multiple resource types: for example, a storage device is both
an I/O resource and a capacity resource. Consider all types that can lead to performance bottle-
necks. Also note that I/O resources can be further studied as queueing systems, which queue and
then service these requests.

Some physical components, such as hardware caches (e.g., CPU caches), can be left out of
your checklist. The USE method is most effective for resources that suffer performance degrada-
tion under high utilization or saturation, leading to bottlenecks, while caches improve perfor-
mance under high utilization. These can be checked using other methodologies. If you are unsure
whether to include a resource, include it, and then see how well the metrics work in practice.


Functional Block Diagram
Another way to iterate over resources is to find or draw a functional block diagram for the
system, such as the one shown in Figure 2.13. Such a diagram also shows relationships, which
can be very useful when looking for bottlenecks in the flow of data.
50   Chapter 2 Methodologies




     Figure 2.13 Example two-processor functional block diagram

     CPU, memory, and I/O interconnects and buses are often overlooked. Fortunately, they are not
     common system bottlenecks, as they are typically designed to provide an excess of throughput.
     Unfortunately, if they are, the problem can be difficult to solve. Maybe you can upgrade the main
     board, or reduce load; for example, “zero copy” software techniques lighten memory bus load.

     To investigate interconnects, see CPU Performance Counters in Chapter 6, CPUs, Section 6.4.1,
     Hardware.


     Metrics
     Once you have your list of resources, consider the metric types appropriate to each: utilization,
     saturation, and errors. Table 2.6 shows some example resources and metric types, along with
     possible metrics (generic OS).


     Table 2.6   Example USE method metrics
     Resource               Type           Metric
     CPU                    Utilization    CPU utilization (either per CPU or a system-wide average)
     CPU                    Saturation     Run queue length, scheduler latency, CPU pressure
                                           (Linux PSI)
     Memory                 Utilization    Available free memory (system-wide)
     Memory                 Saturation     Swapping (anonymous paging), page scanning, out-of-
                                           memory events, memory pressure (Linux PSI)
     Network interface      Utilization    Receive throughput/max bandwidth, transmit throughput/
                                           max bandwidth
     Storage device I/O     Utilization    Device busy percent
                                                                                              2.5 Methodology        51



Resource                   Type              Metric
Storage device I/O         Saturation        Wait queue length, I/O pressure (Linux PSI)
Storage device I/O         Errors            Device errors (“soft,” “hard”)



These metrics can be either averages per interval or counts.

Repeat for all combinations, and include instructions for fetching each metric. Take note of met-
rics that are not currently available; these are the known-unknowns. You’ll end up with a list of
about 30 metrics, some of which are difficult to measure, and some of which can’t be measured
at all. Fortunately, the most common issues are usually found with the easier metrics (e.g., CPU
saturation, memory capacity saturation, network interface utilization, disk utilization), so these
can be checked first.

Some examples of harder combinations are provided in Table 2.7.


Table 2.7      Example USE method advanced metrics
Resource                     Type              Metric
CPU                          Errors            For example, machine check exceptions, CPU cache
                                               errors5
Memory                       Errors            For example, failed malloc()s (although a default Linux
                                               kernel configuration makes this rare due to overcommit)
Network                      Saturation        Saturation-related network interface or OS errors, e.g.,
                                               Linux “overruns”
Storage controller           Utilization       Depends on the controller; it may have a maximum IOPS
                                               or throughput that can be checked against current activity
CPU interconnect             Utilization       Per-port throughput/maximum bandwidth (CPU
                                               performance counters)
Memory interconnect          Saturation        Memory stall cycles, high cycles per instruction (CPU
                                               performance counters)
I/O interconnect             Utilization       Bus throughput/maximum bandwidth (performance
                                               counters may exist on your HW, e.g., Intel “uncore”
                                               events)



Some of these may not be available from standard operating system tools and may require the
use of dynamic tracing or CPU performance monitoring counters.

Appendix A is an example USE method checklist for Linux systems, iterating over all combina-
tions for hardware resources with the Linux observability toolset, and includes some software
resources, such as those described in the next section.

5
 For example, recoverable error-correcting code (ECC) errors for CPU cache lines (if supported). Some kernels will
offline a CPU if an increase in these is detected.
