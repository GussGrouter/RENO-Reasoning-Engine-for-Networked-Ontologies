# network-algorithmics-6-8-conclusions-after-the-basic-restructuring-to-avoid-copying-control-overh (chunk 000002)

the processing of instructions using cached data without a commensurate speedup in context switching
and interrupt processing.
    This chapter started by surveying basic techniques for reducing process-scheduling overhead for
networking code. These lessons have been taken to heart by the networking community. Hardly any
implementor worth his or her salt will do something egregious, such as structuring each layer as a
separate process, and not resorting freely to upcalls. However, the deeper lesson of Fig. 6.2 is not
the seemingly arcane structure, but the implicit idea of user-level networking. User-level networking
was not developed at the time Clark presented his paper, but is mainstream today. Note that user-
level networking, together with ADCs, makes possible technologies such as DPDK (2018) which are
pervasive.
    On the other hand, the art of structuring processing in the application context, for example, a Web
server, is still an open question. While event-driven servers (augmented with helper processes) sat-
isfactorily balance the need to maximize concurrency and minimize context-switching overhead, the
software engineering and debugging aspects of such designs still leave many questions unanswered.
The staged event-driven approach is a step in this direction.
    The event-driven approach also relies on the fast implementation of equivalents of the select() call.
While the select() approaches has fundamental scalability problems, it is reassuring that the ideas for
new event notification APIs described in the first edition (Banga et al., 1999) have now become main-
stream in Linux with epoll().
    Allowing applications to communicate directly with network devices using a protected virtual in-
terface is an idea that is here to stay with technologies such as DPDK (2018) and SPDK (spdk, 2022).
Finally, while interrupts are fundamentally unavoidable, their nuisance value can be greatly mitigated
by the use of batching and the use of polling in appropriate environments. Once again, it is reassuring
to know that the fundamental ideas of avoiding receive livelock (Mogul and Ramakrishnan, 1997) de-
scribed in the first edition are alive and well in moderm technologies such as DPDK and Linux NAPI
polling (Salim et al., 2001).
    Some of the more radical operating system restructuring ideas described in this chapter may be
needed in the near future, given the throughput and latency limits of even the best tuned network
stacks in conventional operating systems. In terms of ideas, papers like Arrakis (Peter et al., 2015) and
Shenango (Ousterhout et al., 2019) show that just as operating system ideas impact endnode networking
(as in most of this chapter), the reverse can also be true. Arguably, Arrakis (Peter et al., 2015) is
influenced by the data plane, control plane separation in telephone networks and Software Defined
Networks. On the other hand, Shenango (Ousterhout et al., 2019) uses mechanisms to detect congestion
in operating system queues that are arguably inspired by classic networking techniques—though the
specifics are different.
    Table 6.1 shows a list of the techniques used in this chapter, with the corresponding principles. In
summary, while Epictetus urged his readers to control their passions, we feel it is equally important for
implementors of networking code to be passionate about control.
