# network-algorithmics-16-12-a-concerted-approach-to-accounting (chunk 000002)

not much harder than one counter, and incrementing in parallel is easily feasible if the 16 counters
   are maintained on-chip in a forwarding ASIC. The solution also aligns with real user needs because
   it cheaply supports the use of up to 16 destination-sensitive3 counters.
2. Routing Support: To attack the problem of changing prefix routes (which would result in the tool’s
   having to constantly map each prefix into a different class), the DCU solution enlists the help of
   the routing protocol. The idea is that all prefixes advertised by ISP X are given a color (which
   can be controlled using a simple route policy filter), and prefixes advertised by ISP Y are given a
   different color. Thus, when a router such as R1 gets a route advertisement for prefix P with color c,
   it automatically assigns prefix P to class c. This small change in the routing protocol greatly reduces
   the work of the tool.
    Juniper also has other schemes (Semeria and Gredler, 2001), including counters based on packet
classifiers and counters based on MPLS tunnels. These are slightly more flexible than DCU accounting
because they can take into account the source address of a packet in determining its class. But these
other schemes do not have the administrative scalability of DCU accounting because they lack routing
support.
    The DCU accounting scheme is an example of P4, leveraging existing system components, and P3,
relaxing system requirements (e.g., only a small number of aggregate classes).
