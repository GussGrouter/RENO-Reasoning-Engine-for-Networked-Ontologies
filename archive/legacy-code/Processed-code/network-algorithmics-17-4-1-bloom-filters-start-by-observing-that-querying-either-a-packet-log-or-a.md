# Network Algorithmics — 17.4.1 Bloom filters Start by observing that querying either a packet log or a table of allowed users is a set membership (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 528
- Slice: from `17.4.1 Bloom filters Start by observing that querying either a packet log or a table of allowed users is a set membership` up to next detected section heading

---

17.4.1 Bloom filters
Start by observing that querying either a packet log or a table of allowed users is a set membership
query, which is easily implemented by a hash table. For example, in a different security context, if John
and Cathy are allowed users and we wish to check if Jonas is an allowed user, we can use a hash table
that stores John and Cathy’s IDs but not Jonas.
    Checking for Jonas requires hashing Jonas’s ID into the hash table and following any lists at that
entry. To handle collisions, each hash table entry must contain a list of IDs of all users that hash into
that bucket. This requires at least W bits per allowed user, where W is the length of each user ID. In
general, to implement a hash table for a set of identifiers requires at least W bits per identifier, where
W is the length of the smallest identifier.
    Bloom filters (Bloom, 1970), shown in Fig. 17.7, allow one to reduce the amount of memory for set
membership to a few bits per set element. The idea is to keep a bitmap of size, say, 5N , where N is the
number of set elements. Before elements are inserted, all bits in the bitmap are cleared.
    For each element in the set, its ID is hashed using k independent hash functions (two in Fig. 17.7,
H 1 and H 2) to determine bit positions in the bitmap to set. Thus in the case of a set of valid users
in Fig. 17.7 ID John hashes into the second and next-to-last bit positions. ID Cathy hashes into one

502      Chapter 17 Network security



position in the middle and also into one of John’s positions. If two IDs hash to the same position, the
bit remains set.
    Finally, when searching to see if a specified element (say, Jonas) is in the set, Jonas is hashed using
all the k hash functions. Jonas is assumed to be in the set if all the bits hashed into by Jonas are set.
Of course, there is some chance that Jonas may hash into the position already set by, say, Cathy and
one by John (see Fig. 17.7). Thus there is a chance of what is called a false positive: answering the
membership query positively when the member is not in the set.
    Notice that the trick that makes Bloom filters possible is relaxing the specification (P3). A normal
hash table, which requires W bits per ID, does not make errors! Reducing to 5 bits per ID requires
allowing errors; however, the percentage of errors is small. In particular, if there is an attack tree and
set elements are hashed packet values, as in Fig. 17.6, false positives mean only occasionally barking
up the wrong tree branch(es).
    More precisely, the false-positive rate for an m-size bitmap to store n members using k hash func-
tions is
                                                    k              k
                                   1 − (1 − 1/m)kn ≈ 1 − e−kn/m

The equation is not as complicated as it may appear: (1 − 1/m)kn is the probability that any bit is not
set, given n elements that each hashes k times to any of m bit positions. Finally, to get a false positive,
all of the k bit positions hashed onto by the ID that causes a false positive must be set.
    Using this equation, it is easy to see that for k = 3 (three independent hash functions) and 5 bits per
member (m/n = 5), the false-positive rate is roughly 1%. The false-positive rate can be improved up to
a point by using more hash functions and by increasing the bitmap size.
