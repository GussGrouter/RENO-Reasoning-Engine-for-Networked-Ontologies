# network-algorithmics-13-18-scaling-to-larger-and-faster-switches (chunk 000001)

# Network Algorithmics — 13.18 Scaling to larger and faster switches (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 390
- Slice: from `13.18 Scaling to larger and faster switches` up to next detected section heading

---

13.18 Scaling to larger and faster switches
As various hurdles exist for existing switching schemes to scale to a large number of ports and higher
per-port speeds, Section 13.18 describes two approaches to that end. Both approaches achieve the two
scalability objectives by reducing one or both of the two major switching costs, namely, the overall
size of the switch circuitry and the time complexity of the bipartite matching computation. The first
approach, based on the principle of divide and conquer (P15), reduces the overall size of the switch
circuitry through the use of more space-efficient switch fabrics than a monolithic crossbar, such as the
Clos fabric (Section 13.18.3) and the Benes fabric (Section 13.18.4). The other, called Load-Balanced
Switching (LBS), reduces the algorithmic cost of bipartite matching computation to virtually zero.
However, it does so by using two large crossbars instead of one.
    So far, this chapter has concentrated on fairly small switches that suffice to build up to a 32-port
router. Most Internet routers deployed up to the time of writing have been in this category, sometimes
for good reasons. For instance, building wiring codes tend to limit the number of offices that can be
served from a wiring closet. Thus switches for local area networks (Simcoe and Pei, 1994) located in
wiring closets tend to be well served with small port sizes.
    However, the telephone network has generally employed a few very large switches that can switch
1000–10,000 lines. Employing larger switches tends to eliminate switch-to-switch links, reducing over-
all latency and increasing the number of switch ports available for users (as opposed to being used to
connect to other switches). Thus while a number of researchers (e.g., Turner, 1997 and Chaney et al.,
1997) have argued for such large switches, there was little large-scale industrial support for such large
switches until recently.
    There are three recent trends that favor the design of large switches.
1. DWDM: The use of dense wavelength-division multiplexing (DWDM) to effectively bundle multi-
   ple wavelengths on optical links in the core will effectively increase the number of logical links that
   must be switched by core routers.
2. Fiber to the home: There is a good chance that in the near future, even homes and offices will be
   wired directly with fiber that goes to a large central office–type switch.
3. Modular, multichassis routers: There is increasing interest in deploying router clusters that consist
   of a set of routers interconnected by a high-speed network. For example, many network access

364        Chapter 13 Switching

points connect up routers via an FDDI link or by a GigaSwitch (see Section 13.4). Router clusters,
    or multichassis routers as they are sometimes called, are becoming increasingly interesting because
    they allow incremental growth, as explained later.
    The typical lifetime of a core router is estimated (Semeria and Gredler, 2001) to be 18–24 months,
after which traffic increases often cause ISPs to throw away older-generation routers and wheel in new
ones. Multichassis routers can extend the lifetime of a core router to five years or more, by allowing
ISPs to start small and then to add routers to the cluster according to traffic needs.
    In the early 2000s Juniper Networks led the pack by announcing its T-series routers, which allow up
to 16 single-chassis routers (each of which has up to 16 ports) to be assembled via a fabric into what is
effectively a 256-port router. At the heart of the multichassis system is a scalable 256-by-256 switching
system. Also in the early 2000s Cisco Networks announced its own version, the CRS-1 Router.
