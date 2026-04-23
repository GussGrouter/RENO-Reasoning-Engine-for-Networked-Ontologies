      9.7.2     Latency Scatter Plots
      Scatter plots are useful for visualizing I/O latency per-event, which may include thousands of
      events. The x-axis can show completion time, and the y-axis I/O response time (latency). The
      example in Figure 9.11 plots 1,400 I/O events from a production MySQL database server, cap-
      tured using iosnoop(8) and plotted using R.




      Figure 9.11 Scatter plot of disk read and write latency

      The scatter plot shows reads (+) and writes ( ) differently. Other dimensions could be plotted, for
                                                   °
      example, disk block address on the y-axis instead of latency.

      A couple of read outliers can be seen here, with latencies over 150 ms. The reason for these
      outliers was previously not known. This scatter plot, and others that included similar outliers,
      showed that they occur after a burst of writes. The writes have low latency since they returned
      from a RAID controller write-back cache, which will write them to the device after returning the
      completions. I suspect that the reads are queueing behind the device writes.

      This scatter plot showed a single server for a few seconds. Multiple servers or longer intervals can
      capture many more events, which when plotted merge together and become difficult to read. At
      that point, consider using a latency heat map.

