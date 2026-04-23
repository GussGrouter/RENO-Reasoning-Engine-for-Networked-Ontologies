# network-algorithmics-5-8-exercises-1-data-caches-and-copies-a-normal-data-cache-is-a-mapping-from (chunk 000002)

tents of L and M. A memory access to either L or M will return C. What is the advantage over
     the previous scheme in the previous item?
   • This is all very speculative and wild. Comment on the disadvantages of the idea in the previous
     item. In particular, many caches use a technique called set associativity, where a simple hash
     function (e.g., low-order bits) is used to select a small set of cache entries that the hardware
     searches in parallel. Why might the multiple address per cache entry interact poorly with the set
     associative search?
2. Application-level optimizations for Web servers: Operating systems such as the Exokernel (En-
   gler et al., 1995) take an even more extreme viewpoint and allow the application to customize kernel
   features for its benefit without compromising safety for other applications. One interesting optimiza-
   tion is to combine the final TCP FIN with the read of the last data segment (an optimization allowed
   by TCP).
   • Why does this optimization help small Web transfers (which are quite common)?
   • Why is this optimization hard to do in a regular Web server, and why is it easier if the application
     is integrated with the kernel, as in the Exokernel?
   • Explain how this optimization can be migrated to an ordinary Web server by passing information
     across the interface (P9) without compromising safety.
3. Reverse copyout: The emulated COW paper (Brustoloni and Steenkiste, 1996) describes an inter-
   esting degree of freedom (P13) for copying page-aligned data between two modules (say, system
   and application). Imagine that you wish to copy a partial page from an application page, X, to a
   system page, Y . If the page is full, assume that you can swap the two pages efficiently. Assume the
   partial page has useful data D and some remainder R.
   • If the amount of data D is small compared to R, it is simpler to copy D to the destination page in
     Y . On the other hand, if D is large (say, almost all of the page) compared to R, devise a simple
     strategy to minimize copying. Note that if the destination page, Y , has some other data in the
     remainder of the page, that data must remain after the copy.
   • What is a simple threshold you would use to choose between these two strategies?

CHAPTER

Transferring control
                                                                                                                      6
                                                                           Control thy passions, lest they take vengeance on thee.
                                                                                                                      —Epictetus
