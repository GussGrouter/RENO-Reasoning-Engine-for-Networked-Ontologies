# Network Algorithmics — 1.3 Exercise 1. Implementing chi-square: The chi-square statistic can be used to find if the overall set of observed (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 42
- Slice: from `1.3 Exercise 1. Implementing chi-square: The chi-square statistic can be used to find if the overall set of observed` up to next detected section heading

---

1.3 Exercise
1. Implementing chi-square: The chi-square statistic can be used to find if the overall set of observed
   character frequencies are unusually different (as compared to normal random variation) from the
   expected character frequencies. This is a more sophisticated test, statistically speaking, than the
   simple threshold detector used in the warm-up example. Assume that the thresholds represent the
   expected frequencies. The statistic is computed by finding the sum of
                                                            2
              ExpectedF requency [i] − ObservedF requency [i] /ExpectedF requency [i]

   for all values of character i. The chip should alarm if the final statistic is above a specified threshold.
   (For example, a value of 14.2 implies that there is only a 1.4% chance that the difference is due to
   chance variation.) Find a way to efficiently implement this statistic, assuming once again that the
   length is known only at the end.

This page intentionally left blank

                                                                                                             CHAPTER


Network implementation models
                                                                                                                 2
                       A rather small set of key concepts is enough. Only by learning the essence of each topic, and by
                  carrying along the least amount of mental baggage at each step, will the student emerge with a good
                                                                                  overall understanding of the subject.
                                                                                         —Carver Mead and Lynn Conway



To improve the performance of endnodes and routers, an implementor must know the rules of the
game. A central difficulty is that network algorithmics encompasses four separate areas: protocols,
hardware architectures, operating systems, and algorithms. Networking innovations occur when area
experts work together to produce synergistic solutions. But can a logic designer understand protocol
issues, and can a clever algorithm designer understand hardware trade-offs, at least without deep study?
    A useful dialog can begin with simple models that have explanatory and predictive power but with-
out unnecessary detail. At the least, such models should define terms used in the book; at best, such
models should enable a creative person outside an area to play with and create designs that can be
checked by an expert within the area. For example, a hardware chip implementor should be able to sug-
gest software changes to the chip driver, and a theoretical computer scientist should be able to dream
up hardware matching algorithms for switch arbitration. This is the goal of this chapter.
    The chapter is organized as follows. Starting with a model for protocols in Section 2.1, the im-
plementation environment is described in bottom-up order. Section 2.2 describes relevant aspects of
hardware protocol implementation, surveying logic, memories, and components. Section 2.3 describes
a model for endnodes and network devices such as routers. Section 2.4 describes a model for the rel-
evant aspects of operating systems that affect performance, especially in endnodes. To motivate the
reader and to retain the interest of the area expert, the chapter contains a large number of networking
examples to illustrate the application of each model.


    Quick reference guide
    Hardware designers should skip most of Section 2.2, except for Example 3 (design of a switch arbitrator), Example 4
    (design of a flow ID lookup chip), Example 5 (pin count limitations and their implications), and Section 2.2.5 (which
    summarizes three hardware design principles useful in networking). Processor and architecture experts should skip Sec-
    tion 2.3 except for Example 7 (network processors).
         Implementors familiar with operating systems should skip Section 2.4, except for Example 8 (receiver livelock as
    an example of how operating system structure influences protocol implementations). Even those unfamiliar with an area
    such as operating systems may wish to consult these sections if needed after reading the specific chapters that follow.




Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00007-5
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                          17

18       Chapter 2 Network implementation models
