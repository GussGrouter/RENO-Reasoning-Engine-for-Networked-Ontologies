                                                                                 2.5 Methodology       43


example, an application change may improve performance because it works around a database
or operating system bug that is later fixed. But the application will still have that tuning that no
longer makes sense, and that no one understood properly in the first place.

Another risk is where a change that isn’t properly understood causes a worse problem during
peak production load, and a need to back out the change.


2.5.3     Blame-Someone-Else Anti-Method
This anti-methodology follows these steps:

   1. Find a system or environment component for which you are not responsible.

   2. Hypothesize that the issue is with that component.

   3. Redirect the issue to the team responsible for that component.

   4. When proven wrong, go back to step 1.

    “Maybe it’s the network. Can you check with the network team if they’ve had dropped
    packets or something?”

Instead of investigating performance issues, the user of this methodology makes them someone
else’s problem, which can be wasteful of other teams’ resources when it turns out not to be
their problem after all. This anti-methodology can be identified by a lack of data leading to the
hypothesis.

To avoid becoming a victim of blame-someone-else, ask the accuser for screenshots showing
which tools were run and how the output was interpreted. You can take these screenshots and
interpretations to someone else for a second opinion.


2.5.4     Ad Hoc Checklist Method
Stepping through a canned checklist is a common methodology used by support professionals
when asked to check and tune a system, often in a short time frame. A typical scenario involves
the deployment of a new server or application in production, and a support professional spending
half a day checking for common issues now that the system is under real load. These checklists
are ad hoc and are built from recent experience and issues for that system type.

Here is an example checklist entry:

    Run iostat –x 1 and check the r_await column. If this is consistently over 10 (ms)
    during load, then either disk reads are slow or the disk is overloaded.

A checklist may be composed of a dozen or so such checks.

While these checklists can provide the most value in the shortest time frame, they are point-in-
time recommendations (see Section 2.3, Concepts) and need to be frequently refreshed to stay
current. They also tend to focus on issues for which there are known fixes that can be easily
documented, such as the setting of tunable parameters, but not custom fixes to the source code
or environment.
44   Chapter 2 Methodologies


     If you are managing a team of support professionals, an ad hoc checklist can be an effective way
     to ensure that everyone knows how to check for common issues. A checklist can be written to be
     clear and prescriptive, showing how to identify each issue and what the fix is. But bear in mind
     that this list must be constantly updated.


     2.5.5 Problem Statement
     Defining the problem statement is a routine task for support staff when first responding to
     issues. It’s done by asking the customer the following questions:

        1. What makes you think there is a performance problem?

        2. Has this system ever performed well?

        3. What changed recently? Software? Hardware? Load?

        4. Can the problem be expressed in terms of latency or runtime?

        5. Does the problem affect other people or applications (or is it just you)?

        6. What is the environment? What software and hardware are used? Versions?
           Configuration?

     Just asking and answering these questions often points to an immediate cause and solution.
     The problem statement has therefore been included here as its own methodology and should
     be the first approach you use when tackling a new issue.

     I have solved performance issues over the phone by using the problem statement method alone,
     and without needing to log in to any server or look at any metrics.


     2.5.6     Scientific Method
     The scientific method studies the unknown by making hypotheses and then testing them. It
     can be summarized by the following steps:

        1. Question
        2. Hypothesis

        3. Prediction

        4. Test

        5. Analysis

     The question is the performance problem statement. From this you can hypothesize what the
     cause of poor performance may be. Then you construct a test, which may be observational or
     experimental, that tests a prediction based on the hypothesis. You finish with analysis of the test
     data collected.

     For example, you may find that application performance is degraded after migrating to a system
     with less main memory, and you hypothesize that the cause of poor performance is a smaller
     file system cache. You might use an observational test to measure the cache miss rate on both
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
52   Chapter 2 Methodologies


     Software Resources
     Some software resources can be similarly examined. This usually applies to smaller components
     of software (not entire applications), for example:
         ■   Mutex locks: Utilization may be defined as the time the lock was held, saturation by those
             threads queued waiting on the lock.
         ■   Thread pools: Utilization may be defined as the time threads were busy processing work,
             saturation by the number of requests waiting to be serviced by the thread pool.
         ■   Process/thread capacity: The system may have a limited number of processes or threads,
             whose current usage may be defined as utilization; waiting on allocation may be satura-
             tion; and errors are when the allocation failed (e.g., “cannot fork”).
         ■   File descriptor capacity: Similar to process/thread capacity, but for file descriptors.

     If the metrics work well in your case, use them; otherwise, alternative methodologies such as
     latency analysis can be applied.


     Suggested Interpretations
     Here are some general suggestions for interpreting the metric types:

         ■   Utilization: Utilization at 100% is usually a sign of a bottleneck (check saturation and its
             effect to confirm). Utilization beyond 60% can be a problem for a couple of reasons: depend-
             ing on the interval, it can hide short bursts of 100% utilization. Also, some resources such
             as hard disks (but not CPUs) usually cannot be interrupted during an operation, even for
             higher-priority work. As utilization increases, queueing delays become more frequent and
             noticeable. See Section 2.6.5, Queueing Theory, for more about 60% utilization.
         ■   Saturation: Any degree of saturation (non-zero) can be a problem. It may be measured as
             the length of a wait queue, or as time spent waiting on the queue.
         ■   Errors: Non-zero error counters are worth investigating, especially if they are increasing
             while performance is poor.

     It’s easy to interpret the negative cases: low utilization, no saturation, no errors. This is more use-
     ful than it sounds—narrowing down the scope of an investigation can help you focus quickly on
     the problem area, having identified that it is likely not a resource problem. This is the process of
     elimination.


     Resource Controls
     In cloud computing and container environments, software resource controls may be in place to
     limit or throttle tenants who are sharing one system. These may limit memory, CPU, disk I/O,
     and network I/O. For example, Linux containers use cgroups to limit resource usage. Each of
     these resource limits can be examined with the USE method, similarly to examining the physi-
     cal resources.

     For example, “memory capacity utilization” can be the tenant’s memory usage versus its mem-
     ory cap. “Memory capacity saturation” can be seen by limit-imposed allocation errors or swapping
     for that tenant, even if the host system is not experiencing memory pressure. These limits are
     discussed in Chapter 11, Cloud Computing.
                                                                               2.5 Methodology        53



Microservices
A microservice architecture presents a similar problem to that of too many resource metrics:
there can be so many metrics for each service that it is laborious to check them all, and they can
overlook areas where metrics do not yet exist. The USE method can address these problems with
microservices as well. For example, for a typical Netflix microservice, the USE metrics are:
   ■   Utilization: The average CPU utilization across the entire instance cluster.
   ■   Saturation: An approximation is the difference between the 99th latency percentile and
       the average latency (assumes the 99th is saturation-driven).
   ■   Errors: Request errors.

These three metrics are already examined for each microservice at Netflix using the Atlas cloud-
wide monitoring tool [Harrington 14].

There is a similar methodology that has been designed specifically for services: the RED method.


2.5.10      The RED Method
The focus of this methodology is services, typically cloud services in a microservice architecture.
It identifies three metrics for monitoring health from a user perspective and can be summarized
as [Wilkie 18]:

    For every service, check the request rate, errors, and duration.

The metrics are:
   ■   Request rate: The number of service requests per second
   ■   Errors: The number of requests that failed
   ■   Duration: The time for requests to complete (consider distribution statistics such as per-
       centiles in addition to the average: see Section 2.8, Statistics)

Your task is to draw a diagram of your microservice architecture and ensure that these three
metrics are monitored for each service. (Distributed tracing tools may provide such diagrams for
you.) The advantages are similar to the USE method: the RED method is fast and easy to follow,
and comprehensive.

The RED method was created by Tom Wilkie, who has also developed implementations of the
USE and RED method metrics for Prometheus with dashboards using Grafana [Wilkie 18]. These
methodologies are complementary: the USE method for machine health, and the RED method
for user health.

The inclusion of the request rate provides an important early clue in an investigation: whether a
performance problem is one of load versus architecture (see Section 2.3.8, Load vs. Architecture).
If the request rate has been steady but the request duration has increased, it points to a problem
with the architecture: the service itself. If both the request rate and duration have increased,
then the problem may be one of the load applied. This can be further investigated using work-
load characterization.
