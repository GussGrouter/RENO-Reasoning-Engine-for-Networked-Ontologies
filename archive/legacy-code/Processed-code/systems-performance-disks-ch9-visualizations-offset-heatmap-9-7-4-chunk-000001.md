9.7.4    Offset Heat Maps
I/O location, or offset, can also be visualized as a heat map (and predates latency heat maps in
computing). Figure 9.13 shows an example.




Figure 9.13 DTraceTazTool
490   Chapter 9 Disks


      Disk offset (block address) is shown on the y-axis, and time on the x-axis. Each pixel is colored
      based on the number of I/O that fell in that time and latency range, darker colors for larger num-
      bers. The workload visualized was a file system archive, which creeps across the disk from block 0.
      Darker lines indicate a sequential I/O, and lighter clouds indicate random I/O.

      This visualization was introduced in 1995 with taztool by Richard McDougall. This screenshot
      is from DTraceTazTool, a version I wrote in 2006. Disk I/O offset heat maps are available from
      multiple tools, including seekwatcher (Linux).

