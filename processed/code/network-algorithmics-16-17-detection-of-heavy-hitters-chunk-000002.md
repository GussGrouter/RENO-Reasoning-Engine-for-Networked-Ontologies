# network-algorithmics-16-17-detection-of-heavy-hitters (chunk 000002)

The idea of ElephantTrap is quite similar to that of sample-and-hold. It also samples packets and
adds new flows to the flow table. There are, however, two main differences. First, unlike sample-
and-hold, which checks every packet against the cached flow table, ElephantTrap samples a certain
percentage of packets and only checks them against the cached flow table (sampled increments).
    Second, unlike sample-and-hold, which only increments and never decrements the values of (flow
size) counters, ElephantTrap gradually cycles around the cached flow table and halves their values
(exponential decay). Flow-table entries with counter values lower than a certain threshold are eligible
for eviction to make room for a new flow. Due to the sampled increments and the exponential decay, the
size of a flow can no longer be inferred accurately from the corresponding counter value. ElephantTrap,
developed and nicknamed “ETrap” (Cisco Systems Inc., 2017; Ronad, 2019) by Cisco, has been used
for intelligent buffering and scheduling on the Cisco Nexus 9000 Series Switch products.
