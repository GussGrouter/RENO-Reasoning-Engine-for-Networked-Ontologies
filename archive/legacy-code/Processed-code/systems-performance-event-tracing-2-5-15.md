# Systems Performance — event tracing (2.5.15) (PDF pages 96–104)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-drilldown-latency-methodr-scout-p96-104.md

---

2.5.15 Event Tracing
Systems operate by processing discrete events. These include CPU instructions, disk I/O and
other disk commands, network packets, system calls, library calls, application transactions,
database queries, and so on. Performance analysis usually studies summaries of these events,
such as operations per second, bytes per second, or average latency. Sometimes important detail
is lost in the summary, and the events are best understood when inspected individually.

Network troubleshooting often requires packet-by-packet inspection, with tools such as
tcpdump(8). This example summarizes packets as single lines of text:

# tcpdump -ni eth4 -ttt
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth4, link-type EN10MB (Ethernet), capture size 65535 bytes
00:00:00.000000 IP 10.2.203.2.22 > 10.2.0.2.33986: Flags [P.], seq
1182098726:1182098918, ack 4234203806, win 132, options [nop,nop,TS val 1751498743
ecr 1751639660], length 192
58   Chapter 2 Methodologies


     00:00:00.000392 IP 10.2.0.2.33986 > 10.2.203.2.22: Flags [.], ack 192, win 501,
     options [nop,nop,TS val 1751639684 ecr 1751498743], length 0
     00:00:00.009561 IP 10.2.203.2.22 > 10.2.0.2.33986: Flags [P.], seq 192:560, ack 1,
     win 132, options [nop,nop,TS val 1751498744 ecr 1751639684], length 368
     00:00:00.000351 IP 10.2.0.2.33986 > 10.2.203.2.22: Flags [.], ack 560, win 501,
     options [nop,nop,TS val 1751639685 ecr 1751498744], length 0
     00:00:00.010489 IP 10.2.203.2.22 > 10.2.0.2.33986: Flags [P.], seq 560:896, ack 1,
     win 132, options [nop,nop,TS val 1751498745 ecr 1751639685], length 336
     00:00:00.000369 IP 10.2.0.2.33986 > 10.2.203.2.22: Flags [.], ack 896, win 501,
     options [nop,nop,TS val 1751639686 ecr 1751498745], length 0
     [...]

     Varying amounts of information can be printed by tcpdump(8) as needed (see Chapter 10,
     Network).

     Storage device I/O at the block device layer can be traced using biosnoop(8) (BCC/BPF-based):

     # biosnoop
     TIME(s)         COMM              PID      DISK      T SECTOR        BYTES       LAT(ms)
     0.000004        supervise         1950     xvda1     W 13092560      4096           0.74
     0.000178        supervise         1950     xvda1     W 13092432      4096           0.61
     0.001469        supervise         1956     xvda1     W 13092440      4096           1.24
     0.001588        supervise         1956     xvda1     W 13115128      4096           1.09
     1.022346        supervise         1950     xvda1     W 13115272      4096           0.98
     [...]

     This biosnoop(8) output includes the I/O completion time (TIME(s)), initiating process details
     (COMM, PID), disk device (DISK), type of I/O (T), size (BYTES), and I/O duration (LAT(ms)). See
     Chapter 9, Disks, for more information about this tool.

     The system call layer is another common location for tracing. On Linux, it can be traced using
     strace(1) and perf(1)’s trace subcommand (see Chapter 5, Applications). These tools also have
     options to print timestamps.

     When performing event tracing, look for the following information:

         ■   Input: All attributes of an event request: type, direction, size, and so on
         ■   Times: Start time, end time, latency (difference)
         ■   Result: Error status, result of event (e.g., successful transfer size)

     Sometimes performance issues can be understood by examining attributes of the event, for
     either the request or the result. Event timestamps are particularly useful for analyzing latency
     and can often be included by using event tracing tools. The preceding tcpdump(8) output
     included delta timestamps, measuring the time between packets, using -ttt.

     The study of prior events provides more information. An uncommonly high latency event,
     known as a latency outlier, may be caused by previous events rather than the event itself. For
     example, the event at the tail of a queue may have high latency but be caused by the previously
     queued events, not its own properties. This case can be identified from the traced events.
                                                                                  2.5 Methodology       59
