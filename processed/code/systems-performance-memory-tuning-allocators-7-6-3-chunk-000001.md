7.6.3

Allocators

Different user-level allocators may be available, offering improved performance for multithreaded
applications. These may be selected at compile time, or at execution time by setting the
LD_PRELOAD environment variable.
For example, the libtcmalloc allocator could be selected using:
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4

This may be placed in its startup script.

