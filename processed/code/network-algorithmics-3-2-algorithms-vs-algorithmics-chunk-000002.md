# network-algorithmics-3-2-algorithms-vs-algorithmics (chunk 000002)

To accomplish this, in Fig. 3.6 we keep a queue of the last 100,000 packets that were sent by the
router. When a packet is forwarded, we also add a copy of the packet (or just keep a pointer to the
packet) to the head of the queue. To keep the queue bounded, when the queue is full, we delete from
the tail as well.
    The main difficulty with this scheme is that when a guilty flow is detected, there may be lots of
the flow’s packets in the queue (Fig. 3.6). All of these packets must be placed in the forensic log for
transmission to a manager. The naive method of searching through a large DRAM buffer is very slow.
    The textbook algorithms approach would be to add some index structure to search quickly for flow
IDs. For example, one might maintain a hash table of flow IDs that maps every flow to a list of pointers
to all packets with that flow ID in the queue. When a new packet is placed in the queue, the flow ID is
looked up in the hash table and the address of the new packet in the queue is placed at the end of the
flow’s list. Of course, when packets leave the queue, their entries must be removed from the list, and
the list can be long. Fortunately, the entry to be deleted is guaranteed to be at the head of the queue for
that flow ID.
    Despite this, the textbook scheme has some difficulties. It adds more space to maintain these extra
queues per flow ID, and space can be at a premium for a high-speed implementation. It also adds some
extra complexity to packet processing to maintain the hash table and requires reading out all of a flow’s
packets to the forensic log before the packet is overwritten by a packet that arrives 100,000 packets
later. Instead, the following “systems” solution may be more elegant.

Solution
Do not attempt to immediately identify all of a flow F ’s packets when F is identified, but lazily identify
them as they reach the end of the packet queue. This is shown in Fig. 3.7. When we add a packet to the
head of the queue, we must remove a packet from the end of the queue (at least when the queue is full).

---

## PDF page 84
