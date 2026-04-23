<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (combined extract; Chapter 5 Applications) -->
Some companies use a target application performance index (ApDex or Apdex) as an objective
and as a metric to monitor. It can better convey customer experience and involves first classifying customer events as to whether they are “satisfactory,” “tolerable,” or “frustrating.” The
Apdex is then calculated using [Apdex 20]:
Apdex = (satisfactory + 0.5 × tolerable + 0 × frustrating) / total events
The resulting Apdex ranges from 0 (no satisfied customers) to 1 (all satisfied customers).

5.1.2

Optimize the Common Case

Software internals can be complex, with many different code paths and behaviors. This may be
especially evident if you browse the source code: applications are commonly tens of thousands
of lines of code, while operating system kernels are upward of hundreds of thousands. Picking
areas to optimize at random may involve a great deal of work for not much gain.
One way to efficiently improve application performance is to find the most common code path
for the production workload and begin by improving that. If the application is CPU-bound,
that may mean the code paths that are frequently on-CPU. If the application is I/O-bound, you
should be looking at the code paths that frequently lead to I/O. These can be determined by
analysis and profiling of the application, including studying stack traces and flame graphs, as
covered in later chapters. A higher level of context for understanding the common case may also
be provided by application observability tools.

5.1.3

Observability

As I reiterate in many chapters of this book, the biggest performance wins can come from
eliminating unnecessary work.
This fact sometimes gets overlooked when an application is being selected based on performance.
If benchmarking showed application A to be 10% faster than application B, it may be tempting
to choose application A. However, if application A is opaque and application B provides a rich set
of observability tools, it’s very likely that application B will be the better choice in the long run.
Those observability tools make it possible to see and eliminate unnecessary work and to better
understand and tune active work. The performance wins gained through enhanced observability
may dwarf the initial 10% performance difference. The same is true for the selection of languages
and runtimes: such as choosing Java or C, which are mature and have many observability tools,
versus choosing a new language.

5.1

Application Basics

5.1.4 Big O Notation
Big O notation, commonly taught as a computer science subject, is used to analyze the complexity of algorithms and to model how they will perform as the input dataset scales. The O refers to
the order of the function, describing its growth rate. This notation helps programmers pick more
efficient and performant algorithms when developing applications [Knuth 76][Knuth 97].
Common big O notations and algorithm examples are listed in Table 5.1.

Table 5.1

Example big O notations

Notation

Examples

O(1)

Boolean test

O(log n)

