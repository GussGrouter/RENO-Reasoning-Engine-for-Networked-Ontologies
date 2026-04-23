# network-algorithmics-16-4-1-motivation-and-design-objectives (chunk 000005)

ai,1 , . . . , ai,d , respectively (i.e., Ci,j = Aj [ai,j ]). For example, as shown in Fig. 16.5(B), C5 is spread
across A3 [1] = 10, A2 [2] = 11, and A1 [5] = 11011.
     An index bitmap I is maintained for each bucket. I is divided into p − 1 parts, I1 , . . . , Ip−1 , with
a one-to-one correspondence to the subcounter arrays A1 , . . . , Ap−1 , respectively. Each part Ij is a
bitmap with kj bits, Ij [1], . . . , Ij [kj ], one bit Ij [a] for each entry Aj [a] in Aj . Each Ij [a] is used
to determine if the counter stored in Aj [a] has expanded beyond the j th subcounter array. Ij is also
used to compute the index location of Ci in the next subcounter array Aj +1 . Because a counter cannot
expand beyond the last sub-counter array, there is no need for an index bitmap component for the
most significant subcounter array Ap . For example, consider the entries A1 [1] and A1 [5] where the
corresponding counter has expanded beyond A1 . This is indicated by having the corresponding bit
positions I1 [1] and I1 [5] set to 1, as shown in shaded boxes in Fig. 16.5(B). All remaining bit positions
in I1 are set to 0, as shown in clear boxes.
     For each counter that has expanded beyond A1 , an arrow is shown in Fig. 16.5(B) that links a
subcounter in A1 with the corresponding subcounter entry in A2 . For example, for C5 , its subcounter
entry A1 [5] in A1 is linked to the subcounter entry A2 [2] in A2 . Rather than expending memory to store
these links explicitly, which could vanish savings gained by reduced counter widths, we dynamically
compute the location of a subcounter in the next subcounter array Aj +1 based on the current bitmap
Ij . In this way no memory space is needed to store link pointers. This dynamic computation can be
readily determined using an operation called rank(s, j ), which returns the number of ones only in the
range s[1] . . . s[j ] in the bit-string s (similar to the rank operator defined in Jacobson (1989)). The
rank operator in turn can be efficiently computed in software using the aforementioned popcount(s)
instruction, which returns the number of ones in the bit-string s.

Handling increments
The increment operation is also based on the traversal of subcounters using rank indexing. We will
first describe the basic idea by means of an example. Consider the counter C2 in Fig. 16.5(B). Its
count is 31, which can be encoded in just the subcounter array A1 with C2,1 = 11111. Suppose we
want to increment C2 . We first increment its first subcounter component C2,1 = 11111, which results
in C2,1 = 00000 with a carry propagation to the next level. This is depicted in Fig. 16.5(C).
    This carry propagation triggers the increment of the next subcounter component C2,2 . The location
of C2,2 can be determined using rank indexing (i.e. rank(I1 , 2) = 2). However, the location of A2 [2] was
previously occupied by counter C5 . To maintain rank ordering, we have to shift the entries in A2 down
by one to free up the location A2 [2]. This is achieved by applying an operation called varshift(s, j, c),
which performs a right shift on the substring starting at bit-position j by c bits (with vacant bits filled
by zeros). The varshift operator can be readily implemented in most processors by means of shift and
bitwise logical instructions.
