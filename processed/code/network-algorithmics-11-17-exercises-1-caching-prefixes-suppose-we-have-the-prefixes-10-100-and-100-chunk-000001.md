# network-algorithmics-11-17-exercises-1-caching-prefixes-suppose-we-have-the-prefixes-10-100-and-100 (chunk 000001)

# Network Algorithmics — 11.17 Exercises 1. Caching Prefixes: Suppose we have the prefixes 10*, 100*, and 1001*. Hugh Hopeful would like (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 318
- Slice: from `11.17 Exercises 1. Caching Prefixes: Suppose we have the prefixes 10*, 100*, and 1001*. Hugh Hopeful would like` up to next detected section heading

---

11.17 Exercises
1. Caching Prefixes: Suppose we have the prefixes 10*, 100*, and 1001*. Hugh Hopeful would like
   to cache prefixes instead of entire 32-bit addresses. Hugh’s scheme keeps a set of prefixes in the
   cache (fast memory), in addition to the complete set of prefixes in slow memory. Hugh’s scheme
   first does a best-matching-prefix search in the cache; if a matching prefix is found, the next hop
   of the prefix is used. If no matching prefix is found, a best-matching-prefix search is done for the
   entire database and the resulting prefix cached. Periodically, prefixes that have not been matched
   for a while are flushed from the cache. Alyssa P. Hacker quickly gives Hugh a counterexample to
   show him that his scheme is flawed and that caching prefixes are tricky (if not impossible). Can
   you?
2. Encoding Prefixes in a Constant Length: We said in the text that encoding prefixes like 10*,
   100*, and 1000* in a fixed length could not be done by padding prefixes with zeroes. It clearly can
   be done by padding with zeroes and adding an encoding of the prefix length. We want to study a
   more efficient method.
   • How many possible prefixes on 32 bits can there be?
   • Show how to encode all such prefixes using a fixed length of 33 bits. Make sure that 10*, 100*,
     and 1000* encode to different values.
   • Can you use this fixed-length encoding of prefixes to have the multiple hash tables used in
     Section 11.11 be packed into a single hash table? Why might this help to decrease the chances
     of hash collisions for a given memory size?
3. Quantifying the Benefits of Compressing One-Way Branches:
   • For a unibit trie that does not compress one-way branches, show that the maximum number of
     trie nodes can be O(N · W ), where N is the number of prefixes and W is the maximum prefix
     length. (Hint: Generate a trie that uses log2 N levels to generate N nodes, and then hang a long
     string of N − W nodes from each of the N nodes.)
   • Show that a unibit trie with text strings to compress one-way branches can have at most 2N trie
     nodes and 2N text strings.
   • Extend your analysis to multibit trie nodes with a fixed stride. How would you implement text
     string compression in such tries?
4. Controlled Prefix Expansion: Code up an efficient algorithm that expands a set of prefixes to
   any target set of lengths L1 , . . . , Lk . Check your algorithm using the sample database of Fig. 11.6.
   What is the complexity of your algorithm?
5. Optimal Variable-Stride Trie: Prove that the varied-stride trie of Fig. 11.8 is optimal for a trie
   height of 2. Use the recursive formulation shown in the text.
6. Reducing Memory References in Lulea: The naive approach to counting bits shown in Fig. 11.13
   should take three memory references (to access numSet, to read the appropriate chunk of the
   bitmap, and to access the compressed trie node for the actual information.) Show how to use
   P4a to combine the first two accesses into a single access.
7. Next Node versus Leaf Pushing in Lulea: Before we applied Lulea compression, we first leaf
   pushed the expanded trie of Fig. 11.7. The motivation was to make every entry either a pointer or
   a prefix but not both. Suppose we have a special prefix entry at the top of every trie node; if any
