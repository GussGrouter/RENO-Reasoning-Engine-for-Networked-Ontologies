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

P9: Pass hints in module interfaces
A hint is information passed from a client to a service that, if correct, can avoid expensive computation
by the service. The two key phrases are passed and if correct. By passing the hint in its request, a
service can avoid the need for the associative lookup needed to access a cache. For example, a hint can
be used to supply a direct index into the processing state at the receiver. Also, unlike caches, the hint is
not guaranteed to be correct and hence must be checked against other certifiably correct information.
Hints improve performance if the hint is correct most of the time.
    This definition of a hint suggests a variant in which information is passed that is guaranteed to be
correct and hence requires no checking. For want of an established term, we will call such information
a tip. Tips are harder to use because of the need to ensure the correctness of the tip.


4 Butler Lampson, a computer scientist and Turing Award winner, provides two quotes: When in doubt, get rid of it (anonymous)
and Exterminate Features (Thacker).

---

## PDF page 91

64       Chapter 3 Fifteen implementation principles



    As a systems example, the Alto File system (Lampson, 1989) has every file block on disk carry a
pointer to the next file block. This pointer is treated as only a hint and is checked against the file name
and block number stored in the block itself. If the hint is incorrect, the information can be reconstructed
from disk. Incorrect hints must not jeopardize system correctness but result only in performance degra-
dation.

P10: Pass hints in protocol headers
For distributed systems, the logical extension to Principle P9 is to pass information such as hints in
message headers. Since this book deals with distributed systems, we will make this a separate principle.
For example, computer architects have applied this principle to circumvent inefficiencies in message-
passing parallel systems such as the Connection Machine.
    One of the ideas in active messages (Chapter 5) is to have a message carry the address of the
interrupt handler for fast dispatching. Another example is tag switching (Chapter 11), where packets
carry additional indices besides the destination address to help the destination address to be looked up
quickly. Tags are used as hints because tag consistency is not guaranteed; packets can be routed to the
wrong destination, where they must be checked.
