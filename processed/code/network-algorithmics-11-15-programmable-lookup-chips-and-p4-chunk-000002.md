# network-algorithmics-11-15-programmable-lookup-chips-and-p4 (chunk 000002)

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
