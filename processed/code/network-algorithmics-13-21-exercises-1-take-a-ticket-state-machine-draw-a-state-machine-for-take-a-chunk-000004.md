# network-algorithmics-13-21-exercises-1-take-a-ticket-state-machine-draw-a-state-machine-for-take-a (chunk 000004)

Fair Dropping (AFD) that has a similarly low time complexity as RED, yet a similarly good QoS guar-
antee as Deficit Round Robin. Section 14.4 offers a simple scheme to limit the bandwidth and burstiness
of a flow, and Section 14.5 describes a basic priority scheme. Section 14.6 provides a brief introduction
to reservation protocols. Section 14.7 presents simple techniques to apportion the available link band-
width among competing flows. The section also briefly describes how the accompanying reservations
for flow bandwidths can be made. Section 14.8 provides an introduction to how one can provide good
delay guarantees for a flow at the cost of sorting packet deadlines in real time.
    Sections 14.9 through Section 14.14 begin a technical description of how to ensure both delay
bounds and fairness, culminating in Quick Fair Queuing that is implemented in the Linux kernel. These
sections can be skipped by more practical readers who may want to skip to Section 14.14. Section 14.9
introduces generalized processor sharing (GPS), the fairest possible scheduling policy. Although the
GPS policy is not practically implementable, a key component of it called GPS clock tracking is. This
implementation is described in Section 14.12. GPS clock tracking lies at the heart of implementing
weighted fair queueing (WFQ) and worst-case fair weighted-fair queueing (WF2 Q), two practically
implementable packet scheduling policies that are almost as fair as GPS. They are described in Sec-
tion 14.10 and Section 14.11, respectively. Section 14.14 describes Quick Fair Queuing (QFQ), a packet
scheduling algorithm that provides a QoS guarantee similar to WF2 Q, yet has an implementation com-
plexity comparable to DRR.
    Finally, Section 14.15 describes two research proposals towards making packet scheduling pro-
grammable in switches and routers: PIFO in Section 14.15.1 and UPS in Section 14.15.2. Section 14.16
describe several scalable schedulers that are able to schedule a large number of flows with little or no
state.
    The packet-scheduling techniques described in this chapter (and the corresponding principles in-
volved) are summarized in Table 14.1.

14.1 Motivation for quality of service                     385

Quick reference guide
  The most important scheduling algorithms that an Internet router must implement are RED (Section 14.2), token buckets
  (Section 14.4), priority queueing (Section 14.5), deficit round-robin (DRR) (Section 14.7.3), and DiffServ (for DiffServ,
  consult only the relevant portion of Section 14.16). Other interconnect devices, such as SAN switches and gateways, are
  not required to implement RED; however, implementing some form of QoS, such as DRR or token buckets, in such devices
  is also a good idea. Cisco routers also implement Approximate Fair Dropping (Section 14.3) as a cheaper alternative to
  DRR. Finally, Quick Fair Queuing (QFQ), described in Section 14.14, provides comparable implementation complexity
  to DRR but has much better delay bounds; it was incorporated into the Linux kernel.

Table 14.1 Summary of packet-scheduling techniques used in this chapter
              and the corresponding principles.
              Number                     Principle                           Scheduling technique
              P7          Use power of two parameters                 RED
              P3          Use policing, not shaping                   Token bucket policing
              P3          Focus on bandwidth only                     DRR
              P12         Maintain list of active queues
              P7          Use large enough quanta
              P3a         Aggregate by hashing flows                  SFQ
              P3c         Shift work to edge routers                  DiffServ
              P10         Incrementally compute interest vector
              P10         Pass class in TOS field                     Core stateless
              P2b         clean up lazily                             GPS clock tracking using shape data
                                                                      structure
              P15         use augmented data structure
              P3b         schedule among groups using DRR             QFQ
              P14         use bucket sorting, bitmaps
              P4c         use built-in instruction
