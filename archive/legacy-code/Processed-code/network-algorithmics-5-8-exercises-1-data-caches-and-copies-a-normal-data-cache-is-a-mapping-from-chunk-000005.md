# network-algorithmics-5-8-exercises-1-data-caches-and-copies-a-normal-data-cache-is-a-mapping-from (chunk 000005)

Table 6.1 Techniques for reducing control overhead that are discussed in
             this chapter, together with the corresponding principles.
             Number                             Principle                              Used in
             P8         Go beyond downcalls used in specifications               Upcalls
             P8         Process per message, not per layer                       x-Kernel
             P13        Link protocol implementation with user code              Mach variants
             P13        Process per disk access                                  Flash
             P13        Modularize by task, not clients                          Haboob Web server
             P4         VM mapping to avoid copies in cache and application      Flash
             P15        Bitmap tree                                              Fast ufalloc()
             P12a       Incrementally compute interest vector                    Fast select()
             P9         Pass hints from protocol to select ()
             P12        Remember interest across calls
             P3c        Move protection from kernel to adaptor                   ADCs
             P2         Have kernel authorize adaptor on initialization
             P13        Batch process interrupts                                 Most OSs
             P2b        Execute protocol in the context of the receive process   LRP (lazy receiver
                                                                                 processing)
