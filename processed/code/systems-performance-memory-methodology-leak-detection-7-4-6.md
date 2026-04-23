7.4.6 Leak Detection
This problem occurs when an application or kernel module grows endlessly, consuming memory
from the free lists, from the file system cache, and eventually from other processes. This may
first be noticed because the system starts swapping or an application is OOM killed, in response
to the endless memory pressure.

7.4

Methodology

This type of issue is caused by either:
■

■

A memory leak: A type of software bug where memory is no longer used but never freed.
This is fixed by modifying the software code, or by applying patches or upgrades (which
modify the code).
Memory growth: The software is consuming memory normally, but at a much higher rate
than is desirable for the system. This is fixed either by changing the software configuration,
or by the software developer changing how the application consumes memory.

Memory growth issues are often misidentified as memory leaks. The first question to ask is: Is it
supposed to do that? Check the memory usage, the configuration of your application, and the
behavior of its allocators. An application may be configured to populate a memory cache, and
the observed growth may be cache warmup.
How memory leaks can be analyzed depends on the software and language type. Some allocators
provide debug modes for recording allocation details, which can then be analyzed postmortem
for identifying the call path responsible. Some runtimes have methods for doing heap dump
analysis, and other tools for doing memory leak investigations.
The Linux BCC tracing tools includes memleak(8) for growth and leak analysis: it tracks allocations and notes those that were not freed during an interval, along with the allocation code path.
It cannot tell if these are leaks or normal growth, so your task is to analyze the code paths to
determine which is the case. (Note that this tool also incurs high overhead with high allocation
rates.) BCC is covered in Chapter 15, BPF, Section 15.1, BCC.
