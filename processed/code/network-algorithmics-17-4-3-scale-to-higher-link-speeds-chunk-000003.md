# network-algorithmics-17-4-3-scale-to-higher-link-speeds (chunk 000003)

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
