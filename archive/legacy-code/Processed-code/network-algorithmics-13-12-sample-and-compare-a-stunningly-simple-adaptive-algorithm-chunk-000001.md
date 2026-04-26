# network-algorithmics-13-12-sample-and-compare-a-stunningly-simple-adaptive-algorithm (chunk 000001)

# Network Algorithmics — 13.12 Sample-and-compare: a stunningly simple adaptive algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 380
- Slice: from `13.12 Sample-and-compare: a stunningly simple adaptive algorithm` up to next detected section heading

---

13.12 Sample-and-compare: a stunningly simple adaptive algorithm
We start with the adaptive algorithm proposed in Tassiulas (1998), which we call sample-and-compare.
This algorithm is stunningly simple: at each time slot t, sample a (uniform) random matching (P3a)
denoted as R(t), compare its weight to that of the matching S(t − 1) used in the previous time slot, and
use the heavier matching as S(t) (i.e., for the current time slot t). Compared to the MWM algorithm,
the sample-and-compare algorithm has a much lower computational complexity of O(N ). Amazingly,
just like MWM, sample-and-compare can provably attain 100% throughput under all traffic patterns.
However, its delay performance is poor under heavy load, as explained by the following queueing
dynamics it experiences under heavy load.
    It can be shown that the current (i.e., at time t) normalized throughput of a switching algorithm
is roughly equal to the weight of S(t) as a fraction of that of MWM at time t. In particular, for any
switching algorithm to attain 100% throughput like sample-and-compare does, the weight of S(t) has to
eventually be very close to that of MWM. However, since only with a tiny probability can a (uniform)
random matching R(t) have a large enough weight to exceed that of S(t − 1) (that is already quite
large), the rate at which R(t) can “gain enough weight” under sample-and-compare to approach that of
MWM is extremely slow. Hence, the weight of S(t) can be much smaller than that of MWM for a long
time, during which the throughput of the switch is much smaller than 100%, and as a consequence, the
weights of the edges (VOQ lengths) become very large under a heavy load. This explains the poor delay
performance of sample-and-compare. When (almost) all edge weights become gigantic, however, the
weight of a random matching R(t) starts to have a decent probability of beating that of S(t − 1), and
the weight of S(t) starts to approach that of MWM much more rapidly. This explains why sample-and-
compare can attain 100% throughput at last.
