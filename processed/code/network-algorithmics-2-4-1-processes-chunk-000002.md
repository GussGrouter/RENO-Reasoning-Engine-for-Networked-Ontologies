# network-algorithmics-2-4-1-processes (chunk 000002)

Under high network load, the computer can enter what is called receiver livelock (Mogul and Ra-
makrishnan, 1997), in which the computer spends all its time processing incoming packets, only to
discard them later because the applications never run. In our example, if there is a series of back-to-
back packet arrivals, only the highest-priority interrupt handler will run, possibly leaving no time for
the software interrupt and certainly leaving none for the browser process. Thus either the IP or socket
queues will fill up, causing packets to be dropped after resources have been invested in their processing.
Methods to mitigate this effect are described in Chapter 6.
    Notice also that the latency and throughput of network code in an endnode depend on “process”
activation times. For example, current figures for Pentium IV machines show around 2 µsec of interrupt
latency for a null interrupt call, around 10 µsec for a Process Context switch on a Linux machine
with two processes, and much more time for Windows and Solaris on the same machine. These times
may seem small, but recall that 30 minimum-size (40-byte) packets can arrive in 10 µsec on a Gigabit
Ethernet link.
