# Systems Performance — averages (2.8.2) (averages-2-8-2) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

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
