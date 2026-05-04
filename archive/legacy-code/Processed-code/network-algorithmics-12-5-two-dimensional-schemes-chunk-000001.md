# network-algorithmics-12-5-two-dimensional-schemes (chunk 000001)

# Network Algorithmics — 12.5 Two-dimensional schemes (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 331
- Slice: from `12.5 Two-dimensional schemes` up to next detected section heading

---

12.5 Two-dimensional schemes
A useful problem-solving technique is first to solve a simpler version of a complex problem such as
packet classification and to use the insight gained to solve the more complex problem. Since packet
classification with just one field has been solved in Chapter 11, the next simplest problem is two-
dimensional packet classification.
    Two-dimensional rules may be useful in their own right. This is because large backbone routers
may have a large number of destination–source rules to handle virtual private networks and multicast

12.5 Two-dimensional schemes               305

FIGURE 12.3
An example with seven destination–source rules.

forwarding and to keep track of traffic between subnets. Further, as we will see, there is a heuristic
observation that reduces the general case to the two-dimensional case.
    Since there are only three distinct approaches to one-dimensional prefix matching—using tries,
binary search on prefix lengths, and binary search on ranges—it is worth looking for generalizations of
each of these distinct approaches. All three generalizations exist. However, this chapter will describe
only the most efficient of these (the generalization of tries) in this section.
    The appropriate generalization of standard prefix tries to two dimensions is called the grid of tries.
The main idea will be explained using an example database of seven destination–source rules, shown
in Fig. 12.3. We arrive at the final solution by first considering two naive variants.
