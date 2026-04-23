# network-algorithmics-3-7-exercises-1-batching-disk-locality-and-logs-most-serious-databases-use-l (chunk 000004)

The previous chapter outlined 15 principles for efficient network protocol implementation. Part 2 of the
book begins a detailed look at specific network bottlenecks such as data copying and control transfer.
While the principles are used in these later chapters, the focus of these later chapters is on the specific
bottleneck being examined. Given that network algorithmics is as much a way of thinking as it is a
set of techniques, it seems useful to round out Part 1 by seeing the principles in action on small, self-
contained, but nontrivial network problems.
    Thus this chapter provides examples of applying the principles in solving specific networking prob-
lems. The examples are drawn from real problems, and some of the solutions are used in real products.
Unlike subsequent chapters, this chapter is not a collection of new material followed by a set of exer-
cises. Instead, this chapter can be thought of as an extended set of exercises.
    In Sections 4.1 to 4.15 15 problems are motivated and described. Each problem is followed by a
hint that suggests specific principles, which is then followed by a solution sketch. There are also a few
exercises after each solution. In classes and seminars on the topic of this chapter, the audience enjoyed
inventing solutions by themselves (after a few hints were provided), rather than directly seeing the final
solutions.

Quick reference guide
    In an ideal world, each problem should have something interesting for every reader. For those readers pressed for time,
    however, here is some guidance. Hardware designers looking to sample a few problems may wish to try their hand at
    designing an Ethernet monitor (Section 4.4) or doing a binary search on long identifiers (Section 4.14). Systems people
    looking for examples of how systems thinking can finesse algorithmic expertise may wish to tackle a problem on applica-
    tion device channels (Section 4.1) or a problem on compressing the connection table (Section 4.11). Algorithm designers
    may be interested in the problem of identifying a resource hog (Section 4.10) and a problem on the use of protocol design
    changes to simplify an implementation problem in link state routing (Section 4.8).

Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00009-9
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                            75

76        Chapter 4 Principles in action
