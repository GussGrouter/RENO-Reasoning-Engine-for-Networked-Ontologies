# network-algorithmics-6-4-5-speeding-up-select-by-changing-the-api (chunk 000003)

As we have seen, a drawback of select() is that it does work proportional to the size of the interest
set, rather than the number of events returned, which causes poor scaling. The epoll API, of course,
avoids this issue. As described in Gammo et al. (2004), if the server has many idle connections, perfor-
mance degrades badly when using select() but not when using epoll(). The advent of multicore CPUs
complicated the design of epoll() since many applications scale by using multi-threading. This was not
supported by early implementations of epoll() but was fixed later.
    There are other subtleties. Imagine a socket descriptor shared across multiple operating system
threads or processes. When an event happens all of the threads/processes must be woken up. This is
sometimes called the “thundering herd” (epoll(7), 2022) problem. This is avoided by having a flag that
ensures that the kernel wakes up just one of the waiting threads/processes.
