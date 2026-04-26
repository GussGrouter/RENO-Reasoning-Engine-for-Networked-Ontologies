                                                                                    2.6   Modeling     65


The relative capacity is C(N), and N is the scaling dimension, such as the CPU count or user load.
The α parameter (where 0 <= α <= 1) represents the degree of seriality and is how this deviates
from linear scalability.

Amdahl’s Law of Scalability can be applied by taking the following steps:

   1. Collect data for a range of N, either by observation of an existing system or experimentally
      using micro-benchmarking or load generators.

   2. Perform regression analysis to determine the Amdahl parameter (α); this may be done
      using statistical software, such as gnuplot or R.

   3. Present the results for analysis. The collected data points can be plotted along with the
      model function to predict scaling and reveal differences between the data and the model.
      This may also be done using gnuplot or R.

The following is example gnuplot code for Amdahl’s Law of Scalability regression analysis, to
provide a sense of how this step can be performed:

inputN = 10                          # rows to include as model input
alpha = 0.1                          # starting point (seed)
amdahl(N) = N1 * N/(1 + alpha * (N - 1))
# regression analysis (non-linear least squares fitting)
fit amdahl(x) filename every ::1::inputN using 1:2 via alpha

A similar amount of code is required to process this in R, involving the nls() function for non-
linear least squares fitting to calculate the coefficients, which are then used during plotting. See
the Performance Scalability Models toolkit in the references at the end of this chapter for the full
code in both gnuplot and R [Gregg 14a].

An example Amdahl’s Law of Scalability function is shown in the next section.


2.6.4 Universal Scalability Law
The Universal Scalability Law (USL), previously called the super-serial model [Gunther 97], was
developed by Dr. Neil Gunther to include a parameter for coherency delay. This was pictured
earlier as the coherence scalability profile, which includes the effects of contention.

USL can be defined as:

    C(N) = N/(1 + α(N – 1) + βN(N – 1))

C(N), N, and α are as with Amdahl’s Law of Scalability. β is the coherence parameter. When
β == 0, this becomes Amdahl’s Law of Scalability.

Examples of both USL and Amdahl’s Law of Scalability analysis are graphed in Figure 2.17.
66   Chapter 2 Methodologies




     Figure 2.17 Scalability models

     The input dataset has a high degree of variance, making it difficult to visually determine the
     scalability profile. The first ten data points, drawn as circles, were provided to the models. An
     additional ten data points are also plotted, drawn as crosses, which check the model prediction
     against reality.

     For more on USL analysis, see [Gunther 97] and [Gunther 07].


     2.6.5     Queueing Theory
     Queueing theory is the mathematical study of systems with queues, providing ways to analyze
     their queue length, wait time (latency), and utilization (time-based). Many components in
     computing, both software and hardware, can be modeled as queueing systems. The modeling of
     multiple queueing systems is called queueing networks.

     This section summarizes the role of queueing theory and provides an example to help you under-
     stand that role. It is a large field of study, covered in detail in other texts [Jain 91][Gunther 97].

     Queueing theory builds upon various areas of mathematics and statistics, including probability
     distributions, stochastic processes, Erlang’s C formula (Agner Krarup Erlang invented queueing
     theory), and Little’s Law. Little’s Law can be expressed as

          L = λW

     which determines the average number of requests in a system, L, as the average arrival rate, λ,
     multiplied by the average request time in the system, W. This can be applied to a queue, such
     that L is the number of requests in the queue, and W is the average wait time on the queue.
                                                                                     2.6   Modeling    67


Queueing systems can be used to answer a variety of questions, including the following:

    ■   What will the mean response time be if the load doubles?
    ■   What will be the effect on mean response time after adding an additional processor?
    ■   Can the system provide a 90th percentile response time of under 100 ms when the load
        doubles?

Apart from response time, other factors, including utilization, queue lengths, and number of
resident jobs, can be studied.

A simple queueing system model is shown in Figure 2.18.




Figure 2.18 Queueing model

This has a single service center that processes jobs from the queue. Queueing systems can have
multiple service centers that process work in parallel. In queueing theory, the service centers are
often called servers.

Queueing systems can be categorized by three factors:

    ■   Arrival process: This describes the inter-arrival time for requests to the queueing system,
        which may be random, fixed-time, or a process such as Poisson (which uses an exponen-
        tial distribution for arrival time).
    ■   Service time distribution: This describes the service times for the service center. They
        may be fixed (deterministic), exponential, or of another distribution type.
    ■   Number of service centers: One or many.

These factors can be written in Kendall’s notation.


Kendall’s Notation
This notation assigns codes for each attribute. It has the form

    A/S/m

These are the arrival process (A), service time distribution (S), and number of service centers (m).
There is also an extended form of Kendall’s notation that includes more factors: number of buf-
fers in the system, population size, and service discipline.
68   Chapter 2 Methodologies


     Examples of commonly studied queueing systems are

         ■   M/M/1: Markovian arrivals (exponentially distributed arrival times), Markovian service
             times (exponential distribution), one service center
         ■   M/M/c: same as M/M/1, but multiserver
         ■   M/G/1: Markovian arrivals, general distribution of service times (any), one service center
         ■   M/D/1: Markovian arrivals, deterministic service times (fixed), one service center

     M/G/1 is commonly applied to study the performance of rotational hard disks.


     M/D/1 and 60% Utilization
     As a simple example of queueing theory, consider a disk that responds to a workload determinis-
     tically (this is a simplification). The model is M/D/1.

     The question posed is: How does the disk’s response time vary as its utilization increases?

     Queueing theory allows the response time for M/D/1 to be calculated:

         r = s(2 - ρ)/2(1 - ρ)

     where the response time, r, is defined in terms of the service time, s, and the utilization, ρ.

     For a service time of 1 ms, and utilizations from 0 to 100%, this relationship has been graphed in
     Figure 2.19.




     Figure 2.19 M/D/1 mean response time versus utilization
                                                                          2.7   Capacity Planning    69


Beyond 60% utilization, the average response time doubles. By 80%, it has tripled. As disk I/O
latency is often the bounding resource for an application, increasing the average latency by dou-
ble or higher can have a significant negative effect on application performance. This is why disk
utilization can become a problem well before it reaches 100%, as it is a queueing system where
requests (typically) cannot be interrupted and must wait their turn. This is different from CPUs,
for example, where higher-priority work can preempt.

This graph can visually answer an earlier question—what will the mean response time be if the
load doubles?—when utilization is relative to load.

This model is simple, and in some ways it shows the best case. Variations in service time can
drive the mean response time higher (e.g., using M/G/1 or M/M/1). There is also a distribution
of response times, not pictured in Figure 2.19, such that the 90th and 99th percentiles degrade
much faster beyond 60% utilization.

As with the earlier gnuplot example for Amdahl’s Law of Scalability, it may be illustrative to
show some actual code, for a sense of what may be involved. This time the R statistics software
was used [R Project 20]:

svc_ms <- 1                       # average disk I/O service time, ms
util_min <- 0                     # range to plot
util_max <- 100                   # "
ms_min <- 0                       # "
ms_max <- 10                      # "
# Plot mean response time vs utilization (M/D/1)
plot(x <- c(util_min:util_max), svc_ms * (2 - x/100) / (2 * (1 - x/100)),
    type="l", lty=1, lwd=1,
    xlim=c(util_min, util_max), ylim=c(ms_min, ms_max),
    xlab="Utilization %", ylab="Mean Response Time (ms)")

The earlier M/D/1 equation has been passed to the plot() function. Much of this code specifies
limits to the graph, line properties, and axis labels.



2.7      Capacity Planning
Capacity planning examines how well the system will handle load and how it will scale as load
scales. It can be performed in a number of ways, including studying resource limits and factor
analysis, which are described here, and modeling, as introduced previously. This section also
includes solutions for scaling, including load balancers and sharding. For more on this topic, see
The Art of Capacity Planning [Allspaw 08].

For capacity planning of a particular application, it helps to have a quantified performance
objective to plan for. Determining this is discussed early on in Chapter 5, Applications.
70   Chapter 2 Methodologies


     2.7.1      Resource Limits
     This method is a search for the resource that will become the bottleneck under load. For con-
     tainers, a resource may encounter a software-imposed limit that becomes the bottleneck. The
     steps for this method are:

        1. Measure the rate of server requests, and monitor this rate over time.

       2. Measure hardware and software resource usage. Monitor this rate over time.

        3. Express server requests in terms of resources used.

        4. Extrapolate server requests to known (or experimentally determined) limits for each
           resource.

     Begin by identifying the role of the server and the type of requests it serves. For example, a web
     server serves HTTP requests, a Network File System (NFS) server serves NFS protocol requests
     (operations), and a database server serves query requests (or command requests, for which que-
     ries are a subset).

     The next step is to determine the system resource consumption per request. For an existing sys-
     tem, the current rate of requests along with resource utilization can be measured. Extrapolation
     can then be used to see which resource will hit 100% utilization first, and what the rate of
     requests will be.

     For a future system, micro-benchmarking or load generation tools can be used to simulate the
     intended requests in a test environment, while measuring resource utilization. Given sufficient
     client load, you may be able to find the limit experimentally.

     The resources to monitor include:

         ■   Hardware: CPU utilization, memory usage, disk IOPS, disk throughput, disk capacity
             (volume used), network throughput
         ■   Software: Virtual memory usage, processes/tasks/threads, file descriptors

     Let’s say you’re looking at an existing system currently performing 1,000 requests/s. The
     busiest resources are the 16 CPUs, which are averaging 40% utilization; you predict that they
     will become the bottleneck for this workload once they become 100% utilized. The question
     becomes: What will the requests-per-second rate be at that point?

         CPU% per request = total CPU%/requests = 16 × 40%/1,000 = 0.64% CPU per request

         max requests/s = 100% × 16 CPUs/CPU% per request = 1,600 / 0.64 = 2,500 requests/s

     The prediction is 2,500 requests/s, at which point the CPUs will be 100% busy. This is a rough
     best-case estimate of capacity, as some other limiting factor may be encountered before the
     requests reach that rate.

     This exercise used only one data point: application throughput (requests per second) of 1,000
     versus device utilization of 40%. If monitoring over time is enabled, multiple data points at
     different throughput and utilization rates can be included, to improve the accuracy of the
                                                                         2.7   Capacity Planning   71


estimation. Figure 2.20 illustrates a visual method for processing these and extrapolating the
maximum application throughput.




Figure 2.20 Resource limit analysis

Is 2,500 requests/s enough? Answering this question requires understanding what the peak
workload will be, which shows up in daily access patterns. For an existing system that you have
monitored over time, you may already have an idea of what the peak will look like.

Consider a web server that is processing 100,000 website hits per day. This may sound like many,
but as an average is only one request/s—not much. However, it may be that most of the 100,000
website hits occur in the seconds after new content is posted, so the peak is significant.


2.7.2    Factor Analysis
When purchasing and deploying new systems, there are often many factors that can be changed
to achieve the desired performance. These may include varying the number of disks and CPUs,
the amount of RAM, the use of flash devices, RAID configurations, file system settings, and so
forth. The task is usually to achieve the performance required for the minimum cost.

Testing all combinations would determine which has the best price/performance ratio; however,
this can quickly get out of hand: eight binary factors would require 256 tests.

A solution is to test a limited set of combinations. Here is an approach based on knowing the
maximum system configuration:

   1. Test performance with all factors configured to maximum.

  2. Change factors one by one, testing performance (it should drop for each).

   3. Attribute a percentage performance drop to each factor, based on measurements, along
      with the cost savings.

   4. Starting with maximum performance (and cost), choose factors to save cost, while main-
      taining the required requests per second based on their combined performance drop.

   5. Retest the calculated configuration for confirmation of delivered performance.

For an eight-factor system, this approach may require only ten tests.
72   Chapter 2 Methodologies


     As an example, consider capacity planning for a new storage system, with a requirement of
     1 Gbyte/s read throughput and a 200 Gbyte working set size. The maximum configuration
     achieves 2 Gbytes/s and includes four processors, 256 Gbytes of DRAM, 2 dual-port 10 GbE
     network cards, jumbo frames, and no compression or encryption enabled (which is costly to
     activate). Switching to two processors reduces performance by 30%, one network card by 25%,
     non-jumbo by 35%, encryption by 10%, compression by 40%, and less DRAM by 90% as the
     workload is no longer expected to fully cache. Given these performance drops and their known
     savings, the best price/performance system that meets the requirements can now be calculated;
     it might be a two-processor system with one network card, which meets the throughput needed:
     2 × (1 – 0.30) × (1 – 0.25) = 1.04 Gbytes/s estimated. It would then be wise to test this configura-
     tion, in case these components perform differently from their expected performance when used
     together.


     2.7.3     Scaling Solutions
     Meeting higher performance demands has often meant larger systems, a strategy called vertical
     scaling. Spreading load across numerous systems, usually fronted by systems called load balancers
     that make them all appear as one, is called horizontal scaling.

     Cloud computing takes horizontal scaling further, by building upon smaller virtualized systems
     rather than entire systems. This provides finer granularity when purchasing compute to process
     the required load and allows scaling in small, efficient increments. Since no initial large pur-
     chase is required, as with enterprise mainframes (including a support contract commitment),
     there is less need for rigorous capacity planning in the early stages of a project.

     There are technologies to automate cloud scaling based on a performance metric. The AWS tech-
     nology for this is called an auto scaling group (ASG). A custom scaling policy can be created
     to increase and decrease the number of instances based on a usage metric. This is pictured in
     Figure 2.21.




     Figure 2.21 Auto scaling group

     Netflix commonly uses ASGs that target a CPU utilization of 60%, and will scale up and down
     with the load to maintain that target.
                                                                                     2.8 Statistics     73


Container orchestration systems may also provide support for automatic scaling. For example,
Kubernetes provides horizontal pod autoscalers (HPAs) that can scale the number of Pods (con-
tainers) based on CPU utilization or another custom metric [Kubernetes 20a].

For databases, a common scaling strategy is sharding, where data is split into logical components,
each managed by its own database (or redundant group of databases). For example, a customer
database may be split into parts by splitting the customer names into alphabetical ranges.
Picking an effective sharding key is crucial to evenly spread the load across the databases.



2.8        Statistics
It’s important to have a good understanding of how to use statistics and what their limitations are.
This section discusses quantifying performance issues using statistics (metrics) and statistical
types including averages, standard deviations, and percentiles.


2.8.1 Quantifying Performance Gains
Quantifying issues and the potential performance improvement for fixing them allows them to
be compared and prioritized. This task may be performed using observation or experiments.


Observation-Based
To quantify performance issues using observation:

   1. Choose a reliable metric.

   2. Estimate the performance gain from resolving the issue.

For example:

    ■   Observed: Application request takes 10 ms.
    ■   Observed: Of that, 9 ms is disk I/O.
    ■   Suggestion: Configure the application to cache I/O in memory, with expected DRAM
        latency around ~10 μs.
    ■   Estimated gain: 10 ms → 1.01 ms (10 ms - 9 ms + 10 μs) = ~9x gain.

As introduced in Section 2.3, Concepts, latency (time) is well suited for this, as it can be directly
compared between components, which makes calculations like this possible.

When using latency, ensure that it is measured as a synchronous component of the application
request. Some events occur asynchronously, such as background disk I/O (write flush to disk),
and do not directly affect application performance.


Experimentation-Based
To quantify performance issues experimentally:

   1. Apply the fix.

   2. Quantify before versus after using a reliable metric.
74   Chapter 2 Methodologies


     For example:

         ■   Observed: Application transaction latency averages 10 ms.
         ■   Experiment: Increase the application thread count to allow more concurrency instead of
             queueing.
         ■   Observed: Application transaction latency averages 2 ms.
         ■   Gain: 10 ms → 2 ms = 5x.

     This approach may not be appropriate if the fix is expensive to attempt in the production
     environment! For that case, observation-based should be used.


     2.8.2 Averages
     An average represents a dataset by a single value: an index of central tendency. The most
     common type of average used is an arithmetic mean (or mean for short), which is a sum of values
     divided by the count of values. Other types include the geometric mean and harmonic mean.


     Geometric Mean
     The geometric mean is the nth root (where n is the count of values) of multiplied values. This is
     described in [Jain 91], which includes an example of using it for network performance analysis:
     if the performance improvement of each layer of the kernel network stack is measured individu-
     ally, what is the average performance improvement? Since the layers work together on the same
     packet, performance improvements have a “multiplicative” effect, which can be best summa-
     rized by the geometric mean.


     Harmonic Mean
     The harmonic mean is the count of values divided by the sum of their reciprocals. It is more
     appropriate for taking the average of rates, for example, calculating the average transfer rate for
     800 Mbytes of data, when the first 100 Mbytes will be sent at 50 Mbytes/s and the remaining
     700 Mbytes at a throttled rate of 10 Mbytes/s. The answer, using the harmonic mean, is
     800/(100/50 + 700/10) = 11.1 Mbytes/s.


     Averages over Time
     With performance, many metrics we study are averages over time. A CPU is never “at 50%
     utilization”; it has been utilized during 50% of some interval, which could be a second, minute,
     or hour. It is important to check for intervals whenever considering averages.

     For example, I had an issue where a customer had performance problems caused by CPU satura-
     tion (scheduler latency) even though their monitoring tools showed CPU utilization was never
     higher than 80%. The monitoring tool was reporting 5-minute averages, which masked periods in
     which CPU utilization hit 100% for seconds at a time.
                                                                                  2.8 Statistics     75



Decayed Average
A decayed average is sometimes used in systems performance. An example is the system “load
averages” reported by various tools including uptime(1).

A decayed average is still measured over a time interval, but recent time is weighted more heavily
than time further past. This reduces (dampens) short-term fluctuations in the average.

See Load Averages in Chapter 6, CPUs, Section 6.6, Observability Tools, for more on this.


Limitations
Averages are a summary statistic that hides details. I’ve analyzed many cases of occasional
disk I/O latency outliers exceeding 100 ms, while the average latency was close to 1 ms. To
better understand the data, you can use additional statistics covered in Section 2.8.3, Standard
Deviation, Percentiles, Median (the next section), and visualizations covered in Section 2.10,
Visualizations.


2.8.3     Standard Deviation, Percentiles, Median
Standard deviations and percentiles (e.g., 99th percentile) are statistical techniques to provide
information on the distribution of data. The standard deviation is a measure of variance, with
larger values indicating greater variance from the average (mean). The 99th percentile shows the
point in the distribution that includes 99% of the values. Figure 2.22 pictures these for a normal
distribution, along with the minimum and maximum.




Figure 2.22 Statistical values

Percentiles such as 90th, 95th, 99th, and 99.9th are used in performance monitoring of request
latency to quantify the slowest in the population. These may also be specified in service-level
agreements (SLAs) as a way to measure that performance is acceptable for most users.

The 50th percentile, called the median, can be examined to show where the bulk of the data is.
