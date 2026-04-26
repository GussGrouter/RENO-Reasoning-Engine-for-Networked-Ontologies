# network-algorithmics-13-10-avoiding-randomization-with-islip (chunk 000001)

# Network Algorithmics — 13.10 Avoiding randomization with iSLIP (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 374
- Slice: from `13.10 Avoiding randomization with iSLIP` up to next detected section heading

---

13.10 Avoiding randomization with iSLIP
Parallel iterative matching was a seminal scheme because it introduced the idea that pretty-good
bipartite matchings can be computed at reasonable computation and hardware costs with clever par-
allelization. Once that was done, just as was the case when Roger Bannister first ran the mile in under
four minutes, others could make further improvements. But, PIM has two potential problems. First,
it uses randomization, and it may be hard to produce a reasonable source of random numbers at very
high speeds.2 Second, it requires a logarithmic number of iterations to attain maximal matches. Given
that each of a logarithmic number of iterations takes three phases and that the entire matching decision
must be made within a minimum packet arrival time, it would be better to have a matching scheme that
comes close to maximal matchings in just one or two iterations.
    iSLIP is a very popular and influential scheme that essentially “derandomizes” PIM and also
achieves very close to maximal matches after just one or two iterations. The basic idea is extremely
simple. When an input port or an output port in PIM experiences multiple requests, it chooses a “win-
ning” request uniformly at random, for the sake of fairness. Whereas Ethernet provides fairness with
randomness, token rings do so using a round-robin pointer implemented by a rotating token.

2 One can argue that schemes like RED require randomness at routers, anyway. However, a poor-quality source of random
numbers in an RED implementation will be less noticeable than poor-quality random numbers within a switch fabric.

348      Chapter 13 Switching
