# Network Algorithmics — 8.7 Conclusions While it may be trite to say that necessity is the mother of invention, it is also often true. New needs (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 235
- Slice: from `8.7 Conclusions While it may be trite to say that necessity is the mother of invention, it is also often true. New needs` up to next detected section heading

---

8.7 Conclusions
While it may be trite to say that necessity is the mother of invention, it is also often true. New needs
drive new innovations; the lack of a need explains why innovations did not occur earlier. The CSPF filter
was implemented when the major need was to avoid a process context switch; having achieved that,
improved filter performance was only a second-order effect. BPF was implemented when the major
need was to implement a few filters very efficiently to enable monitoring tools like tcpdump to run at
close to wire speeds. Having achieved that, scaling to a large number of filters seemed less important.
    Pathfinder was implemented to support user-level networking in the x-kernel (Hutchinson and
Peterson, 1991), and to allow Scout (Mosberger and Peterson, 1996) to use paths as a first-class
object that could be exploited in many ways. Having found a plausible hardware implementation,
perhaps improved software performance seemed less important. DPF was implemented to provide
high-performance networking together with complete application-level flexibility in the context of an
extensible operating system (Engler et al., 1995). Table 8.1 presents a summary of the techniques used
in this chapter, together with the major principles involved.
    However, given the popularity of TCP/IP today and the availability of packet steering mechanisms
in major operating systems, it seems unclear that Pathfinder and DPF are worth the extra complexity
today. BPF continues to be useful for monitoring tools.

                                                                             8.8 Exercises       209



    In terms of ideas, however, as in the H.G. Wells quote at the start of the chapter, each algorithm
builds on the earlier algorithms. All filter implementations borrow from CSPF the intellectual leap
of separating demultiplexing from packet processing, together with the notion that application demulti-
plexing specifications can be safely exported to the kernel. DPF and Pathfinder in turn borrow from BPF
the basic notion of exploiting the underlying architecture using a register-based, state-machine model.
DPF borrows from Pathfinder the notion of using a generalized trie to factor out common checks.
