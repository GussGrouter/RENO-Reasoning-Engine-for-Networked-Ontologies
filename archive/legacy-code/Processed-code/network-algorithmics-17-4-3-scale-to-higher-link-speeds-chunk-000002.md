# network-algorithmics-17-4-3-scale-to-higher-link-speeds (chunk 000002)

since 2.5% × 16 is also 0.4, another way is to sample 2.5% of the packets, and let each full Bloom filter
be 16 bits. Then which one is better?
    Intuitively, a higher sampling rate helps, as it increases the size of the overlap, which the traceback
operation depends on, between the two sets of packets seen by two neighboring routers. However, the
number of hash functions would have to be proportionally smaller, which results in the Bloom filter
having a higher false-positive rate. This adds noise to the traceback process and reduces the accuracy.
Clearly there is an inherent tradeoff between these two parameters, but where is the “sweet spot” (i.e.,
optimal parameter setting)?
    In Li et al. (2004) this question was fully settled using information theory, or more specifically,
via mutual information maximization. In the example above the optimal tradeoff point is found to be
around 3.3% ∗ 12 = 0.4 under a few representative network topologies and parameter settings. It was
shown in Li et al. (2004) that, with these two enhancements, even under this stringent budget constraint
of 0.4 bits per packet, the enhanced traceback (by sampled logging) scheme can accurately identify the
attacker with a high probability when the victim receives at least hundreds of packets from the attacker.

17.5 Detecting worms
This section and the next two focus on the problem of detecting worms. A worm (such as Code Red,
Nimda, Slammer) begins with an exploit sent by an attacker to take over a machine. The exploit is
typically a buffer overflow attack, which is caused by sending a packet (or packets) containing a field
that has more data than can be handled by the buffer allocated by the receiver for the field. If the receiver
implementation is careless, the extra data beyond the allocated buffer size can overwrite key machine
parameters, such as the return address on the stack.
    Thus with some effort, a buffer overflow can allow the attacking machine to run code on the attacked
machine. The new code then picks several random IP addresses2 and sends similar packets to these new
victims. Even if only a small fraction of IP addresses respond to these attacks, the worm spreads rapidly.
    Current worm detection technology is both retroactive (i.e., only after a new worm is first detected
and analyzed by a human, a process that can take days, can the containment process be initiated) and
manual (i.e., requires human intervention to identify the signature of a new worm). Such technology
is exemplified by Code Red and Slammer, which took days of human effort to identify, following
which containment strategies were applied in the form of turning off ports, applying patches, and doing
signature-based filtering in routers and intrusion detection systems.
    There are difficulties with these current technologies.
1. Slow Response: There is a proverb that talks about locking the stable door after the horse has es-
   caped. Current technologies fit this paradigm because, by the time the worm containment strategies
   are initiated, the worm has already infected much of the network.
2. Constant Effort: Every new worm requires a major amount of human work to identify, post advi-
   sories, and finally take action to contain the worm. Unfortunately, all evidence seems to indicate that

2 By contrast, a virus requires user intervention, such as opening an attachment, to take over the user machine. Viruses also
typically spread by using known addresses, such as those in the mail address book, rather than random probing.

17.5 Detecting worms                 505
