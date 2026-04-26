# network-algorithmics-11-15-programmable-lookup-chips-and-p4 (chunk 000003)

a Table, which can be indexed either by exact matching or with wildcarded bits (thus abstracting across
exact match, longest matching prefix and ACL lookup). In a running example, the STAG field could be
processed by an exact match table that drops certain values of the STAG that are in the table.
    Finally, P4 requires specifying a control flow graph that chains together the processing of tables to
describe the overall processing of a packet based on its header fields. Thus in the above example, the
Control Flow Graph would specify that the header is processed by the STAG table after Ethernet, after
which the header is sent to the IPv4 lookup table.
    In summary, a P4 program has three major parts: a header specification for parsing, a specification
of the tables used to process headers, and a control flow graph that describes the “main” program which
specifies how control flows between tables.
    What makes P4 attractive is, as we said earlier, the RMT (Bosshart et al., 2013) architecture that
provides a set of generic match-action stages arranged in a linear pipeline. The wires between stages
are also short unlike traditional FPGA interconnects. Each stage is furnished with a sufficient amount of
CAM and RAM and multiple parallel processors. The programmer or compiler can then assign multiple
physical pipeline stages (or even a fraction of a stage) to logical tables defined in the control flow graph.
    Note that P4 only offers limited reconfurability. Some examples of things that cannot be pro-
grammed by P4 include queueing disciplines (the Tofino-3, does, however offer a palette of queue
disciplines), stateful processing (e.g., NAT) and content processing (e.g., Intrusion detection, detect-
ing content signatures). A great deal of recent research has appeared to tackle some of those issues.
For example, packet transactions (Sivaraman et al., 2016b) attempts to allow programmable stateful
processing and schemes like PIFO (Sivaraman et al., 2016a) attempt to allow programmable queue
disciplines. We will consider these schemes in the chapter on packet scheduling.
    Despite these limitations, P4 appears to be popular. Some important use cases are as follows. First,
simply reallocating resoures can be useful. In a core router there is more need for forwarding tables
and less for ACLs, while the reverse is true for an edge router. Today’s vendors make distinct hardware
products for each; instead a single P4 router can simply be programmed to provide specific routers
for various market segments. Second, adding new headers is often very time consuming. For example,
VXLAN (Mahalingam et al., 2020) took years to be added to custom ASICs; but this could be done in
a few hours on a P4 router. Finally, there are new applications such as measurement and security that
could be programmed in enterprise-specific ways. We will consider some of these in the chapters on
measurement and security.
