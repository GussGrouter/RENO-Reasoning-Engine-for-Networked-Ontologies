# network-algorithmics-17-4-1-bloom-filters-start-by-observing-that-querying-either-a-packet-log-or-a (chunk 000002)

The equation is not as complicated as it may appear: (1 − 1/m)kn is the probability that any bit is not
set, given n elements that each hashes k times to any of m bit positions. Finally, to get a false positive,
all of the k bit positions hashed onto by the ID that causes a false positive must be set.
    Using this equation, it is easy to see that for k = 3 (three independent hash functions) and 5 bits per
member (m/n = 5), the false-positive rate is roughly 1%. The false-positive rate can be improved up to
a point by using more hash functions and by increasing the bitmap size.
