# network-algorithmics-5-2-3-fbufs-optimizing-page-remapping (chunk 000004)

So far, it is possible that premapped page 8 in the first application on a path is mapped to page 10
in the second application. This is painful because when the second application reads a descriptor for
page 8, it must somehow know that it corresponds to its own VP 10. Instead, the designers used the
principle of avoiding unnecessary generality (P7) and insisted that the fbuf get mapped to the same VP
in all applications on the path. This can be done by reserving some number of initial pages in the VM
of all processes to be fbuf pages.
    At this point, we may feel that we are finished, but there are still a few thorny problems. To achieve
protection, we allowed only a single writer and had multiple readers. However, that means that pages
are immutable; only the writer can touch them. But what about adding headers when one goes down
the stack. The solution to this problem is shown in Fig. 5.7, where a packet is really an aggregate data
structure with pointers to individual fbufs so that headers can be added by adding an ordinary buffer or
an fbuf to the aggregate.
    This is not as big a deal as it sounds because the commonly used UNIX mbufs (see Chapter 9) are
also composites of buffers strung together.4
    So far, the fbuf scheme has used the underlying VM mapping ideas in Fig. 5.3 except that it has
made them more efficient by amortizing the mapping costs over (hopefully) a large number of packet
transfers. Page table updates are removed in the common case. This can be done in ordinary operating
systems. In fact, after the fbufs paper, Thadani and Khalidi (1995) extended the idea and implemented
it in Sun’s Solaris operating system. But this begs the question: How are standard copy semantics
preserved? What if the application does a Write? A standard operating system such as UNIX cannot
depend on COW as in Fig. 5.3.
    The ultimate answer in fbufs is that standard copy semantics are not preserved. The API is changed.
Application writers must be careful not to write to an fbuf when it has been handed to the kernel until
the fbuf is returned by the kernel in a free list. To protect against buggy or malicious code, the kernel

4 To be precise, UNIX mbufs are strung together in a linear topology, while buffer aggregates form a more general tree topology,
but the performance costs due to chaining and indexing are similar.

5.2 Reducing copying via local restructuring           123

FIGURE 5.7
Using aggregate objects to allow adding layers to add headers while allowing only a single writer.
