# Network Algorithmics — 18.1.3 Toward a synthesis In his book The Character of Physical Law, Richard Feynman argues that we have a need to understand (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 543
- Slice: from `18.1.3 Toward a synthesis In his book The Character of Physical Law, Richard Feynman argues that we have a need to understand` up to next detected section heading

---

18.1.3 Toward a synthesis
In his book The Character of Physical Law, Richard Feynman argues that we have a need to understand
the world in “various hierarchies, or levels.” Later, he goes on to say that “all the sciences, and not
just the sciences but all the efforts of intellectual kinds, are an endeavor to see the connections of the
hierarchies . . . and in that way we are gradually understanding this tremendous world of interconnecting
hierarchies.”
    We have divided network algorithmics into two hierarchies: endnode algorithmics and router algo-
rithmics. What are the connections between these two hierarchies? Clearly, we have used the same set
of 15 principles to understand and derive techniques in both areas. But are there other unities that can
provide insight and suggest new directions?
    There are differences between endnode and router algorithmics. Endnodes have large, structured,
and general-purpose operating systems that require workarounds to obtain high performance; routers,

                                                    18.1 What this book has been about               517



by contrast, have fairly primitive operating systems (e.g., Cisco IOS) that bear some resemblance to a
real-time operating system. Most endnodes’ protocol functions are implemented (today) in software,
while the critical performance functions in a router are implemented in hardware. Endnodes compute,
routers communicate. Thus routers have no file system and no complex process scheduling.
    But there are similarities as well between endnode and router algorithmics.
• Copying in endnodes is analogous to the data movement orchestrated by switching in routers.
• Demultiplexing in endnodes is analogous to classification in routers.
• Scheduling in endnodes is analogous to fair queuing in routers.
    Other than packet classification, where the analogy is more exact, it may seem that the other cor-
respondences are a little stretched. However, these analogies suggest the following potentially fruitful
directions.
   1. Switch-based endnode architectures: The analogy between copying and switching, and the clean
separation between I/O and computation in a router, suggests that this may also be a good idea for
endnodes. More precisely, most routers have a crossbar switch that allows parallel data transfers using
dedicated ASICs or processors; packets meant for internal computation are routed to a separate set
of processors. While we considered this briefly in Chapter 2, we did not consider very deeply the
implications for endnode operating systems.
By dedicating memory bandwidth and processing to I/O streams, the main computational processors
can compute without interruptions, system calls, or kernel thread because I/O is essentially serviced and
placed in clean form by a set of I/O processors (using separate memory bandwidth that does not interfere
with the main processors) for use by the computational processors when they switch computational
tasks. With switch-based bus replacements such as Infiniband, and the increasing use of protocol offload
engines such as TCP chips, this vision is already realizable. However, while the hardware elements are
present, a fundamental restructuring of operating systems is needed to fully realize the potential of this
vision as for example in Arrakis (Peter et al., 2015) described in Chapter 6.
   2. Generalized endnode packet classification: Although there seems to be a direct correspondence
between packet classification in endnodes (Chapter 8) and packet classification in routers (Chapter 12),
the endnode problem is simpler because it works only for a constrained set of classifiers, where all
the wildcards are at the end. Router classifiers, on the other hand, allow arbitrary classifiers, requiring
more complicated algorithmic machineries or CAMs. To be fair, in recent years the packet classifiers
in Linux and other operating systems have come closer to the power of routers and in some cases have
gone beyond because of their ability to do application level filtering.
   3. Fair queuing in endnodes: Fair queuing in routers was originally invented to provide more dis-
criminating treatment to flows in times of overload and (later) to provide quality of service to flows in
terms of, say, latency. Both these issues resonate in the endnode environment. For example, the problem
of receiver livelock (Chapter 6) requires discriminating between flows during times of overload. The
use of early demultiplexing and separate IP queues per flow in lazy receiver processing seems like a
first crude step toward fair queuing. Similarly, many endnodes do real-time processing, such as running
MPEG players, just as routers have to deal with the real-time constraints of, say, voice-over-IP packets.
Thus a reasonable question is whether the work on fair schedulers in the networking community can
be useful in an operating system environment. When a sending TCP is scheduling between multiple
concurrent connections, could it use a scheduling algorithm such as DRR for better fairness? At a

518       Chapter 18 Conclusions



higher level, could a Web server use worst-case weighted fair queuing to provide better delay bounds for
certain clients? In recent years the two communities (scheduling in routers and scheduling in endnode)
have influenced each other. Today sophisticated endnode scheduling algorithms are implemented in
operating systems such as Linux qdisc (Components of Linux Traffic Control, 2022) and Google’s
carousel (Saeed et al., 2017) described in Chapter 7.
   So far, we have suggested that endnodes could learn from router design in overall I/O architecture
and operating system design. Routers can potentially learn the following from endnodes.
   1. Fundamental Algorithms: Fundamental algorithms for endnodes, such as selection, buffer allo-
cation, CRCs, and timers, are likely to be useful for routers, because the router processor is still an
endnode, with very similar issues.
   2. More Structured Router Operating Systems: While the internals of router operating systems, such
as Cisco’s IOS and Juniper’s JunOS, are hidden from public scrutiny, there is at least anecdotal evidence
that there are major software engineering challenges associated with such systems as time progresses
(leading to the need to be compatible with multiple past versions) and as customers ask for special
builds. Perhaps routers can benefit from some of the design ideas behind existing operating systems
that have stood the test of time.
While protection may be fundamentally unnecessary (no third-party applications running on a router),
how should a router operating system be structured for modularity? One approach to building a modular
but efficient router operating system can be found in the router plugins system (Decasper et al., 1998)
and the Click operating system (Kohler et al., 2000). More modern proposals include Arrakis (Peter et
al., 2015) and (Belay et al., 2016).
   3. Vertically Integrated Routers: The components of an endnode (applications, operating system,
boxes, chips) are often built by separate companies, thus encouraging innovation. The interface be-
tween these components is standardized (e.g., the API between applications and operating system),
allowing multiple companies to supply new solutions. Why should a similar vision not hold for routers
some years from now especially as the vision of Software Defined Networks continues to take hold?
Currently, this is more of a business than a technical issue because the dominant vendors do not want
to open up the market to competitors. However, this was true in the past for computers and is no longer
true; thus there is hope.
We are already seeing router chips being manufactured by semiconductor companies. However, a great
aid to progress would be a standardized router operating system that is serious and general enough for
production use by several, if not all, router companies.1 Such a router operating system would have to
work across a range of router architectures, just as operating systems span a variety of multiprocessor
and disk architectures.
Once this is the case, perhaps there is even a possibility of “applications” that run on routers. This is not
as far-fetched as it sounds, because there could be a variety of security and measurement programs that
operate on a subset of the packets received by the router. With the appropriate API (and especially if
the programs are operating on a logged copy of the router packet stream), such applications could even
be farmed out to third-party application developers. It is probably easy to build an environment where


1 Click is somewhat biased toward endnode bus-based routers as opposed to switch-based routers with ASIC support.

                                                   18.2 What network algorithmics is about            519



a third-party application (working on logged packets) cannot harm the main router functions, such as
forwarding and routing.
