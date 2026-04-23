# network-algorithmics-6-9-exercises-1-packet-filters-and-upcalls-in-the-description-on-upcalls-fig (chunk 000004)

7.1 Why timers?
Why do systems need timers? Systems need timers for failure recovery and also to implement al-
gorithms in which the notion of time or relative time is integral. Several kinds of failures cannot be
detected asynchronously. Some can be detected by periodic checking (e.g., disk watchdog timers), and
such timers always expire. Other failures can only be inferred by the lack of some positive action (e.g.,
message acknowledgment) within a specified period. If failures are infrequent, these timers rarely ex-
pire.
     Many systems also implement algorithms that use time or relative time. Examples include algo-
rithms that control the rate of production of some entity (e.g., rate-based flow control in networks) and
scheduling algorithms. These timers almost always expire.
     The performance of algorithms to implement a timer module becomes an issue when any of the
following are true. First, performance becomes an issue if the algorithm is implemented by a processor
that is interrupted each time a hardware clock ticks and the interrupt overhead is substantial. Second,
it becomes an issue if fine-granularity timers are required. Third, it becomes an issue if the average
number of active timers is large. All three factors are becoming increasingly critical in cloud servers
running at 100 Gbps that do fine-grained traffic shaping of hundreds of thousands of flows (Saeed et
al., 2017).
     If the hardware clock interrupts the host every tick and the interval between ticks is on the order
of microseconds, then the interrupt overhead is substantial. Most host operating systems offer timers
of coarse granularity (milliseconds or seconds). Alternatively, in some systems finer-granularity timers
reside in special-purpose hardware. In either case the performance of the timer algorithms will be an
issue because they determine the latency incurred in starting or stopping a timer and the number of
timers that can be simultaneously outstanding.
     As an example, consider communications between members of a distributed system. Since messages
can be lost in the underlying network, timers are needed at some level to trigger retransmissions. A
host in a distributed system can have several timers outstanding. Consider, for example, a server with
50,000 connections and three timers per connection. Further, as networks scale to 100 gigabit speeds
and beyond, both the required resolution and the rate at which timers are started and stopped will
increase.
     Some network implementations do not use a timer per packet; instead, only a few timers are used
for the entire networking package. Such TCP implementation gets away with two timers because the

7.2 Model and performance measures                  181
