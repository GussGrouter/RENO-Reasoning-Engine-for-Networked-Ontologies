Chapter 8
File Systems

File system performance often matters more to the application than disk or storage device performance, because it is the file system that applications interact with and wait for. File systems
can use caching, buffering, and asynchronous I/O to avoid subjecting applications to disk-level
(or remote storage system) latency.
System performance analysis and monitoring tools have historically focused on disk performance, leaving file system performance as a blind spot. This chapter sheds light on file systems,
showing how they work and how to measure their latency and other details. This often makes it
possible to rule out file systems and their underlying disk devices as the source of poor performance, allowing investigation to move on to other areas.
The learning objectives of this chapter are:
■

Understand file system models and concepts.

■

Understand how file system workloads affect performance.

■

Become familiar with file system caches.

■

Become familiar with file system internals and performance features.

■

Follow various methodologies for file system analysis.

■

Measure file system latency to identify modes and outliers.

■

Investigate file system usage using tracing tools.

■

Test file system performance using microbenchmarks.

■

Become aware of file system tunable parameters.

This chapter consists of six parts, the first three providing the basis for file system analysis and
the last three showing its practical application to Linux-based systems. The parts are as follows:
■

■

■

Background introduces file system-related terminology and basic models, illustrating file
system principles and key file system performance concepts.
Architecture introduces generic and specific file system architecture.
Methodology describes performance analysis methodologies, both observational and
experimental.

360

Chapter 8 File Systems

■

Observability Tools shows file system observability tools for Linux-based systems,
including static and dynamic instrumentation.

■

Experimentation summarizes file system benchmark tools.

■

Tuning describes file system tunable parameters.
