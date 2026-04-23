<!-- pdftotext -f 182 -l 230 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
5.3 Programming Languages
Programming languages may be compiled or interpreted and may also be executed via a virtual
machine. Many languages list “performance optimizations” as features, but, strictly speaking,
these are usually features of the software that executes the language, not the language itself. For
example, the Java HotSpot Virtual Machine software includes a just-in-time (JIT) compiler to
dynamically improve performance.
Interpreters and language virtual machines also provide different levels of performance observability support via their own specific tools. For the system performance analyst, basic profiling
using these tools can lead to some quick wins. For example, high CPU usage may be identified
as a result of garbage collection (GC) and then fixed via some commonly used tunables. Or it
may be caused by a code path that can be found as a known bug in a bug database and fixed by
upgrading the software version (this happens a lot).

5.3

Programming Languages

The following sections describe basic performance characteristics per programming language
type. For more about individual language performance, look for texts about that language.

