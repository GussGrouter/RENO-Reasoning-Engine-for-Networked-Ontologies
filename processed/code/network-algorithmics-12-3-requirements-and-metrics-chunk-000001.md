# network-algorithmics-12-3-requirements-and-metrics (chunk 000001)

# Network Algorithmics — 12.3 Requirements and metrics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 328
- Slice: from `12.3 Requirements and metrics` up to next detected section heading

---

12.3 Requirements and metrics
The requirements for rule matching are similar to those for IP lookups (Chapter 11). We wish to do
packet classification at wire speed for minimum-size packets, and thus speed is the dominant metric.
To allow the database to fit in high-speed memory, it is useful to reduce the amount of memory needed.
For most firewall databases, insertion speed is not an issue because rules are rarely changed.
    However, this is not true for dynamic or stateful packet rules. This capability is useful, for example,
for handling UDP traffic. Because UDP headers do not contain an ACK bit that can be used to determine
whether a packet is the bellwether packet of a connection, the screening router cannot tell the difference
between the first packet sent from the outside to an internal server (which it may want to block) and a
response sent to a UDP request to an internal client (which it may want to pass). The solution used in
some products is to have the outgoing request packet dynamically trigger the insertion of a rule (which
has addresses and ports that match the request) that allows the inbound response to be passed. This
requires very fast update times, a third metric.
    Besides stateful firewalls, Software-defined Networking (SDN) may also require frequent rule in-
sertions. For instance, reactive SDN controllers add a new rule wherever new traffic starts. Rule updates
could become more frequent as network management becomes more agile and programmatic.

12.4 Simple solutions
There are six simple solutions that are often used or considered: linear search, tuple space search,
caching, demultiplexing algorithms, MPLS, and content-addressable memories (CAMs). While CAMs
have difficult hardware design issues, they effectively represent a parallelization of the simplest algo-
rithmic approach: linear search.

12.4.1 Linear search
Some older firewall implementations do a linear search of the database and keep track of the best-
matching rule. Linear search is reasonable for small rule sizes but is extremely slow for large rule sets.
For example, a core router that does linear search among a rule set of 2000 rules (used at the time of
writing by some ISPs) will considerably degrade its forwarding performance below wire speed.
