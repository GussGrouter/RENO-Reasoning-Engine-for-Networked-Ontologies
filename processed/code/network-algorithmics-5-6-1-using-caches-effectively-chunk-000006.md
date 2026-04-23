# network-algorithmics-5-6-1-using-caches-effectively (chunk 000006)

Software engineering considerations
Optimizations such as code restructuring (Fig. 5.12) and locality-driven processing (Fig. 5.13) also
need to be evaluated by their effects on code modularity and maintenance. After all, one could rewrite
the kernel and all applications using assembly language to more perfectly optimize memory bandwidth.
But it would be difficult to get the code to work or be maintainable.
    Code restructuring is best done by a compiler. For example, error-handling code can be annotated
with hints (Mosberger et al., 1996) suggesting which branches are more frequently taken (generally
obvious to the programmer), and a specially augmented compiler can restructure the code for I-cache
locality. Algorithms for this purpose are described in Mosberger et al. (1996).
    On the other hand, locality-driven processing preserves modularity within layers. Communication
between layers must be changed as follows. If each layer code passes a packet to the code for a higher
layer with a procedure call, this code must be modified to add packets to a queue for the higher layer.
Similarly, when a layer is called, it removes packets from its read queue until the queue is exhausted;
after processing each packet, it places it on the queue for its next-higher layer. This strategy works well
when each layer can reuse buffers from other layers, as is the case for UNIX mbufs. Overall, the code
changes may not be severe.

142      Chapter 5 Copying data
