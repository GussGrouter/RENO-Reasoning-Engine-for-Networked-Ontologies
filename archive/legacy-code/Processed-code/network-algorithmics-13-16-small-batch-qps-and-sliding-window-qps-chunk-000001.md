# network-algorithmics-13-16-small-batch-qps-and-sliding-window-qps (chunk 000001)

# Network Algorithmics — 13.16 Small-batch QPS and sliding-window QPS (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 386
- Slice: from `13.16 Small-batch QPS and sliding-window QPS` up to next detected section heading

---

13.16 Small-batch QPS and sliding-window QPS
In this section, we describe a late-breaking input-queued switching algorithm called sliding-window
queue-proportional sampling (Meng et al., 2020). SW-QPS improves upon a parallel batch switching
algorithm called small-batch queue-proportional sampling (SB-QPS) that was also proposed in Meng et
al. (2020). It was shown in Meng et al. (2020) that, compared to other batch switching algorithms such
as Aggarwal et al. (2003); Neely et al. (2007); Wang et al. (2018), SB-QPS significantly reduces the
batch size without sacrificing the throughput performance and hence has much lower delay when traffic
load is light to moderate. It also achieves the lowest possible time complexity of O(1) per matching
computation per port, via parallelization, using the QPS data structure and algorithm we have just
described. SW-QPS retains and enhances all benefits of SB-QPS and reduces the batching delay to
zero via a novel switching framework called sliding-window switching.
     To compute each matching, SW-QPS runs only a single iteration, as compared to O(log N ) itera-
tions needed by iSLIP in theory. Each SW-QPS iteration is also “cheaper” than an iSLIP iteration in two
aspects. First, the time complexity of each SW-QPS iteration, to be explained next, is O(1), whereas
each iSLIP iteration is O(log N ) in theory using the programmable priority encoder described in Sec-
tion 2.2.3. Second, whereas an input port sends out only a single request in each SW-QPS iteration, it
sends out in general O(N ) requests (to every output port whose corresponding VOQ is nonempty) in
each iSLIP iteration. Despite being much “cheaper,” SW-QPS achieves overall better throughput and
delay performance than iSLIP, as shown in Meng et al. (2020).
