# Network Algorithmics — 11.15 Programmable Lookup Chips and P4 (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 313
- Slice: from `11.15 Programmable Lookup Chips and P4` up to next detected section heading

---

11.15 Programmable Lookup Chips and P4
Many routers use fixed function lookup chip models similar to those in the last section, where a
limited amount of programmability can be done in firmware. For example, for the wide area Arista
7500R3/7800R3 and 7280R3 routers that scale to more than 2.5 million routes, their documenta-
tion (Arista Corporation, 2010) states that “internally FlexRoute uses an algorithmic approach to
performing lookups”.
    By contrast, in recent years, chips, such as Intel’s Tofino-3 (Intel Corporation, 2022), have emerged
that have a fairly large amount of TCAM and are programmable using higher level languages such as

                                           11.15 Programmable Lookup Chips and P4                    287



P4. We will explore P4 and the use of CAMs briefly in this section. For example, Intel’s Aurora 710,
based on Intel Tofino 3.2T switching silicon, claims (Intel Corporation, 2022) to allow data centers to
increase the IP routing table size to 1.2M. Further, the TCAM is distributed among a set of physical
stages that can be programmed using P4.
     The Tofino-3 is an example of what is called the Reconfigurable Match Table (RMT) (Bosshart et
al., 2013) approach to programmable network processors. Briefly, the RMT approach is a generaliza-
tion of the fixed function chip described in the last section which is internally pipelined, and where each
stage has access to on-chip SRAM and is devoted to a single function. By contrast, in the RMT archi-
tecture the chip internally has a large number (say 32) of stages that are anonymous (not devoted to any
function) and programmable (they can be programmed to perform basic functions on packet headers).
Further, each stage has both RAM and CAM. In fact, the CAM in say the Tofino-3 is so plentiful that it
can support a large number of routes without any further algorithmic approaches.
     As a packet flows through the RMT chip, each packet header is streamed through the stages with
successive packet headers following in lockstep to keep the pipeline full. While the SRAM and the
CAM pages are divided among the physical stages, a single logical stage of processing (e.g., a level of
processing in a tree) can get more memory by being allocated more physical stages.
     Each physical stage can be programmed not just in firmware by internal experts but by network
operators in the field using a higher language called P4 (though our experience is that P4 programming
is also somewhat esoteric). This field-programmability is similar to the programmability offered by
Field Programmable Gate Arrays (FPGAs). Unlike FPGAs, chips like Tofino-3 are much faster. They
gain speed, however, by offering limited programmabilty, using the P4 language that we now explore.


11.15.1 The P4 language
P4 (P4 Open Source Programming Language) is a high-level language for “programming protocol-
independent packet processors”. P4’s versatility and flexibility change the way network functions are
implemented at high speeds. P4 offers:
1. Reconfigurability: Even after the P4 program is deployed to a reconfigurable hardware router, an
   operator can modify the programs in the field as desired, unlike traditional fixed function ASICs.
2. Protocol independence: The P4 language can specify how the processor deals with packet headers,
   regardless of what protocols are used. In particular, while P4 can support IP headers it is not limited
   to IP. It thus generalizes the SDN approach by allowing custom headers and not just programmable
   routes.
3. Target independence: The same P4 program can be deployed to a variety of hardware, such as CPUs,
   FPGAs, and programmable processors such as Tofino-3.
    P4 needs to allow reconfigurability and yet allow Terabit implementations that are as fast as the
ones implemented using custom ASICs in the past. Traditional FPGAs are fully reconfigurable but at
least an order of magnitude slower than custom ASICs. P4 resolves this quandary by allowing limited
reconfigurability that suffices for network implementations.
    P4 does this by first allowing new headers to be defined using a programmable parser. If, for ex-
ample, an organization wants to add a new security tag (say STAG) between the Ethernet and IPv4
headers, P4 allows the operator to define the STAG length and fields, and place it between the Ethernet
and IPv4 headers. Second, P4 defines a way to process new headers where each header is processed by

288      Chapter 11 Prefix-match lookups



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
