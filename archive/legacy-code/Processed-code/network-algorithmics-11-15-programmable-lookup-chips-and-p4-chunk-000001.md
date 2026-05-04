# network-algorithmics-11-15-programmable-lookup-chips-and-p4 (chunk 000001)

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
