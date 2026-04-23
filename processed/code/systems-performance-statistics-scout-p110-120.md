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
76   Chapter 2 Methodologies


     2.8.4 Coefficient of Variation
     Since standard deviation is relative to the mean, variance can be understood only when consid-
     ering both standard deviation and mean. A standard deviation of 50 alone tells us little. That
     plus a mean of 200 tells us a lot.

     There is a way to express variation as a single metric: the ratio of the standard deviation to the
     mean, which is called the coefficient of variation (CoV or CV). For this example, the CV is 25%.
     Lower CVs mean less variance.

     Another expression of variance as a single metric is the z value, which is how many standard
     deviations a value is from the mean.


     2.8.5 Multimodal Distributions
     There is a problem with means, standard deviations, and percentiles, which may be obvious
     from the previous chart: they are intended for normal-like or unimodal distributions. System
     performance is often bimodal, returning low latencies for a fast code path and high latencies for
     a slow one, or low latencies for cache hits and high latencies for cache misses. There may also be
     more than two modes.

     Figure 2.23 shows the distribution of disk I/O latency for a mixed workload of reads and writes,
     which includes random and sequential I/O.




     Figure 2.23 Latency distribution

     This is presented as a histogram, which shows two modes. The mode on the left shows laten-
     cies of less than 1 ms, which is for on-disk cache hits. The right, with a peak around 7 ms, is for
                                                                                      2.9    Monitoring     77


on-disk cache misses: random reads. The average (mean) I/O latency is 3.3 ms, which is plotted
as a vertical line. This average is not the index of central tendency (as described earlier); in fact, it
is almost the opposite. As a metric, the average for this distribution is seriously misleading.

     Then there was the man who drowned crossing a stream with an average depth of
     six inches. —W. I. E. Gates

Every time you see an average used as a performance metric, especially an average latency, ask:
What is the distribution? Section 2.10, Visualizations, provides another example and shows how
effective different visualizations and metrics are at showing this distribution.


2.8.6      Outliers
Another statistical problem is the presence of outliers: a very small number of extremely high or
low values that don’t appear to fit the expected distribution (single- or multimode).

Disk I/O latency outliers are an example—very occasional disk I/O that can take over 1,000 ms,
when the majority of disk I/O is between 0 and 10 ms. Latency outliers like these can cause
serious performance problems, but their presence can be difficult to identify from most metric
types, other than as a maximum. Another example is network I/O latency outliers caused by
TCP timer-based retransmits.

For a normal distribution, the presence of outliers is likely to shift the mean by a little, but not
the median (which may be useful to consider). The standard deviation and 99th percentile have
a better chance of identifying outliers, but this is still dependent on their frequency.

To better understand multimodal distributions, outliers, and other complex yet common
behaviors, inspect the full distribution, for example by using a histogram. See Section 2.10,
Visualizations, for more ways to do this.



2.9       Monitoring
System performance monitoring records performance statistics over time (a time series) so that
the past can be compared to the present and time-based usage patterns can be identified. This is
useful for capacity planning, quantifying growth, and showing peak usage. Historic values can
also provide context for understanding the current value of performance metrics, by showing
what the “normal” range and average have been in the past.


2.9.1     Time-Based Patterns
Examples of time-based patterns are shown in Figures 2.24, 2.25, and 2.26, which plot file sys-
tem reads from a cloud computing server over different time intervals.
78   Chapter 2 Methodologies




     Figure 2.24 Monitoring activity: one day




     Figure 2.25 Monitoring activity: five days




     Figure 2.26 Monitoring activity: 30 days

     These graphs show a daily pattern that begins to ramp up around 8 a.m., dips a little in the after-
     noon, and then decays during the night. The longer-scale charts show that activity is lower on
     the weekend days. A couple of short spikes are also visible in the 30-day chart.

     Various cycles of behavior including those shown in the figures can commonly be seen in his-
     toric data, including:

         ■   Hourly: Activity may occur every hour from the application environment, such as
             monitoring and reporting tasks. It’s also common for these to execute with a 5- or 10-
             minute cycle.
         ■   Daily: There may be a daily pattern of usage that coincides with work hours (9 a.m. to
             5 p.m.), which may be stretched if the server is for multiple time zones. For Internet
             servers, the pattern may follow when worldwide users are active. Other daily activity
             may include nightly log rotation and backups.
                                                                                            2.10 Visualizations      79


    ■   Weekly: As well as a daily pattern, there may be a weekly pattern present based on work-
        days and weekends.
    ■   Quarterly: Financial reports are done on a quarterly schedule.
    ■   Yearly: Yearly patterns of load may be due to school schedules and vacations.

Irregular increases in load may occur with other activities, such as releasing new content on a
website, and sales (Black Friday/Cyber Monday in the US). Irregular decreases in load can occur
due to external activities, such as widespread power or internet outages, and sports finals (where
everyone watches the game instead of using your product).6


2.9.2       Monitoring Products
There are many third-party products for system performance monitoring. Typical features
include archiving data and presenting it as browser-based interactive graphs, and providing
configurable alerts.

Some of these operate by running agents (also known as exporters) on the system to gather their sta-
tistics. These agents either execute operating system observability tools (such as iostat(1) or sar(1))
and parse the text of the output (which is considered inefficient) or read directly from operating
system libraries and kernel interfaces. Monitoring products support a collection of custom agents
for exporting statistics from specific targets: web servers, databases, and language runtimes.

As systems become more distributed and the usage of cloud computing continues to grow, you
will more often need to monitor numerous systems: hundreds, thousands, or more. This is
where a centralized monitoring product can be especially useful, allowing an entire environ-
ment to be monitored from one interface.

As a specific example: the Netflix cloud is composed of over 200,000 instances and is monitored
using the Atlas cloud-wide monitoring tool, which was custom built by Netflix to operate at this
scale and is open source [Harrington 14]. Other monitoring products are discussed in Chapter 4,
Observability Tools, Section 4.2.4, Monitoring.


2.9.3 Summary-Since-Boot
If monitoring has not been performed, check whether at least summary-since-boot values are
available from the operating system, which can be used to compare with the current values.



2.10 Visualizations
Visualizations allow more data to be examined than can be easily understood (or sometimes
even displayed) as text. They also enable pattern recognition and pattern matching. This can be
an effective way to identify correlations between different metric sources, which may be diffi-
cult to accomplish programmatically, but easy to do visually.


6
 When I was on the Netflix SRE on-call rotation, I learned some non-traditional analysis tools for these cases: to
check social media for suspected power outages and to ask in team chatrooms if anyone knew of a sports final.
80   Chapter 2 Methodologies


     2.10.1      Line Chart
     A line chart (also called line graph) is a well-known, basic visualization. It is commonly used for
     examining performance metrics over time, showing the passage of time on the x-axis.

     Figure 2.27 is an example, showing the average (mean) disk I/O latency for a 20-second period.
     This was measured on a production cloud server running a MySQL database, where disk I/O
     latency was suspected to be causing slow queries.




     Figure 2.27 Line chart of average latency

     This line chart shows fairly consistent average read latency of around 4 ms, which is higher than
     expected for these disks.

     Multiple lines can be plotted, showing related data on the same set of axes. With this example, a
     separate line may be plotted for each disk, showing whether they exhibit similar performance.

     Statistical values can also be plotted, providing more information on the distribution of data.
     Figure 2.28 shows the same range of disk I/O events, with lines added for the per-second median,
     standard deviation, and percentiles. Note that the y-axis now has a much greater range than the
     previous line chart (by a factor of 8).

     This shows why the average is higher than expected: the distribution includes higher-latency
     I/O. Specifically, 1% of the I/O is over 20 ms, as shown by the 99th percentile. The median also
     shows where I/O latency was expected, around 1 ms.
                                                                             2.10 Visualizations      81




Figure 2.28 Median, mean, standard deviation, percentiles

2.10.2      Scatter Plots
Figure 2.29 shows disk I/O events for the same time range as a scatter plot, which enables all data
to be seen. Each disk I/O is drawn as a point, with its completion time on the x-axis and latency
on the y-axis.




Figure 2.29 Scatter plot

Now the source of the higher-than-expected average latency can be understood fully: there are
many disk I/O with latencies of 10 ms, 20 ms, even over 50 ms. The scatter plot has shown all the
data, revealing the presence of these outliers.
