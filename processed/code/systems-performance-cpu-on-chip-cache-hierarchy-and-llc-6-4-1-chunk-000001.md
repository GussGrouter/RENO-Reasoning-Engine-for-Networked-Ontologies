<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

CPU Caches
Various hardware caches are usually included in the processor (where they are referred to as
on-chip, on-die, embedded, or integrated) or with the processor (external). These improve memory
performance by using faster memory types for caching reads and buffering writes. The levels of
cache access for a generic processor are shown in Figure 6.6.

Figure 6.6 CPU cache hierarchy

231

232

Chapter 6 CPUs

They include:
■

Level 1 instruction cache (I$)

■

Level 1 data cache (D$)

■

Translation lookaside buffer (TLB)

■

Level 2 cache (E$)

■

Level 3 cache (optional)

The E in E$ originally stood for external cache, but with the integration of Level 2 caches it has
since been cleverly referred to as embedded cache. The “Level” terminology is used nowadays
instead of the “E$”-style notation, which avoids such confusion.
It is often desirable to refer to the last cache before main memory, which may or may not be level
3. Intel uses the term last-level cache (LLC) for this, also described as the longest-latency cache.
The caches available on each processor depend on its type and model. Over time, the number
and sizes of these caches have been increasing. This is illustrated in Table 6.3, which lists example Intel processors since 1978, including advances in caches [Intel 19a][Intel 20a].
