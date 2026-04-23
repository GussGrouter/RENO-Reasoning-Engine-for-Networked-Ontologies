■

■

Describe performance tuning objectives.
Become familiar with performance improving techniques, including
multithreaded programming, hash tables, and non-blocking I/O.

■

Understand common locking and synchronization primitives.

■

Understand challenges posed by different programming languages.

■

Follow a thread state analysis methodology.

■

Perform CPU and off-CPU profiling.

■

Perform syscall analysis, including tracing process execution.

■

Become aware of stack trace gotchas: missing symbols and stacks.

This chapter discusses application basics, fundamentals for application performance, programming languages and compilers, strategies for generic application performance analysis, and
system-based application observability tools.

172

Chapter 5 Applications

5.1 Application Basics
Before diving into application performance, you should familiarize yourself with the role of the
application, its basic characteristics, and its ecosystem in the industry. This forms the context
within which you can understand application activity. It also gives you opportunities to learn
about common performance issues and tuning and provides avenues for further study. To learn
this context, try answering the following questions:
■

■

■

■

■

■

■

■

■

■

■

■

Function: What is the role of the application? Is it a database server, web server, load
balancer, file server, object store?
Operation: What requests does the application serve, or what operations does it perform?
Databases serve queries (and commands), web servers serve HTTP requests, and so on. This
can be measured as a rate, to gauge load and for capacity planning.
Performance requirements: Does the company running the application have a service
level objective (SLO) (e.g., 99.9% of requests at < 100 ms latency)?
CPU mode: Is the application implemented as user-level or kernel-level software? Most
applications are user-level, executing as one or more processes, but some are implemented
as kernel services (for example, NFS), and BPF programs are also kernel-level.
Configuration: How is the application configured, and why? This information may be
found in a configuration file or via administration tools. Check if any tunable parameters
related to performance have been changed, including buffer sizes, cache sizes, parallelism
(processes or threads), and other options.
Host: What hosts the application? A server or cloud instance? What are the CPUs, memory
topology, storage devices, etc.? What are their limits?
Metrics: Are application metrics provided, such as an operation rate? They may be provided
