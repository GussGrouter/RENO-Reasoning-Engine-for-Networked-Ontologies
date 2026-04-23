# network-algorithmics-8-8-exercises-1-other-uses-of-early-demultiplexing-besides-the-uses-of-early (chunk 000001)

# Network Algorithmics — 8.8 Exercises 1. Other Uses of Early Demultiplexing: Besides the uses of early demultiplexing already described, consider the following potential uses. (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 236
- Slice: from `8.8 Exercises 1. Other Uses of Early Demultiplexing: Besides the uses of early demultiplexing already described, consider the following potential uses.` up to next detected section heading

---

8.8 Exercises
1. Other Uses of Early Demultiplexing: Besides the uses of early demultiplexing already described,
   consider the following potential uses.
   • Quality of Service: Why might early demultiplexing help offer different qualities of service to
     different packets in an end system? Give an example.
   • Integrated Layer Processing: Integrated layer processing (ILP) was studied in Chapter 5. Discuss
     why early demultiplexing may be needed for ILP.
   • Specializing Code: Once the path of a protocol is known, one can possibly specialize the code for
     the path, just as DPF specializes the code for each node. Give an example of how path information
     could be exploited to create more efficient code.
2. Further DPF Optimizations: Besides the optimizations already described, consider the following
   other optimizations that DPF exploits.
   • Atom Coalescing: It often happens that a node in the DPF tree checks for two smaller field values
     in the same word. For example, the TCP node may check for a source port value and a destination
     port value. How can DPF do these checks more efficiently? What crucial assumption does this
     depend on, and how can DPF validate this assumption?
   • Optimizing Hash Tables: When DPF adds a classifier, it may update the hash table at the node.
     Unlike Pathfinder, the code can be specialized to the specific set of values in each hash table.
     Explain why this can be used to provide a more efficient implementation for small tables and for
     collision handling in some cases.

This page intentionally left blank

CHAPTER

Protocol processing
                                                                                                               9
                                                Household tasks are easier and quicker when they are done by somebody else.
                                                                                                           —James Thorpe
