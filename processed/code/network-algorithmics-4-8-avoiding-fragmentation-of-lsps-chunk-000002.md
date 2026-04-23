# network-algorithmics-4-8-avoiding-fragmentation-of-lsps (chunk 000002)

Solution
If the individual fragments of the original LSP of R1 are to be propagated independently without hop-
by-hop reassembly, then each fragment must be a separate LSP by itself, with a separate sequence
number. This crucial observation leads to the following elegant idea.
    Modify the link state routing protocol to allow any router R1 to be multiple pseudorouters R1a ,
R1b , R1c (see Fig. 4.15). The original set of endnodes are divided among these pseudorouters, so the
LSP of each pseudorouter can fit into most data link frames without the need for fragmentation. For
example, if most data link sizes are at least 576 bytes, roughly 72 endnodes can fit within a data link
frame.
    How is this concept of a pseudorouter actually realized? In the original LSP propagation, each
router had a 6-byte ID that is placed in all LSPs sent by the router. To allow for pseudorouters, we
change the protocol to have LSPs carry a 7-byte ID (6-byte router ID + 1-byte pseudorouter ID). The
pseudorouter ID can be assigned by the actual router that houses all the pseudorouters. By allowing 256
pseudorouters per router, roughly 18,000 endnodes can be supported per router.
    While the LSP propagation treats pseudorouters separately, it is crucial that route computation treat
the separate pseudorouters as one router. After all, the endnodes are all directly connected to R1 in our
example. But this is easily done because all the LSPs with the same first 6 bytes can be recognized as
being from the same router.
    In summary, the main idea is to shift computation in space (P3c) by having the source fragment the
original LSP into independent LSPs instead of having each data link do the fragmentation. This is a

92        Chapter 4 Principles in action

FIGURE 4.15
Avoiding hop-by-hop fragmentation by dividing a large router into pseudorouters.

good example of systems thinking. Needless to say, the implementors liked this solution (invented by
Radia Perlman) much better than the original approach.

Exercises

• How can a router assign endnodes to pseudorouters? What happens if a router initially has a lot of
  endnodes (and hence a lot of pseudorouters) and then most of the endnodes die? This can leave a lot
  of pseudorouters, each of which has only a few endnodes. Why is this bad, and how can it be fixed?
• As in the relaxed-consistency examples described in Chapter 3, this solution can lead to some un-
  expected (but not very serious) temporary inconsistencies. Assuming a solution to the previous
  exercise, describe a scenario in which a given router, say, R2, can find (at some instant) that its
  LSP database shows the same endnode (say, E1) belonging to two pseudorouters, R1a and R1c .
  Why is this no worse than ordinary LSP routing?
