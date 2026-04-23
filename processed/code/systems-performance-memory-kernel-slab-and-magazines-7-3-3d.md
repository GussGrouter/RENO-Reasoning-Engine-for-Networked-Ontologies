Slab
The kernel slab allocator manages caches of objects of a specific size, allowing them to be
recycled quickly without the overhead of page allocation. This is especially effective for kernel
allocations, which are frequently for fixed-size structs.
As a kernel example, the following two lines are from ZFS arc.c7:
df = kmem_alloc(sizeof (l2arc_data_free_t), KM_SLEEP);
head = kmem_cache_alloc(hdr_cache, KM_PUSHPAGE);

7

The only reason these came to mind as examples is because I developed the code.

The first, kmem_alloc(), shows a traditional-style kernel allocation whose size is passed as an
argument. The kernel maps this to a slab cache based on that size (very large sizes are handled
differently, by an oversize arena). The second, kmem_cache_alloc(), operates directly on a custom
slab allocator cache, in this case (kmem_cache_t *)hdr_cache.
Developed for Solaris 2.4 [Bonwick 94], the slab allocator was later enhanced with per-CPU
caches called magazines [Bonwick 01]:
Our basic approach is to give each CPU an M-element cache of objects called a magazine,
by analogy with automatic weapons. Each CPU’s magazine can satisfy M allocations
before the CPU needs to reload—that is, exchange its empty magazine for a full one.
Apart from high performance, the original slab allocator featured debug and analysis facilities
including auditing to trace allocation details and stack traces.
