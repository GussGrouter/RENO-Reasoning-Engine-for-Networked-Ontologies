# network-algorithmics-7-10-conclusions-this-chapter-describes-two-techniques-for-efficient-timer-im (chunk 000002)

for today’s Internet servers, which sometimes service thousands of concurrent clients. The second tech-
nique, soft timers, reduces the operating system overhead incurred by PERTICKBOOKKEEPING. This
allows a timer facility to provide fine-grained timers in the expected case, a useful feature as Internet
link speeds increase. The principles used within these two schemes are summarized in Table 7.1.
    When timing wheels were first described (Varghese and Lauck, 1987), they were generally consid-
ered as solving a useless problem. As one system designer put it at the time, “If it ain’t broke, why fix
it?”—a valid question. It helps, however, to think of schemes for problems that you project will appear
in the future. The following information is paraphrased from Justin Gibbs, a key early implementor of
FreeBSD, though its references to actual product use are dated.
    Quoted in the first edition of this book, Gibbs said that (in those days) Yahoo! served all of its
content through 500 FreeBSD servers distributed throughout the world. Also in those days, Hotmail,
the largest provider of Web-based e-mail services, initially used FreeBSD for both e-mail routing and
Web services. Further, thousands of ISPs, including two of the largest ISPs in the nation, Best Internet
and USWest, relied on FreeBSD in that era to provide Internet news services, packet routing, Web
hosting, and shell services for their users.
    In the latter half of 1997 it became apparent, however, that the timer services used in the FreeBSD
kernel would soon become a bottleneck for system throughput. Timer events were employed in several
applications that require per-transaction, time-based, notifications. As the number and/or frequency
of transactions was scaled higher, the load on the timer interface increased linearly. As an example,
the FreeBSD kernel used to schedule a “watch dog” timer for every disk transaction, which, if fired,
initiates error recovery actions. On a typical server machine, over 15% of the CPU was consumed
by timer event scheduling under a modest load of 250 concurrent disk transactions. Analysis of the
algorithms employed by the old timer interfaces showed that the CPU load would rise linearly with the
number of concurrent transactions. System scalability was compromised.
    After finding a bug in the Costello implementation that he fixed, Justin Gibbs implemented Hashed
Wheels in FreeBSD. His implementation reduced timer overhead in the FreeBSD benchmarks to a frac-
tion of a percent of total CPU usage. The Costello algorithm ensured near constant overhead regardless
of the transactional load, guaranteeing that the timer facility scaled to many thousands of transactions
with ease. While the BSD code was later updated for multicore machines and later by Motin and Ital-
iano (Motin and Italiano, 2018), the basic use of a hashed wheel remains after twenty years.
    Many other operating systems, such as Linux, now use timing wheels, as do most real-time oper-
ating systems, including ones used in routers. Note that Linux does offer two timer facilities: a coarse
timer (Corbet, 2015) that uses hierarchical wheels but limits migration (cascading) between wheels,
and a high resolution timer (Gleixner and Niehaus, 2006) that uses red-black trees. Finally, modern
cloud operating systems that do scalable traffic shaping for hundreds of thousands of flows at very fine
granularity also use hashed wheels because they allow more precise shaping with small CPU overhead
(Saeed et al., 2017). Attention to algorithmics can bear fruit in the long run.
