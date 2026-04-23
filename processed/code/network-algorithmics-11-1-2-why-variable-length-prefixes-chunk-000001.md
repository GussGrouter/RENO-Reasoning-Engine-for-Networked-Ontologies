# network-algorithmics-11-1-2-why-variable-length-prefixes (chunk 000001)

# Network Algorithmics — 11.1.2 Why variable-length prefixes? (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 279
- Slice: from `11.1.2 Why variable-length prefixes?` up to next detected section heading

---

11.1.2 Why variable-length prefixes?
Before we consider how to deal with the complexity of variable-length-prefix matching, it is worth
understanding why Internet prefixes are variable length. Given a telephone number such as 858-549-
3816, it is a trivial matter to extract the first three digits (i.e., 858) as the area code. If fixed-length
prefixes are easier to implement, what is the advantage of variable-length prefixes?
    The general answer to this question is that variable-length prefixes make more efficient use of the
address space. This is because areas with a large number of endpoints can be assigned shorter prefixes,
while areas with a few endpoints can be assigned longer prefixes.
    The specific answer comes from the history of Internet addressing. The Internet began with a simple
hierarchy in which 32-bit addresses were divided into a network address and a host number; routers
only stored entries for networks. For flexible address allocation, the network address came in variable
sizes: Class A (8 bits), Class B (16 bits), and Class C (24 bits). To cope with the exhaustion of Class B
addresses, the Classless Internet Domain Routing (CIDR) scheme (Rekhter and Li, 1996) assigns new
organizations multiple contiguous Class C addresses that can be aggregated by a common prefix. This
reduces core router table size.
    Today, the potential depletion of the address space has led Internet registries to be very conservative
in the assignment of IP addresses. A small organization may be given only a small portion of a Class C
address, perhaps a /30, which allows only four IP addresses within the organization. Many organizations
are coping with these sparse assignments by sharing a few IP addresses among multiple computers,
using schemes such as network address translation, or NAT.
    Thus, CIDR and NAT have helped the Internet handle exponential growth with a finite 32-bit address
space. While adoption of IP with a 128-bit address (IPv6) is rapidly increasing (Google, 2022), the
effectiveness of NAT in the short run and the complexity of rolling out a new protocol have made 32-bit
IP addresses still dominant at the time of writing.
    The bottom line is that the decision to deploy CIDR helped save the Internet, but it has introduced
the complexity of longest-matching prefix lookup.
