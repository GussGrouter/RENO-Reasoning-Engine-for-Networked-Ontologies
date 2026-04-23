# network-algorithmics-3-3-2-modularity-with-efficiency (chunk 000001)

# Network Algorithmics — fifteen principles: modularity with efficiency (3.3.2) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 88 -l 111 -layout
- Slice: from `3.3.2 Principles for modularity with efficiency` up to (excluding) `3.3.3 Principles for speeding up routines`

---

3.3.2 Principles for modularity with efficiency
An engineer who had read Dave Clark’s classic papers (e.g., Clark [1985]) on the inefficiencies of
layered implementations once complained to a researcher about modularity. The researcher (Radia
Perlman) replied, “But that’s how we got to the stage where we could complain about something.” Her
point, of course, was that complex systems like network protocols could only have been engineered
using layering and modularity. The following principles, culled from work by Clark and others, show
how to regain efficiencies while retaining modularity.

P6: Create efficient specialized routines by replacing inefficient general-purpose routines
As in mathematics, the use of abstraction in computer system design can make systems compact, or-
thogonal, and modular. However, at times the one-size-fits-all aspect of a general-purpose routine leads
to inefficiencies. In important cases, it can pay to design an optimized and specialized routine.
    A systems example can be found in database caches. Most general-purpose caching strategies would
replace the least recently used record to disk. However, consider a query-processing routine processing
a sequence of database tuples in a loop. In such a case, it is the most recently used record that will be
used furthest in the future, so it is the ideal candidate for replacement. Thus many database applications

---

## PDF page 90

3.3 Fifteen implementation principles—categorization and description                                       63

replace the operating system caching routines with more specialized routines. It is best to do such spe-
cialization only for key routines, to avoid code bloat. A networking example is the fast UDP processing
routines that we describe in Chapter 9.

P7: Avoid unnecessary generality
The tendency to design abstract and general subsystems can also lead to unnecessary or rarely used
features. Thus, rather than building several specialized routines (e.g., P6) to replace the general-purpose
routine, we might remove features to gain performance.4
    Of course, as in the case of P3, removing features requires users of the routine to live with re-
strictions. For example, in RISC processors, the elimination of complex instructions such as multiplies
required multiplication to be emulated by firmware. A networking example is provided by Fbufs (Chap-
ter 5), which provides a specialized virtual memory service that allows efficient copying between virtual
address spaces.

P8: Don’t be tied to reference implementations
Specifications are written for clarity, not to suggest efficient implementations. Because abstract speci-
fication languages are unpopular, many specifications use imperative languages such as C. Rather than
precisely describe what function is to be computed, one gets code that prescribes how to compute the
function. This has two side effects.
    First, there is a strong tendency to overspecify. Second, many implementors copy the reference
implementation in the specification, which is a problem when the reference implementation was chosen
for conceptual clarity and not efficiency. As Clark (1985) points out, implementors are free to change
the reference implementation as long as the two implementations have the same external effects. In
fact, there may be other structured implementations that are efficient as well as modular.
    For example, Charlie knows that when a recipe tells him to cut beans and then to cut carrots, he can
interchange the two steps. In the systems world, Clark originally suggested the use of upcalls (Clark,
1985) for operating systems. In an upcall, a lower layer can call an upper layer for data or advice, seem-
ingly violating the rules of hierarchical decomposition introduced in the design of operating systems.
Upcalls are commonly used today in network protocol implementations.
