# network-algorithmics-17-2-approximate-string-matching (chunk 000002)

detecting whether two or more sets of characters, say, “abcef” and “abfecd,” are similar is by computing
their resemblance (Broder, 1998).
    The resemblance of two sets of characters is the ratio of the size of their intersection to the size
of their union. Intuitively, the higher the resemblance, the higher the similarity. By this definition, the
resemblance of “abcef” and “abfecd” is 5/6 because they have five characters in common.
    Unfortunately, resemblance per se does not take into account order, so “abcef” completely resembles
“fecab.” One way to fix this is to rewrite the sets with order numbers attached so that “abcef” becomes
“1a2b3c4e5f” while “fecab” now becomes “1f2e3c4a5b.” The resemblance, using pairs of characters
as set elements instead of characters, is now nil. Another method that captures order in a more relaxed
manner is to use shingles (Broder, 1998) by forming the two sets to be compared using as elements all
possible substrings of size k of the two sets.
    Resemblance is a nice idea, but it also needs a fast implementation. A naive implementation requires
sorting both sets, which is expensive and takes large storage. Broder’s idea (Broder, 1998) is to quickly
compare the two sets by computing a random (P3a, trade certainty for time) permutation on two sets.
For example, the most practical permutation function on integers of size at most m − 1 is to compute
P (X) = ax + b mod m, for random values of a and b and prime values of the modulus m.
    For example, consider the two sets of integers {1, 3, 5} and {1, 7, 3}. Using the random permutation
{3 x + 5 mod 11}, the two sets become permuted to {8, 3, 9} and {8, 4, 3}. Notice that the minimum
values of the two randomly permuted sets (i.e., 3) are the same.
    Intuitively, it is easy to see that the higher the resemblance of the two sets, the higher the chance
that a random permutation of the two sets will have the same minimum. Formally, this is because the
two permuted sets will have the same minimum if and only if they contain the same element that gets
mapped to the minimum in the permuted set. Since an ideal random permutation makes it equally likely
for any element to be the minimum after permutation, the more elements the two sets have in common,
the higher the probability that the two minimums match.
    More precisely, the probability that two minimums match is equal to the resemblance. Thus one way
to compute the resemblance of two sets is to use some number of random permutations (say, 16) and
compute all 16 random permutations of the two sets. The fraction of these 16 permutations in which
the two minimums match is a good estimate of the resemblance.
    This idea was used by Broder (1998) to detect the similarity of Web documents. However, it is
also quite feasible to implement at high link speeds. The chip must maintain, say, 16 registers to keep
the current minimum using each of the 16 random hash functions. When a new character is read, the
logic permutes the new character according to each of the 16 functions in parallel. Each of the 16 hash
results is compared in parallel with the corresponding register, and the register value is replaced if the
new value is smaller.
    At the end, the 16 computed minima are compared in parallel against the 16 minima for the target
set to compute a bitmap, where a bit is set for positions in which there is equality. Finally, the number
of set bits is counted and divided by the size of the bitmap by shifting left by 4 bits. If the resemblance
is over some specified threshold, some further processing is done.
    Once again, the moral of this section is not that computing the resemblance is the solution to all
problems (or in fact to any specific problem at this moment) but that fairly complex functions can be
computed in hardware using multiple hash functions, randomization, and parallelism. Such solutions
exhibit the interplay of Principles P5 (use parallel memories) and Principle P3a (use randomization).
