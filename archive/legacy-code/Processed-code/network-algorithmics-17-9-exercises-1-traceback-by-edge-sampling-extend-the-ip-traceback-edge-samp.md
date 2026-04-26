# Network Algorithmics — 17.9 Exercises 1. Traceback by edge sampling: Extend the IP traceback edge-sampling idea to reduce the space (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 538
- Slice: from `17.9 Exercises 1. Traceback by edge sampling: Extend the IP traceback edge-sampling idea to reduce the space` up to next detected section heading

---

17.9 Exercises
1. Traceback by edge sampling: Extend the IP traceback edge-sampling idea to reduce the space
   required. As described in the text, try to do this by chopping the node ID required in the base
   scheme into smaller (say, 8-bit) fragments. It may help to consider each of the fragment IDs to be
   the IDs of four virtual nodes that are housed in a single physical node, thus effectively extending the
   path and the number of samples needed for reconstruction.
2. Bloom filters and trajectory sampling: Can you use Bloom filters to improve the label storage
   required by trajectory sampling in Chapter 16? Explain.
3. Sampling and packet logging: Can you use packet sampling to reduce the amount of memory
   required by the logging traceback solution? What are the disadvantages and advantages?
4. Traceback by packet logging: Why does the implementation in Fig. 17.8 go through the indirection
   of a hash to 32 bits (as in trajectory sampling) and then to a Bloom filter?

512      Chapter 17 Network security



5. Aho–Corasick as a state machine: In many applications one may wish to ignore certain padding
   characters that can be inserted by an intruder to make strings hard to detect. How might you extend
   Aho–Corasick to ignore these padding characters while searching for suspicious strings?
6. Resemblance and min-wise hashing: Generalize the Broder methods to approximately search for
   multiple strings and return the string with the highest resemblance.
7. Approximate matching and worm detection: Could the methods for approximate search general-
   ize to detecting worms that mutate?

                                                                                                            CHAPTER


Conclusions
                                                                                                    18
                                                                           The end of a matter is better than its beginning.
                                                                                                 —Ecclesiastes, The Bible



We began the book by setting up the rules of the network algorithmics game. The second part of the
book dealt with server implementations and the third part with router implementations. The fourth and
last part of the book dealt with current and future issues in measurement and security.
    The book covers a large number of specific techniques and a variety of settings, there are techniques
for fast server design versus techniques for fast routers, techniques specific to operating systems versus
techniques specific to hardware. While all these topics are part of the spectrum of network algorithmics,
there is a risk that the material can appear to degenerate into a patchwork of assorted topics that are not
linked together in any coherent way.
    Thus as we draw to a close, it is appropriate to try and reach closure by answering the following
questions in the next four sections.
• What has the book been about? What were the main problems, and how did they arise? What are
  the main techniques? While endnode and router techniques appear to be different when considered
  superficially, are there some underlying characteristics that unite these two topics? Can these unities
  be exploited to suggest some cross-fertilization between these areas? (Section 18.1)
• What is network algorithmics about? What is the underlying philosophy behind network algorith-
  mics, and how does it differ from algorithms by themselves? (Section 18.2)
• Is network algorithmics used in real systems? Are the techniques in this book exercises in specula-
  tion, or are there real systems that use some of these techniques? (Section 18.3)
• What is the future of network algorithmics? Are all the interesting problems already solved? Are
  the techniques studied in this book useful only to understand existing work or to guide new imple-
  mentations of existing tasks? Or are there always likely to be new problems that will require fresh
  applications of the principles and techniques described in this book? (Section 18.4)
