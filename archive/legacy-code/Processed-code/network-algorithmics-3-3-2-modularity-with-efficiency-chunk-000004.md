# network-algorithmics-3-3-2-modularity-with-efficiency (chunk 000004)

To translate a virtual address into a physical address, a processor first tries a cache called the TLB.
If this fails, the processor must look up the page table. A prefix of the address bits is used to index into
the page table directly. The use of table lookup avoids the use of hash tables or binary search, but it
requires large page table sizes. A networking example of this technique is timing wheels (Chapter 7),
where an efficient algorithm for a fixed timer range is constructed using a circular array.

P15: Use algorithmic techniques to create efficient data structures
Even where there are major bottlenecks, such as virtual address translation, systems designers finesse
the need for clever algorithms by passing hints, using caches, and performing table lookup. Thus a
major system designer is reported to have told an eager theoretician: “I don’t use algorithms, son.”
    This book does not take this somewhat antiintellectual position. Instead, it contends that, in context,
efficient algorithms can greatly improve system performance. In fact, a fair portion of the book will be
spent describing such examples. However, there is a solid kernel of truth to the “I don’t use algorithms”
putdown. In many cases, Principles P1 through P14 need to be applied before any algorithmic issues
become bottlenecks.
    Algorithmic approaches include the use of standard data structures as well as generic algorithmic
techniques, such as divide-and-conquer and randomization. The algorithm designer must, however, be
prepared to see his clever algorithm become obsolete because of changes in system structure and tech-
nology. As described in the introduction, the real breakthroughs may arise from applying algorithmic
thinking as opposed to merely reusing existing algorithms.
    Examples of the successful use of algorithms in computer systems are the Lempel–Ziv compression
algorithm employed in the UNIX utility gzip, the Rabin–Miller primality test algorithm found in public
key systems, and the common use of B-trees (due to Bayer–McCreight) in databases (Cormen et al.,
1990). Networking examples studied in this text include the Lulea IP-lookup algorithm (Chapter 11)
and the RFC scheme for packet classification (Chapter 12).
