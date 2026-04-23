7.3.3 (continued) — TCMalloc (book overview)

TCMalloc
TCMalloc is the user-level thread caching malloc, which uses a per-thread cache for small allocations, reducing lock contention and improving performance [Ghemawat 07]. Periodic garbage
collection migrates memory back to a central heap for allocations.
