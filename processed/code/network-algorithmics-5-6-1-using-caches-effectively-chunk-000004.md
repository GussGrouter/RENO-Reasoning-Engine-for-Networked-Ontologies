# network-algorithmics-5-6-1-using-caches-effectively (chunk 000004)

• Multiple instructions per block: Many I-caches can be thought of as an array of blocks, where
  multiple instructions (say, eight) are stored in a block. Thus when an instruction is fetched, all eight
  instructions in the same block are also fetched on the assumption of spatial locality: With sequential
  access, it seems probable that the other seven instructions will also be fetched, and it is cheaper to
  read multiple instructions from memory at the same time.
  Unfortunately, much of networking code contains error checks such as “If error E do X, else do Z.”
  Z is hardly ever executed, but a compiler will often arrange the code for Z immediately after X. For
  example, in Fig. 5.12 imagine that code for Z immediately follows X. If X and Z fall in the same
  block of eight instructions, then fetching frequently accessed X also results in fetching infrequently
  used Z. This makes loading the cache less efficient (more useless work) and makes the cache less
  useful after loading (less useful code in cache).
    Note that both of these effects are caused by the fact that real caches imperfectly reflect tempo-
ral locality. The first is caused by an imperfect hash function that can cause collisions between two
frequently used addresses. The second is caused by the fact that the cache also optimizes for spatial
locality.
    Both effects can be mitigated by reorganizing networking code (Mosberger et al., 1996) so that all
frequently used code is contiguous (see right of Fig. 5.12). For example, in the case “If error E do X,
else do Z,” the code for Z can be moved far away from X. This does require an extra jump instruction
to be added to the code for Z so that it can jump back to the code that followed Z in the unoptimized
version. However, this extra jump is taken only in the error case, and so it is not much of a cost.
    This is an example of realizing that the memory location of code is a degree of freedom that can
be optimized (P13) and an example of optimizing the expected case (P11) despite increasing the code
path for infrequently used code.
