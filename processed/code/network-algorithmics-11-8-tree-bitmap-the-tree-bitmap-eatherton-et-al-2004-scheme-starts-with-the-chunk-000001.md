# network-algorithmics-11-8-tree-bitmap-the-tree-bitmap-eatherton-et-al-2004-scheme-starts-with-the (chunk 000001)

# Network Algorithmics — 11.8 Tree bitmap The tree bitmap (Eatherton et al., 2004) scheme starts with the goal of achieving the same storage (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 298
- Slice: from `11.8 Tree bitmap The tree bitmap (Eatherton et al., 2004) scheme starts with the goal of achieving the same storage` up to next detected section heading

---

11.8 Tree bitmap
The tree bitmap (Eatherton et al., 2004) scheme starts with the goal of achieving the same storage
and speed as the Lulea scheme, but it adds the goal of fast insertions. While we have argued that fast

272       Chapter 11 Prefix-match lookups

FIGURE 11.14
The tree bitmap scheme allows the compression of Lulea without sacrificing fast insertions by using two bitmaps per
node. The first bitmap describes valid versus null pointers, and the second describes internally stored prefixes.

insertions are not as important as fast lookups, they clearly are desirable. Also, if the only way to handle
an insertion or deletion is to rebuild the Lulea-compressed trie, then a router must keep two copies of
its routing database, one that is being built and one that is being used for lookups. This can potentially
double the storage cost from 32 bits per prefix to 64 bits per prefix. This in turn can halve the number
of prefixes that can be supported by a chip that places the entire database in on-chip SRAM.
     To obtain fast insertions and hence avoid the need for two copies of the database, the first problem
in Lulea that must be handled is the use of leaf pushing. When a prefix of a small length is inserted,
leaf pushing can result in pushing down the prefix to a large number of leaves, making insertion slow.
