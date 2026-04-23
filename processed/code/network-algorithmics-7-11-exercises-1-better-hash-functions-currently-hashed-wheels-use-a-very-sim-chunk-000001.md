# network-algorithmics-7-11-exercises-1-better-hash-functions-currently-hashed-wheels-use-a-very-sim (chunk 000001)

# Network Algorithmics — 7.11 Exercises 1. Better Hash Functions: Currently hashed wheels use a very simple and primitive hash function (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 220
- Slice: from `7.11 Exercises 1. Better Hash Functions: Currently hashed wheels use a very simple and primitive hash function` up to next detected section heading

---

7.11 Exercises
1. Better Hash Functions: Currently hashed wheels use a very simple and primitive hash function
   (low-order bits). Find a way to use your favorite hash function to do hashed wheels. (Hint: Consider

194      Chapter 7 Maintaining timers

working with absolute time and not relative time.) What particular aspect of performance of a timer
   module would a better hash function improve? (This idea is due to Travis Newhouse.)
2. Hierarchical Wheels Versus Hashed Wheels and Heaps: Current implementations of timing
   wheels use hashed wheels.
   • What is one possible advantage of hierarchical wheels over hashed wheels? Can you quantify the
     difference precisely?
   • Suppose we do hierarchical wheels by dividing a 32-bit timer into four chunks of 8 bits apiece.
     What is the difference between such a timing wheel and a 256-way d-heap? When might the
     heap be a better solution?

CHAPTER

Demultiplexing
                                                                                                             8
                  Biologically the species is the accumulation of the experiments of all its successful individuals since
                                                                                                           the beginning.
                                                                                                            —H.G. Wells
