# Network Algorithmics — 16.6 Reducing counter width using approximate counting (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 491
- Slice: from `16.6 Reducing counter width using approximate counting` up to next detected section heading

---

16.6 Reducing counter width using approximate counting
The DRAM backing-store approach trades reduced counter widths for more processing and complexity.
A second approach is to trade accuracy and certainty (P3a, b) for reduced counter widths. For many
applications described earlier, approximate counters may suffice.
    The basic idea is as follows. If we increment a b-bit counter only with probability 1/c, then, when
the counter saturates, the expected number of counted events is 2b · c. Thus a b-bit randomized counter
can count c times more events than a deterministic version. But, once the notion of approximate count-
ing is accepted, it is possible to do better.
    Notice that, in the basic idea, the standard deviation (i.e., the expected value of the counter error)
is a few c’s, which is small at counter values c. Morris’s idea for randomized counting is to notice
that, for higher counter values, one can tolerate higher absolute values of the error. For example, if the
standard deviation is equal to the counter, the real value is likely to be within half to twice the value
determined by the counter. Allowing the error to scale with counter values in turn allows a smaller
counter width.
    To achieve this, Morris’s scheme increments a counter with nonconstant probability that depends
on counter value, so the expected error scales with counter size. Specifically, the algorithm increments
a counter with probability 1/2x , where x is the value of the counter. At the end, a counter value of x
represents an expected value of 2x . Thus, the number of bits required for such a counter is log log Max,
where Max is the maximum value required for the counter.
    While this is an interesting scheme, its high standard deviation and the need to pick accurate small
numbers, especially for high values of the counter, are clear disadvantages. Approximate counting is an
example of using P3b, trading accuracy for storage (and time).
