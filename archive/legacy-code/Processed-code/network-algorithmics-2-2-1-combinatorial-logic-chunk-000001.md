# Chunk 000001

- Source: raw/code/pdf/Network.Algorithmics.pdf
- From: processed/code/network-algorithmics-2-2-1-combinatorial-logic.md

---
2.2.1 Combinatorial logic
Section A.2.1 in Appendix describes very simple models of basic hardware gates, such as NOT, NAND,
and NOR, that can be understood by even a software designer who is willing to read a few pages.
However, even knowing how basic gates are implemented is not required to have some insight into
hardware design.
    The first key to understanding logic design is the following observation. Given NOT, NAND, and
NOR gates, Boolean algebra shows that any Boolean function f (I1 , . . . , In ) of n inputs can be imple-
mented. Each bit of a multibit output can be considered a function of the input bits. Logic minimization
is often used to eliminate redundant gates and sometimes to increase speed. For example, if + denotes
OR and · denotes AND, then the function O = I1 · I2 + I1 · I2 can be simplified to O = I1 .

Example 1. Quality of Service and Priority Encoders: Suppose we have a network router that maintains
n output packet queues for a link, where queue i has higher priority than queue j if i < j . This problem
comes under the category of providing quality of service (QoS), which is covered in Chapter 14. The
transmit scheduler in the router must pick a packet from the first nonempty packet queue in priority
order. Assume the scheduler maintains an N -bit vector (bitmap) I such that I [ j ] = 1 if and only if
queue j is nonempty. Then the scheduler can find the highest-priority nonempty queue by finding the
smallest position in I in which a bit is set. Hardware designers know this function intimately as a
priority encoder. However, even a software designer should realize that this function is feasible for
hardware implementation for reasonable n. This function is examined more closely in Example 2.

2.2 Hardware     23
