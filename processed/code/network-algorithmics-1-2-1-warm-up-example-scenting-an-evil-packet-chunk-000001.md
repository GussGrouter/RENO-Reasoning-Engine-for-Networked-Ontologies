# network-algorithmics-1-2-1-warm-up-example-scenting-an-evil-packet (chunk 000001)

# Network Algorithmics — 1.2.1 Warm-up example: scenting an evil packet (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 35
- Slice: from `1.2.1 Warm-up example: scenting an evil packet` up to next detected section heading

---

1.2.1 Warm-up example: scenting an evil packet
Imagine a front-end network monitor (or intrusion detection system) on the periphery of a corporate
network that wishes to flag suspicious incoming packets—packets that could contain attacks on internal
computers. A common such attack is a buffer overflow attack, where the attacker places machine code
C in a network header field F .
    If the receiving computer allocates a buffer too small for header field F and is careless about check-
ing for overflow, the code C can spill onto the receiving machine’s stack. With a little more effort, the
intruder can make the receiving machine actually execute evil code C. C then takes over the receiver
machine. Fig. 1.3 shows such an attack embodied in a familiar field, a destination Web URL (uniform
resource locator). How might the monitor detect the presence of such a suspicious URL? A possible
way is to observe that URLs containing evil code are often too long (an easy check) and often have a
large fraction of unusual (at least in URLs) characters, such as #. Thus the monitor could mark such
packets (containing URLs that are too long and have too many occurrences of such unusual characters)
for a more thorough examination.
    It is worth stating at the outset that the security implications of this strategy need to be carefully
thought out. For example, there may be several innocuous programs, such as CGI scripts, in URLs that
lead to false positives. Without getting too hung up in overall architectural implications, let us assume
that this was a specification handed down to a chip architect by a security architect. We now use this
sample problem, suggested by Mike Fisk, to illustrate algorithmics in action.
    Faced with such a specification, a chip designer may use the following design process, which illus-
trates some of the principles of network algorithmics. The process starts with a strawman design and
refines the design using techniques such as designing a better algorithm, relaxing the specification, and
exploiting hardware.
