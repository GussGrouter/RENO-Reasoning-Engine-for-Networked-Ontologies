# network-algorithmics-14-12-2-augmented-data-structures (chunk 000006)

416      Chapter 14 Scheduling packets

range is (v0 , vm ] (with vk as the “middle point”) as just explained, and the height of is area is clearly
                           three fields in its left child L1 are L1 .area = (I ), L1 .range = (v0 , vk ], and
[1..m]. The values of these
L1 .height = [1..k]  ki=1 i . Those in its right child L2 are L2 .area = (I I ), L2 .range = (vk , vm ],
                                     
and L2 .height = [(k + 1)..m]  m      i=k+1 i . It is not hard to check that the three fields values of L0 ,
L1 , and L2 satisfy the following three equations:

L0 .area = L1 .area + L2 .area + |L2 .range| ∗ L1 .height,                       (14.5)
                                           L0 .height = L1 .height + L2 .height,                        (14.6)
                                                                   
                                            L0 .range = L1 .range     L2 .range.                        (14.7)
