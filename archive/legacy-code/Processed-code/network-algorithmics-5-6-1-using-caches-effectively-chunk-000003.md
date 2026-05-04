# network-algorithmics-5-6-1-using-caches-effectively (chunk 000003)

5.6 Broadening beyond data manipulations                        139

FIGURE 5.12
The figure on the left shows networking code that is laid out in memory so that frequently used (white) and infre-
quently used (black) code is arbitrarily intermixed. Using a direct-mapped cache of half the size of the total code
can lead two frequently used instructions, such as X and Y , to collide. This problem can be avoided by relocating all
frequently used code to be contiguous, as shown on the right.

Code arrangement
It is hard to realize when one is writing networking code that the actual layout of code in memory (and
hence in the I-cache) is a degree of freedom that can be exploited (P13) with some effort. The key idea
in code arrangement (Mosberger et al., 1996) is to lay out code in memory to optimize the common
case (P11) such that commonly used code fits in the I-cache and the effort of loading the I-cache is not
wasted.
     At first glance, this seems to require no extra work. Since a cache should favor frequently used code
over infrequently used code, this should happen automatically. Unfortunately, this is incorrect because
of the following two aspects of the way I-caches are implemented.
• Direct mapping: An I-cache is a mapping of memory addresses to contents; the mapping is usually
  implemented by a simple hash function that optimizes for the case of sequential access. Thus most
  processors use direct-mapped I-caches, where the low-order bits of a memory address are used to
  index the I-cache array. If the high-order bits match, the contents are returned directly from cache;
  otherwise, a Read to memory is done across the bus, and the new data value and high-order bits are
  stored in the same location.
  Fig. 5.12 shows the effect of this implementation artifact. The figure on the left shows the memory
  layout of code for two networking functions, with black code denoting infrequently used code. Since
  the I-cache size is only half the total size of the code, it is possible for two frequently accessed lines
  of code (such as X and Y , with addresses that are the same modulo the I-cache size) to map to the
  same location in the I-cache. Thus if both X and Y are used to process every packet, they will keep
  evicting each other from the cache even though they are both frequently used.

140      Chapter 5 Copying data
