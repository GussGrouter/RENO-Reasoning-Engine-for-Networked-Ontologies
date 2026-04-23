9.7       Visualizations
There are many types of visualizations that can help in analyzing disk I/O performance. This
section demonstrates these with screenshots from various tools. See Chapter 2, Methodologies,
Section 2.10, Visualization, for a discussion about visualizations in general.


9.7.1      Line Graphs
Performance monitoring solutions commonly graph disk IOPS, throughput, and utilization
measurements over time as line graphs. This helps illustrate time-based patterns, such as
changes in load during the day, or recurring events such as file system flush intervals.

Note the metric that is graphed. Average latency can hide multi-modal distributions, and
outliers. Averages across all disk devices can hide unbalanced behavior, including single-
device outliers. Averages across long time periods can also hide shorter-term fluctuations.
488   Chapter 9 Disks

