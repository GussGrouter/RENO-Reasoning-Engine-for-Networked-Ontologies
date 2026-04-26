7.2.8

Allocators

While virtual memory handles multitasking of physical memory, the actual allocation and
placement within a virtual address space are often handled by allocators. These are either userland libraries or kernel-based routines, which provide the software programmer with an easy
interface for memory usage (e.g., malloc(3), free(3)).
Allocators can have a significant effect on performance, and a system may provide multiple
user-level allocator libraries to pick from. They can improve performance by use of techniques
including per-thread object caching, but they can also hurt performance if allocation becomes
fragmented and wasteful. Specific examples are covered in Section 7.3, Architecture.
