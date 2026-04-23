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
82   Chapter 2 Methodologies


     Many of the I/O were submillisecond, shown close to the x-axis. This is where the resolution of
     scatter plots begins to become a problem, as the points overlap and become difficult to distin-
     guish. This gets worse with more data: imagine plotting events from an entire cloud, involving
     millions of data points, on one scatter plot: the dots can merge and become a “wall of paint.”
     Another problem is the volume of data that must be collected and processed: x and y coordinates
     for every I/O.


     2.10.3      Heat Maps
     Heat maps (more properly called a column quantization) can solve the scatter plot scalability prob-
     lems by quantizing x and y ranges into groups called buckets. These are displayed as large pixels,
     colored based on the number of events in that x and y range. This quantizing also solves the
     scatter plot visual density limit, allowing heat maps to show data from a single system or thou-
     sands of systems in the same way. Heat maps had previously been used for location such as disk
     offsets (e.g., TazTool [McDougall 06a]); I invented their use in computing for latency, utilization,
     and other metrics. Latency heat maps were first included in Analytics for the Sun Microsystems
     ZFS Storage appliance, released in 2008 [Gregg 10a][Gregg 10b], and are now commonplace in
     performance monitoring products such as Grafana [Grafana 20].

     The same dataset as plotted earlier is shown in Figure 2.30 as a heat map.




     Figure 2.30 Heat map

     High-latency outliers can be identified as blocks that are high in the heat map, usually of light
     colors as they span few I/O (often a single I/O). Patterns in the bulk of the data begin to emerge,
     which may be impossible to see with a scatter plot.

     The full range of seconds for this disk I/O trace (not shown earlier) is shown in the Figure 2.31
     heat map.
                                                                               2.10 Visualizations     83




Figure 2.31 Heat map: full range

Despite spanning nine times the range, the visualization is still very readable. A bimodal distri-
bution can be seen for much of the range, with some I/O returning with near-zero latency (likely
a disk cache hit), and others with a little less than 1 ms (likely a disk cache miss).

There are other examples of heat maps later in this book, including in Chapter 6, CPUs, Section 6.7,
Visualizations; Chapter 8, File Systems, Section 8.6.18, Visualizations; and Chapter 9, Disks,
Section 9.7.3, Latency Heat Maps. My website also has examples of latency, utilization, and
subsecond-offset heat maps [Gregg 15b].


2.10.4      Timeline Charts
A timeline chart shows a set of activities as bars on a timeline. These are commonly used for
front-end performance analysis (web browsers), where they are also called waterfall charts, and
show the timing of network requests. An example from the Firefox web browser is shown in
Figure 2.32.

In Figure 2.32, the first network request is highlighted: apart from showing its duration as a hor-
izontal bar, components of this duration are also shown as colored bars. These are also explained
in the right panel: the slowest component for the first request is “Waiting,” which is waiting
for the HTTP response from the server. Requests two to six begin after the first request begins
receiving data, and are likely dependent on that data. If explicit dependency arrows are included
in the chart, it becomes a type of Gantt chart.

For back-end performance analysis (servers), similar charts are used to show timelines for
threads or CPUs. Example software includes KernelShark [KernelShark 20] and Trace Compass
[Eclipse 20]. For an example KernelShark screenshot, see Chapter 14, Ftrace, Section 14.11.5,
KernelShark. Trace Compass also draws arrows showing dependencies, where one thread has
woken up another.
84   Chapter 2 Methodologies




     Figure 2.32 Firefox timeline chart

     2.10.5      Surface Plot
     This is a representation of three dimensions, rendered as a three-dimensional surface. It works
     best when the third-dimension value does not frequently change dramatically from one point
     to the next, producing a surface resembling rolling hills. A surface plot is often rendered as a
     wireframe model.

     Figure 2.33 shows a wireframe surface plot of per-CPU utilization. It contains 60 seconds of
     per-second values from many servers (this is cropped from an image that spanned a data center
     of over 300 physical servers and 5,312 CPUs) [Gregg 11b].

     Each server is represented by plotting its 16 CPUs as rows on the surface, the 60 per-second uti-
     lization measurements as columns, and then setting the height of the surface to the utilization
     value. Color is also set to reflect the utilization value. Both hue and saturation could be used, if
     desired, to add fourth and fifth dimensions of data to the visualization. (With sufficient resolu-
     tion, a pattern could be used to indicate a sixth dimension.)

     These 16 × 60 server rectangles are then mapped across the surface as a checkerboard. Even
     without markings, some server rectangles can be clearly seen in the image. One that appears as
     an elevated plateau on the right shows that its CPUs are almost always at 100%.

     The use of grid lines highlights subtle changes in elevation. Some faint lines are visible, which
     indicate a single CPU constantly running at low utilization (a few percent).
                                                                                2.11   Exercises   85




Figure 2.33 Wireframe surface plot: data center CPU utilization

2.10.6       Visualization Tools
Unix performance analysis has historically focused on the use of text-based tools, due in part
to limited graphical support. Such tools can be executed quickly over a login session and report
data in real time. Visualizations have been more time-consuming to access and often require a
trace-and-report cycle. When working urgent performance issues, the speed at which you can
access metrics can be critical.

Modern visualization tools provide real-time views of system performance, accessible from the
browser and mobile devices. There are numerous products that do this, including many that
can monitor your entire cloud. Chapter 1, Introduction, Section 1.7.1, Counters, Statistics, and
Metrics, includes an example screenshot from one such product, Grafana, and other monitoring
products are discussed in Chapter 4, Observability Tools, Section 4.2.4, Monitoring.



2.11         Exercises
1. Answer the following questions about key performance terminology:
   ■   What are IOPS?
   ■   What is utilization?
   ■   What is saturation?
   ■   What is latency?
   ■   What is micro-benchmarking?
86   Chapter 2 Methodologies


     2. Choose five methodologies to use for your (or a hypothetical) environment. Select the order
        in which they can be conducted, and explain the reason for choosing each.

     3. Summarize problems when using average latency as a sole performance metric. Can these
        problems be solved by including the 99th percentile?



     2.12        References
        [Amdahl 67] Amdahl, G., “Validity of the Single Processor Approach to Achieving Large
        Scale Computing Capabilities,” AFIPS, 1967.

        [Jain 91] Jain, R., The Art of Computer Systems Performance Analysis: Techniques for Experimental
        Design, Measurement, Simulation and Modeling, Wiley, 1991.

        [Cockcroft 95] Cockcroft, A., Sun Performance and Tuning, Prentice Hall, 1995.

        [Gunther 97] Gunther, N., The Practical Performance Analyst, McGraw-Hill, 1997.

        [Wong 97] Wong, B., Configuration and Capacity Planning for Solaris Servers, Prentice Hall, 1997.

        [Elling 00] Elling, R., “Static Performance Tuning,” Sun Blueprints, 2000.

        [Millsap 03] Millsap, C., and J. Holt., Optimizing Oracle Performance, O’Reilly, 2003.

        [McDougall 06a] McDougall, R., Mauro, J., and Gregg, B., Solaris Performance and Tools:
        DTrace and MDB Techniques for Solaris 10 and OpenSolaris, Prentice Hall, 2006.

        [Gunther 07] Gunther, N., Guerrilla Capacity Planning, Springer, 2007.

        [Allspaw 08] Allspaw, J., The Art of Capacity Planning, O’Reilly, 2008.

        [Gregg 10a] Gregg, B., “Visualizing System Latency,” Communications of the ACM, July 2010.

        [Gregg 10b] Gregg, B., “Visualizations for Performance Analysis (and More),” USENIX LISA,
        https://www.usenix.org/legacy/events/lisa10/tech/#gregg, 2010.

        [Gregg 11b] Gregg, B., “Utilization Heat Maps,” http://www.brendangregg.com/HeatMaps/
        utilization.html, published 2011.
        [Williams 11] Williams, C., “The $300m Cable That Will Save Traders Milliseconds,” The
        Telegraph, https://www.telegraph.co.uk/technology/news/8753784/The-300m-cable-that-will-
        save-traders-milliseconds.html, 2011.

        [Gregg 13b] Gregg, B., “Thinking Methodically about Performance,” Communications of the
        ACM, February 2013.

        [Gregg 14a] Gregg, B., “Performance Scalability Models,” https://github.com/brendangregg/
        PerfModels, 2014.

        [Harrington 14] Harrington, B., and Rapoport, R., “Introducing Atlas: Netflix’s Primary
        Telemetry Platform,” Netflix Technology Blog, https://medium.com/netflix-techblog/
        introducing-atlas-netflixs-primary-telemetry-platform-bd31f4d8ed9a, 2014.

        [Gregg 15b] Gregg, B., “Heatmaps,” http://www.brendangregg.com/heatmaps.html, 2015.
                                                                             2.12   References    87


[Wilkie 18] Wilkie, T., “The RED Method: Patterns for Instrumentation & Monitoring,”
Grafana Labs, https://www.slideshare.net/grafana/the-red-method-how-to-monitoring-your-
microservices, 2018.

[Eclipse 20] Eclipse Foundation, “Trace Compass,” https://www.eclipse.org/tracecompass,
accessed 2020.

[Wikipedia 20] Wikipedia, “Five Whys,” https://en.wikipedia.org/wiki/Five_whys, accessed
2020.

[Grafana 20] Grafana Labs, “Heatmap,” https://grafana.com/docs/grafana/latest/features/
panels/heatmap, accessed 2020.

[KernelShark 20] “KernelShark,” https://www.kernelshark.org, accessed 2020.

[Kubernetes 20a] Kubernetes, “Horizontal Pod Autoscaler,” https://kubernetes.io/docs/tasks/
run-application/horizontal-pod-autoscale, accessed 2020.

[R Project 20] R Project, “The R Project for Statistical Computing,” https://www.r-project.org,
accessed 2020.
