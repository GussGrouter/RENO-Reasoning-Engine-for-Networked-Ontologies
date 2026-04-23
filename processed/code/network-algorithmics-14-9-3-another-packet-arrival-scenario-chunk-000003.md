# network-algorithmics-14-9-3-another-packet-arrival-scenario (chunk 000003)

We now “prove by induction” that the definition of V (·) in (14.4) is consistent with that of virtual
time, as just stated. Assume the value of V (ti−1 ) is equal to the virtual time corresponding
                                                                                               to real time
ti−1 . Then, during interval [ti−1 , ti ], the total weight of the backlogged flows is j ∈B(ti−1 ) φj . Since
ti−1 + τ ∈ [ti−1 , ti ] for any 0 ≤ τ ≤ ti − ti−1 , we obtain (14.4) by the definition of the GPS policy (as
bit-by-bit round-robin).
