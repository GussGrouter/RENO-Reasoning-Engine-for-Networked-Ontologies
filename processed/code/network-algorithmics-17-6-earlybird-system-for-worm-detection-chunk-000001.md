# network-algorithmics-17-6-earlybird-system-for-worm-detection (chunk 000001)

# Network Algorithmics — 17.6 EarlyBird system for worm detection (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 533
- Slice: from `17.6 EarlyBird system for worm detection` up to next detected section heading

---

17.6 EarlyBird system for worm detection
EarlyBird (Singh et al., 2004b) is one of the earliest systems for detecting new worms, whose signatures
have never been learned or analyzed, with no or minimum human intervention. A key innovation of
EarlyBird is a fingerprinting technique that is among the earliest for the automated extraction of two
aforementioned features of a new worm: large volume of identical traffic and large number of sources
(IP addresses) sending identical traffic. More specifically, EarlyBird offers a highly scalable solution
to the problem of detecting common substrings in application-layer messages sent by many different
source IP addresses. Such a common substring can be a worm suspect, if it appears in a large number
of application (layer) messages sent from a large number of sources. Since an application message is
often divided into multiple packets for network transmission, we call it an object instead in the rest of
this section to distinguish it from a packet.
    To motivate the EarlyBird solution, we highlight three major challenges in detecting and finger-
printing a common substring in objects, and describe why simple ideas do not work. The first challenge
is that the content of such a common substring is not known in advance and is itself to be learned.
As a result, this problem cannot be simply modeled and solved as the aforementioned string matching
problem (see Section 17.2), since here we do not have a target string to search for.
    The second challenge lies in the fact that, even if we knew the exact target substring, the aforemen-
tioned string matching solutions still would not apply. This is because an object containing the substring
to be searched for can be packetized into multiple packets and it is usually not certain at which byte po-
sition the substring is cut (into packets) for two reasons. First, the typical length of a payload-containing
packet varies across different operating systems. Second, since the application-layer header of an object
(e.g., SMTP header in an email) can vary in length, the location (relative offset from the first byte of
the packet payload) at which the substring appears in an object may vary from one object to another.

17.6 EarlyBird system for worm detection                       507
