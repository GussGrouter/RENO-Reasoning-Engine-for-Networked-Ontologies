# network-algorithmics-4-4-ethernet-monitor-bridge-hardware (chunk 000002)

• Can this problem be solved using only two bridge hardware lookups without requiring extra mem-
  ory?
• The set of active source–destination pairs may change with time because some pairs of addresses
  stop communicating for long periods. How can this be handled without keeping the state for every
  possible address pair that has communicated since the monitor was powered on?

---

## PDF page 111

84        Chapter 4 Principles in action

FIGURE 4.9
Demultiplexing in the x-kernel is done by hashing the protocol identifier K and (potentially) using a byte-by-byte
comparison with the key L stored at the hash table entry.
