# network-algorithmics-16-13-1-approach-1-internet-tomography (chunk 000001)

# Network Algorithmics — 16.13.1 Approach 1: Internet tomography (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 500
- Slice: from `16.13.1 Approach 1: Internet tomography` up to next detected section heading

---

16.13.1 Approach 1: Internet tomography
This approach (see Medina et al. (2002); Zhang et al. (2003) for useful reviews of past work) recognizes
the impossibility of deterministic inference from SNMP counters cited earlier and instead attempts
statistical inference, with some probability of error. At the heart of the inference technique is some
model of the underlying traffic distribution (e.g., Gaussian, gravity model) and some statistical (e.g.,
maximum likelihood) or optimization technique (e.g., quadratic programming (Zhang et al., 2003)4 ).
    Early approaches based on Gaussian distributions did very poorly (Medina et al., 2002), but a new
approach based on gravity models does much better, at least on the AT&T backbone. The great advan-
tage of tomography is that it works without retrofitting existing routers, and it is also clearly cheap to
implement in routers. A possible disadvantage of this method is the potential errors in the method (off
by as much as 20% in Zhang et al. (2003)), its sensitivity to routing errors (a single link failure can
throw an estimate off by 50%), and its sensitivity to topology.

4 Some authors limit the term tomography to the use of statistical models; thus Zhang et al. (2003) refer to their work as
tomogravity. But this is splitting hairs.

474      Chapter 16 Measuring network traffic
