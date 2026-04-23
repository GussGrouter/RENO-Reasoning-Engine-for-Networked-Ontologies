# network-algorithmics-3-3-2-modularity-with-efficiency (chunk 000002)

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
