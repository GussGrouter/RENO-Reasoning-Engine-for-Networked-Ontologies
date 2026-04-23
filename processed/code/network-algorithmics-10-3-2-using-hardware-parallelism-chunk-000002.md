# network-algorithmics-10-3-2-using-hardware-parallelism (chunk 000002)

The idea is to have a logarithmic number of processing stages, each with its own memory array.
In Fig. 10.4 the keys are the characters A through H . The first array has only the root of the trie,
the median element E. The second array corresponds to the quartile and third quartile elements C
and G, which are the possible keys at the second probe of binary search, and so on. Search keys
enter from the left and progress from stage to stage, carrying a pointer that identifies which key in the
corresponding stage memory must be compared to the search key. The lookup throughput is nearly one
per memory access because there can be multiple concurrent searches progressing through the stages
in order.
    Although the figure shows the elements in, say, Stage 2, C and G, as being separated by their spacing
in the original table, they can be packed together to save memory in the stages. Thus the overall memory
across all stages becomes equal to the memory in a nonpipelined implementation. Indexing into each
stage memory becomes slightly more tricky.
    Assume Stage i has passed a pointer j to Stage j + 1 along with search key S. Stage j + 1 compares
the search key S to its j th array entry. If the answer is equal, the search is finished but continues flowing
through the pipeline with no more changes. If the search key is smaller, the search key is passed to stage
i + 1 with the pointer j 0 (i.e., j concatenated with bit 0); if the search key is larger, the pointer passed
is j 1. For example, if the key searched for is F , then the pointer becomes 1 when entering Stage 2 and
becomes 10 when entering Stage 3.
    The author first heard of this idea from Greg Waters, who later went on to implement IP lookups
for the core router company Avici. While the idea looks clever and arcane, there is a much simpler way
of understanding the final solution. Computer scientists are well aware of the notion of a binary search
tree (Cormen et al., 1990). Any binary search table can be converted into a fully balanced binary search
tree by making the root the median element, and so on, along the lines of Fig. 10.4. Any tree is trivially
pipelined by height, with nodes of height i being assigned to Stage i.
    The only problem with a binary search tree, as opposed to a table, is the extra space required for
pointers to children. However, it is well known that for a full binary search tree, such as a heap (Cormen
et al., 1990), the pointers can be implicit and can be calculated based on the history of comparisons,
as shown earlier. The upshot is that a seemingly abstruse trick can be seen as the combination of three
simple and well-known facts from theoretical computer science.
