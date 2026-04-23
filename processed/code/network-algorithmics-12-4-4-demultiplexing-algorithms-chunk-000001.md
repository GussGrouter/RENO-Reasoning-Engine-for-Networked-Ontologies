# network-algorithmics-12-4-4-demultiplexing-algorithms (chunk 000001)

# Network Algorithmics — 12.4.4 Demultiplexing algorithms (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 330
- Slice: from `12.4.4 Demultiplexing algorithms` up to next detected section heading

---

12.4.4 Demultiplexing algorithms
Chapter 8 describes the use of packet rules for demultiplexing and algorithms such as Pathfinder,
Berkeley packet filter, and dynamic path finder. Can’t these existing solutions simply be reused? It
is important to realize that the two problems are similar but subtly different.
    The first packet-classification scheme that avoids a linear search through the set of rules is Pathfinder
(Bailey et al., 1994). However, Pathfinder allows wildcards to occur only at the end of a rule. For
instance, (D, S, ∗, ∗, ∗) is allowed, but not (D, ∗, P rot, ∗, SourceP ort). With this restriction, all rules
can be merged into a generalized trie—with hash tables replacing array nodes—and rule lookup can be
done in time proportional to the number of packet fields. DPF (Engler and Kaashoek, 1996) uses the
Pathfinder idea of merging rules into a trie but adds the idea of using dynamic code generation for extra
performance. However, it is unclear how to handle intermixed wildcards and specified fields, such as
(D, ∗, P rot, ∗, SourceP ort), using these schemes.
    Because packet classification allows more general rules, the Pathfinder idea of using a trie does not
work well. There does exist a simple trie scheme (set-pruning tries; see Section 12.5.1) to perform a
lookup in time O(M), where M is the number of packet fields. Such schemes are described in Decasper
et al. (1998) and Malan and Jahanian (1998). Unfortunately, such schemes require (N K ) storage,
where K is the number of packet fields and N is the number of rules. Thus such schemes are not
scalable for large databases. By contrast, some of the schemes we will describe require only O(N M)
storage.
