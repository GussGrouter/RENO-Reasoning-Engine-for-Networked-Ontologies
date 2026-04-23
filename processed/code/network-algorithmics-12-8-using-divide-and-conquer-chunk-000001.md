# network-algorithmics-12-8-using-divide-and-conquer (chunk 000001)

# Network Algorithmics — 12.8 Using divide-and-conquer (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 342
- Slice: from `12.8 Using divide-and-conquer` up to next detected section heading

---

12.8 Using divide-and-conquer
The next three schemes (bit vector linear search, on-demand cross-producting, and equivalenced cross-
producting) all exploit the simple algorithmic idea (P15) of divide-and-conquer. Divide-and-conquer
refers to dividing a problem into simpler pieces and then efficiently combining the answers to the pieces.
We briefly motivate a skeletal framework of this approach in this section. The next three sections will
flesh out specific instantiations of this framework.
    Chapter 11 has already outlined techniques to do lookups on individual fields. Given this back-
ground, the common idea in all three divide-and-conquer algorithms is the following. Start by slicing
the rule database into columns, with the ith column storing all distinct prefixes (or ranges) in field i.
Then, given a packet P , determine the best-matching prefix (or narrowest-enclosing range) for each
of its fields separately. Finally, combine the results of the best-matching-prefix lookups on individual
fields. The main problem, of course, lies in finding an efficient method for combining the lookup of
individual fields into a single compound lookup.
    All the divide-and-conquer algorithms conceptually start by slicing the database of Fig. 12.2 into
individual prefix fields. In the sliced columns, from now on, we will sometimes refer to the wildcard
character ∗ by the string default. Recall that the mail gateway M and internal NTP agent T I are full
IP addresses that lie within the prefix range of N et. The sliced database corresponding to Fig. 12.2 is
shown in Fig. 12.10.
    Clearly, any divide-and-conquer algorithm starts by doing an individual lookup in each column and
then combines the results. The next three sections show that each of the three schemes returns different
results with lookup and follows different strategies to combine the individual field results, despite using
the same sliced database shown in Fig. 12.10.

316       Chapter 12 Packet classification

FIGURE 12.10
The database of Fig. 12.2 “sliced” into columns where each column contains the set of prefixes corresponding to a
particular field.
