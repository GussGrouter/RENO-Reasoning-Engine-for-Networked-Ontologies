# network-algorithmics-5-8-exercises-1-data-caches-and-copies-a-normal-data-cache-is-a-mapping-from (chunk 000001)

# Network Algorithmics — 5.8 Exercises 1. Data caches and copies: A normal data cache is a mapping from a memory location address to a (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 170
- Slice: from `5.8 Exercises 1. Data caches and copies: A normal data cache is a mapping from a memory location address to a` up to next detected section heading

---

5.8 Exercises
1. Data caches and copies: A normal data cache is a mapping from a memory location address to a
   piece of content. If the content is frequently accessed, then the content can be accessed directly from
   the fast cache instead of making a memory access. Assuming the cache is a write-back cache, even
   writes can be written to the cache instead of memory and only written to memory when the cache is
   overwritten. A modern cache block is fairly large (128 bits), with a mapping from a 32-bit address
   to 128 bits of data starting at that address.
   We want to address the copying problem where various modules (including the network and file
   system) copy data via intermediate buffers that are soon overwritten (e.g., socket buffer, application
   buffer). The chapter did so with software changes. Here we consider whether changing the hardware
   architecture can help without software changes such as IO-Lite, fbufs, and mmap.
   • Even an ordinary data cache may help remove some of the overhead when copying data from
     location L to location M. Explain why. (Assume that location M is a temporary buffer that is
     soon overwritten, as in a socket buffer. Assume that if only a single word is written in a large
     cache block, the remaining words can be marked invalid.) Intuitively, this problem is asking
     whether there is an equivalent of COW (used to reduce copying between virtual address spaces)
     in the world of data caches.
   • Now assume a different data cache design, where a cache is a mapping from one or more
     addresses to the same content. Thus a cache has changed from a one-to-one mapping to a many-
     to-one mapping. For example, assume a cache where two locations can point to the same content.
     Thus a cache entry may be (L, M, C), where L and M are addresses and C is the common con-

144      Chapter 5 Copying data
