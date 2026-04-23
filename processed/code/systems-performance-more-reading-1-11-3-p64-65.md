                                                                                    2.3    Concepts     25


transfer time. DNS latency refers to the entire DNS operation. TCP connection latency refers to
the initialization only (TCP handshake).

At a higher level, all of these, including the TCP data transfer time, may be treated as latency
of something else. For example, the time from when the user clicks a website link to when the
resulting page is fully loaded may be termed latency, which includes the time for the browser
to fetch a web page over a network and render it. Since the single word “latency” can be ambig-
uous, it is best to include qualifying terms to explain what it measures: request latency, TCP
connection latency, etc.

As latency is a time-based metric, various calculations are possible. Performance issues can
be quantified using latency and then ranked because they are expressed using the same units
(time). Predicted speedup can also be calculated, by considering when latency can be reduced or
removed. Neither of these can be accurately performed using an IOPS metric, for example.

For reference, time orders of magnitude and their abbreviations are listed in Table 2.1.


Table 2.1       Units of time
Unit                   Abbreviation     Fraction of 1 Second
Minute                 m                60
Second                 s                1
Millisecond            ms               0.001 or 1/1000 or 1 × 10 -3
Microsecond            μs               0.000001 or 1/1000000 or 1 × 10 -6
Nanosecond             ns               0.000000001 or 1/1000000000 or 1 × 10 -9
Picosecond             ps               0.000000000001 or 1/1000000000000 or 1 × 10 -12



When possible, converting other metric types to latency or time allows them to be compared. If
you had to choose between 100 network I/O or 50 disk I/O, how would you know which would
perform better? It’s a complicated question, involving many factors: network hops, rate of net-
work drops and retransmits, I/O size, random or sequential I/O, disk types, and so on. But if you
compare 100 ms of total network I/O and 50 ms of total disk I/O, the difference is clear.


2.3.2         Time Scales
While times can be compared numerically, it also helps to have an instinct about time, and rea-
sonable expectations for latency from different sources. System components operate over vastly
different time scales (orders of magnitude), to the extent that it can be difficult to grasp just how
big those differences are. In Table 2.2, example latencies are provided, starting with CPU register
access for a 3.5 GHz processor. To demonstrate the differences in time scales we’re working with,
the table shows an average time that each operation might take, scaled to an imaginary system
in which a CPU cycle—0.3 ns (about one-third of one-billionth1 of a second) in real life—takes
one full second.

1
    US billionth: 1/1000,000,000
26   Chapter 2 Methodologies


     Table 2.2     Example time scale of system latencies
     Event                                                  Latency                 Scaled
     1 CPU cycle                                              0.3 ns                1s
     Level 1 cache access                                     0.9 ns                3s
     Level 2 cache access                                       3 ns              10 s
     Level 3 cache access                                      10 ns              33 s
     Main memory access (DRAM, from CPU)                     100 ns                 6 min
     Solid-state disk I/O (flash memory)                 10–100 μs             9–90 hours
     Rotational disk I/O                                    1–10 ms             1–12 months
     Internet: San Francisco to New York                       40 ms                4 years
     Internet: San Francisco to United Kingdom                 81 ms                8 years
     Lightweight hardware virtualization boot                100 ms               11 years
     Internet: San Francisco to Australia                    183 ms               19 years
     OS virtualization system boot                            <1s                105 years
     TCP timer-based retransmit                              1–3 s         105–317 years
     SCSI command time-out                                     30 s                 3 millennia
     Hardware (HW) virtualization system boot                  40 s                 4 millennia
     Physical system reboot                                     5m                32 millennia



     As you can see, the time scale for CPU cycles is tiny. The time it takes light to travel 0.5 m, per-
     haps the distance from your eyes to this page, is about 1.7 ns. During the same time, a modern
     CPU may have executed five CPU cycles and processed several instructions.

     For more about CPU cycles and latency, see Chapter 6, CPUs, and for disk I/O latency, Chapter 9,
     Disks. The Internet latencies included are from Chapter 10, Network, which has more examples.


     2.3.3       Trade-Offs
     You should be aware of some common performance trade-offs. The good/fast/cheap “pick two”
     trade-off is shown in Figure 2.4, alongside the terminology adjusted for IT projects.




     Figure 2.4 Trade-offs: pick two
