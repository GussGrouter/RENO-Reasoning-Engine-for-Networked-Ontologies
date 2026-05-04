# network-algorithmics-13-17-combined-input-and-output-queueing (chunk 000002)

Prabhakar, 2000). Hence the cost here is that a 2-fold speedup at the output ports is needed for providing
the QoS guarantees (for which P is used). An interesting perspective on why CIOQ did not take off
was explained in Firoozshahian et al. (2007) and Prabhakar (2009).
    CIOQ likely will never take off for the following reason. As explained earlier, we already have
excellent input-queued switching algorithms such as SW-QPS that can deliver excellent throughput
and delay performances at very low costs. We can simply use such an algorithm for switching (packets
from input ports to output ports) and then enforce P at the output ports. When the load is not too high,
the queueing delay (due to switching) of any packet at the corresponding input port should be small, so
that with overwhelming probability it will arrive at its destination output port by the deadline dictated
by P. This way, we can reap almost the full benefit of CIOQ (the QoS guarantees provided by P)
without paying for its high cost.
