# network-algorithmics-7-9-obtaining-finer-granularity-timers (chunk 000001)

# Network Algorithmics — 7.9 Obtaining finer granularity timers (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 218
- Slice: from `7.9 Obtaining finer granularity timers` up to next detected section heading

---

7.9 Obtaining finer granularity timers
As networks grow faster, one might expect retransmission timers to grow smaller as round-trip delays to
destinations decrease. If round-trip delays fall to microseconds, it makes sense to expect the retransmit
timers to fall to microseconds as well. Unfortunately, with most operating systems, one is stuck with
a millisecond timer even when round-trip delays fall to microseconds. The use of a timing wheel can
allow finer-granularity retransmission timers. But the timers can still be no smaller than the granularity
of the timer tick.
    Now many CPUs provide a programmable hardware interrupt chip that can be programmed to
interrupt the CPU at a desired frequency. Thus an apparently simple method to improve timer resolution
is to increase the frequency of the clock interrupt. Together with the use of a timing wheel, this would
appear to provide much finer timer granularities.
    Unfortunately, there is a flaw in the argument. As we have argued in the model section, modern
CPUs tend to keep a lot of state to speed up processing. This includes pipeline state, the use of a
large number of registers, and caches and TLBs. An interrupt causes high overhead, because it involves
the saving and restoring of CPU state, and can cause changes to locality patterns that result in cache
and TLB misses after exiting the interrupt handler. Early measurements in Aron and Druschel (1999)

192      Chapter 7 Maintaining timers
