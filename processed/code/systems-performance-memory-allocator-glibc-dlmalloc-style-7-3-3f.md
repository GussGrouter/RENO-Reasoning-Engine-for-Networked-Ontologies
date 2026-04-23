7.3.3 (continued) — glibc allocator (book overview)

glibc
The user-level GNU libc allocator is based on dlmalloc by Doug Lea. Its behavior depends on the
allocation request size. Small allocations are served from bins of memory, containing units of a
similar size, which can be coalesced using a buddy-like algorithm. Larger allocations can use
a tree lookup to find space efficiently. Very large allocations switch to using mmap(2). The net
result is a high-performing allocator that benefits from multiple allocation policies.
