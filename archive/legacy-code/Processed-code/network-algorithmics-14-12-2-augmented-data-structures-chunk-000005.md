# network-algorithmics-14-12-2-augmented-data-structures (chunk 000005)

Detailed data structure design
We now describe the shape data structure. We do so recursively, since its base data structure, a balanced
binary search tree, is best explained recursively. The shape data structure, corresponding to the staircase
shown in Fig. 14.21(a), is shown in Fig. 14.21(b) with the details of the two top levels expanded and
the rest abbreviated. As explained earlier, the (entire) tree rooted by L0 contains m leaf nodes with
key values v1 , v2 , v3 , · · · , vm , respectively. Hence the (key) range of the root node L0 is (v0 , vm ] with
vk as the “middle” point of the range. This vk is roughly the “would-have-been” middle point in the
following sense: Had this tree been a usual binary balanced search tree in which every node, internal or
leaf, is associated with a key value, the root node L0 would have been associated with the key value vk ,
or something “close” in the rank order (e.g., vk−2 ).
     We now proceed to the next level of the tree. The range of its left child node L1 is (v0 , vk ], and
hence the left subtree contains k leaf nodes with key values v1 , v2 , ..., vk . The range of its right child
node L2 is (vk , vm ], and hence the right subtree contains m − k leaf nodes with key values vk+1 , vk+2 ,
..., vm . We do not name a middle point for either range since there are no such details in Fig. 14.21(b)
anyway. With this middle point field, the binary search over the binary search tree is straightforward:
compare the search key with the middle point (e.g., vk at L0 ), and then continue the search in either the
left or the right subtree accordingly.
     Now, we describe the three “augmentation” data fields in the shape data structure. To do so, we first
describe a specific objective we would like to achieve. The union of the solid-line-enclosed regions
(IV) and (V) corresponds to the shape information maintained at the root. We want to know if its area
is smaller or larger than t − t0 , the amount of real time that has elapsed since the last time the function
V (·) is evaluated (at time t0 ); the “equal to” case is trivial so we ignore it here and in the subsequent
discussions. The search shall continue in the left subtree in the case of “smaller than,” and in the right
subtree otherwise. While it may sound natural to include the quantity (IV) + (V) as a new data field,
from a data structure and algorithm design point of view, this quantity is hard to maintain in event
of the insertion or deletion of a leaf node. Instead, we maintain two other quantities from which this
quantity can be readily (i.e., in O(1) time) calculated. One such quantity is the area of the solid-line-
enclosed region (I), which is denoted W in the original paper (Valente, 2004). The other is the height
of the
      staircase, which is the total weight of flows F 1, F 2, ..., F k and hence is denoted as [1..m]
( m   i=1 i ) in Fig. 14.21(b). With a slight abuse of notation, we denote the area of region (IV) also
as (IV), and the area of region (I) also as (I), and so on. With this notational abuse, the relationship
between these three quantities ((I V ), [1..m], and (I )) is (I V ) = (vk − v0 ) ∗ [1..m] − (I ).
     The values of the base data structure field (key) range and the two augmented data structure fields
area and height, for the tree nodes L0 , L1 , and L2 , are shown in Fig. 14.21(b). The area associated
with the root node is L0 .area = (I ) + (I I ) + (I I I ). This area is used to calculate the area (VI) + (V),
which t − t0 should be compared against first (before it is compared against (I V ) if at all). Its (key)
