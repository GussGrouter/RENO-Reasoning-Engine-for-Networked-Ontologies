# Network Algorithmics — summary (3.6) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 90 -l 116 -layout
- Slice: from `3.6 Summary` up to exercises/next chapter

---

3.6 Summary
This chapter introduced a set of principles for efficient system implementation. A summary can be
found in Figs. 3.1–3.3. The principles were illustrated with examples drawn from compilers, archi-
tecture, databases, algorithms, and networks to show broad applicability to computer systems. Chef
Charlie’s examples, while somewhat tongue in cheek, show that these principles also extend to general
systems, from restaurants to state governments. While the broad focus is on performance, cost is an
equally important metric. One can cast problems in the form of finding the fastest solution for a given
cost. Optimization of other metrics, such as bandwidth, storage, and computation, can be subsumed
under the cost metric.
    A preview of well-known networking applications of the 15 principles can be found in Figs. 3.1–3.3.
These applications will be explained in detail in later chapters. The first five principles encourage
systems thinking. The next five principles encourage a fresh look at system modularity. The last five
principles point to useful ways to speed up individual subsystems.
    Just as chess strategies are boring until one plays a game of chess, implementation principles are
lifeless without concrete examples. The reader is encouraged to try the following exercises, which
provide more examples drawn from computer systems. The principles will be applied to networks in
the remaining chapters. In particular, the next chapter seeks to engage the reader by providing a set of
15 self-contained networking problems to play with.
