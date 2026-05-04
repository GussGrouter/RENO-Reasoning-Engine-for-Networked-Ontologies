# network-algorithmics-17-4-3-scale-to-higher-link-speeds (chunk 000004)

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
