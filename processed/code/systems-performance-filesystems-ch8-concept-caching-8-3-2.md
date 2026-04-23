8.3.2

Caching

The file system will typically use main memory (RAM) as a cache to improve performance. For
applications, this process is transparent: application logical I/O latency becomes much lower
(better), as it can be served from main memory rather than the much slower disk devices.
Over time, the cache grows, while free memory for the operating system shrinks. This can alarm
new users, but is perfectly normal. The principle is: If there is spare main memory, do something
useful with it. When applications need more memory, the kernel should quickly free it from the
file system cache for use.
File systems use caching to improve read performance, and buffering (in the cache) to improve
write performance. Multiple types of cache are typically used by the file system and the block
device subsystem, which may include those in Table 8.1.

**(Table 8.1 omitted — example cache-type names; see book PDF and Section 8.4.)**

Specific cache types are described in Section 8.4, Architecture, while Chapter 3, Operating
Systems, has the full list of caches (including application- and device-level).

