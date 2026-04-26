# Network Algorithmics — 17.4.3 Scale to higher link speeds (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 529
- Slice: from `17.4.3 Scale to higher link speeds` up to next detected section heading

---

17.4.3 Scale to higher link speeds
When the link speeds continue to grow faster, a router cannot even afford to record a full Bloom filter
for every packet. It can however afford to record either a full Bloom filter for a small percentage of
packets or a “tiny fraction” of a Bloom filter for every packet. For example, when the SRAM budget is
only 0.4 bits (hash functions) per packet and each full Bloom filter is 12 bits (hash functions), a router
can record a full Bloom filter for only 3.3% of the packets. In this case the traceback by logging scheme
described above would not work. For example, if two neighboring routers along an attack path sample

                                                              17.4 IP traceback via logging             503




FIGURE 17.8
Hardware implementation of packet logging using Bloom filters. Note the use of two-level memory: SRAM for
random read-modify-writes and DRAM for large row writes.


packets independently uniformly at random each at such a low sampling rate, an attack packet seen by
one router is likely not seen by the other, making it hard to trace back even this single step.
    In Li et al. (2004) two significant enhancements are made to this scheme to make it perform well in
this more challenging environment. The first enhancement is a correlated sampling scheme called One-
Bit Random Marking and Sampling (ORMS), which is similar to that in trajectory sampling in spirit
but is more sophisticated to make it adversary-proof (necessary for this security application). This idea
can improve the correlation factor between the two sets of packets sampled (for Bloom filter logging)
at two neighboring routers to over 50%; in contrast, independent uniform random sampling by the two
neighboring routers would result in a correlation factor of only 3.3% in the example above. Intuitively,
a higher correlation factor between packets sampled by two neighboring routers makes it easier to trace
back to an attacker.
    The second enhancement is to fully develop the optimization theory concerning the optimal tradeoff
point between the sampling rate and the “size” of each full Bloom filter. Again suppose the budget is
0.4 bits per packet, as in the example above. For example, since 5% × 8 = 0.4, one possible way to use
this budget is to sample 5% of the packets and let each full Bloom filter be 8 bits (hash functions); but

504        Chapter 17 Network security



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



    there is no shortage of new exploits. And worse, simple binary rewriting and other modifications of
    existing attacks can get around simple signature-based blocking (as in Snort).
    Thus there is a pressing need for a new worm detection and containment strategy that is real time
(and hence can contain the worm before it can infect a significant fraction of the network) and is able
to deal with new worms with a minimum of human intervention (some human intervention is probably
unavoidable to at least catalog detected worms, do forensics, and fine-tune automatic mechanisms). In
particular, the detection system should be content agnostic. The detection system should not rely on
external, manually supplied input of worm signatures. Instead, the system should automatically extract
worm signatures, even for new worms that may arise in the future.
    Can network algorithmics speak to this problem? We believe it can. First, we observe that the only
way to detect new worms and old worms with the same mechanism is to abstract the basic properties
of worms.
    As a first approximation, define a worm to have the following abstract features, which are indeed
discernible in all the worms we know, even ones with such varying features as Code Red (massive pay-
load, uses TCP, and attacks on the well-known HTTP port) and MS SQL Slammer (minimal payload,
uses UDP, and attacks on the lesser-known MS SQL port).
1. Large Volume of Identical Traffic: These worms have the property that at least at an intermediate
   stage (after an initial priming period but before full infection), the volume of traffic (aggregated
   across all sources and destinations) carrying the worm is a significant fraction of the network band-
   width.
2. Rising Infection Levels: The number of infected sources participating in the attack steadily increases.
3. Random Probing: An infected source spreads infection by attempting to communicate to random IP
   addresses at a fixed port to probe for vulnerable services.
Note that detecting all three of these features may be crucial to avoid false positives. For example, a
popular mailing list or a flash crowd could have the first feature but not the third.
    An algorithmics approach for worm detection would naturally lead to the following detection strat-
egy, which automatically detects each of these abstract features with low memory and small amounts of
processing, works with asymmetric flows, and does not use active probing. The high-level mechanisms3
are:
1. Identify Large Flows in Real Time with Small Amounts of Memory: In Section 16.7 we showed how
   to describe mechanisms to identify flows with large traffic volumes for any definition of a flow (e.g.,
   sources, destinations). A simple twist on this definition is to realize that the content of a packet (or,
   more efficiently, a hash of the content) can be a valid flow identifier, which by prior work can identify
   in real time (and with low memory) a high volume of repeated content. An even more specific idea
   (which distinguishes worms from valid traffic such as peer-to-peer) is to compute a hash based on
   the content as well as the destination port (which remains invariant for a worm).
2. Count the Number of Sources: In Section 16.8 we described mechanisms using simple bitmaps
   of small size to estimate the number of sources on a link using small amounts of memory and


3 Each of these mechanisms needs to be modulated to handle some special cases, but we prefer to present the main idea untar-
nished with extraneous details.

506      Chapter 17 Network security



   processing. These mechanisms can easily be used to count sources corresponding to high traffic
   volumes identified by the previous mechanism.
3. Determine Random Probing by Counting the Number of Connection Attempts to Unused Portions of
   the IP Address: One could keep a simple compact representation of portions of the IP address space
   known to be unused. One example is the so-called Bogon list, which lists unused 8-bit prefixes (can
   be stored as a bitmap of size 256). A second example is a secret space of IP addresses (can be stored
   as a single prefix) known to an ISP to be unused. A third is a set of unused 32-bit addresses (can be
   stored as a Bloom filter).
    Of course, worm authors could defeat this detection scheme by violating any of these assumptions.
For example, a worm author could defeat Assumption 1 by using a very slow infection rate and by mu-
tating content frequently. Assumption 3 could be defeated using addresses known to be used. For each
such attack, there are possible countermeasures. More importantly, before the advent of polymorphic
worms (defined next), the scheme described was able to detect at least all existing worms we knew of,
though they differed greatly in their semantics. In initial experiments at UCSD that led to the EarlyBird
system (Singh et al., 2004b), to be described in the next section, we also found very few false positives
where the detection mechanisms complained about innocuous traffic.
