# network-algorithmics-5-6-2-direct-memory-access-versus-programmed-i-o (chunk 000002)

5.7 Conclusions
As networks get faster, links today, such as Gigabit Ethernet, are often faster than the buses and memo-
ries within desktop computers and servers. Thus memory and bus bandwidth are crucial resources. This
chapter describes techniques to optimize the use of memory and bus bandwidth for processing IP and
Web packets, the dominant traffic streams found today on the Internet.
    To this end, the chapter started by showing how to remove redundant copies involved in processing
an IP packet using adaptor memory or VM remapping. We then showed how to remove redundant
copies involved in processing Web requests at a server by generalizing VM remapping to include the
file system or by combining file system and network I/O in a single system call. We then showed how
to combine various data manipulations in one fell swoop. All of these techniques require changes to the
application and kernel, but the changes are fairly localized and mostly preserve modularity.
    It is important to state that all the performance problems involved in building a modern Web server
have not been eliminated. Complex Web sites, such as amazon.com, often use several tiers of processing
to respond to Web requests, including an application server, a Web server, and a database server. Such
database-driven Web servers introduce new bottlenecks that may require new techniques beyond those
described in this chapter. However, the underlying principles should hopefully remain the same.
    Table 5.1 presents a summary of the techniques used in this chapter, together with the major prin-
ciples involved. In terms of principles this chapter is about the repeated use of P1, avoiding obvious
waste, where the waste is unnecessary reads and writes that consume precious memory and bus band-
width. At first glance, principle P1 seems vacuous or at best a cliché. What makes this principle deeper
is that the waste is not apparent unless one broadens one’s vision to see as much of the system as
possible.
    Within each local subsystem (e.g., application to kernel, kernel to network, disk to file system) there
is no wasted memory bandwidth. It is only when one follows the adventures of a received packet that

5.8 Exercises        143
