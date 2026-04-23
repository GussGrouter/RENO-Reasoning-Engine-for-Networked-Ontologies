# network-algorithmics-13-16-3-the-sw-qps-algorithm (chunk 000001)

# Network Algorithmics — 13.16.3 The SW-QPS algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 388
- Slice: from `13.16.3 The SW-QPS algorithm` up to next detected section heading

---

13.16.3 The SW-QPS algorithm
The only difference between SW-QPS and SB-QPS is that SW-QPS changes the batch-switching oper-
ation of SB-QPS to a sliding-window switching operation. Sliding-window switching combines regular
switching with batch switching and achieves the better of both worlds, as follows. On the one hand,
during each time slot, under a sliding-window switching operation, there are T matchings under compu-
tation, just like under a batch-switching operation. Each such matching has had or will have a window
of T time slots to find opportunities to have its quality improved by the underlying bipartite matching
algorithm before it “graduates.”
     On the other hand, under a sliding-window switching operation, the “windows of opportunities” of
these T matchings are staggered so that one matching (“class”) is output (“graduated”) every time slot.
This matching is to be used as the crossbar configuration for the current time slot. In this respect it
behaves like a regular switching algorithm and hence completely eliminates the batching delay of batch
switching. More specifically, at the beginning of time slot t, the most senior matching (“class”) in the
window was added (“enrolled”) to the window at the end of time slot t − T − 1 and is to “graduate”
at the beginning of time slot t so its “window of opportunity” (to have its quality improved) is [t −
T , t − 1]. The “window of opportunity” for the second most senior matching is [t − T + 1, t] and so
on. At the end of time slot t, a “freshman class” (an empty matching) is “enrolled” and scheduled to
“graduate” at time slot t + T + 1 in the future.
     Fig. 13.15 shows how the sliding window evolves from time slot t to time slot t + 1. In Fig. 13.15
each interval along the timeline corresponds to a “class.” As shown there, at the beginning of time slot
t, the current window contains “classes of years” (matchings-under-computation to be used as crossbar
schedules for time slots) t, t + 1, · · · , and t + T − 1. Then, at the beginning of time slot t + 1, the
current window slides right by 1 (time slot), and the new window contains “classes of years” t + 1,
t + 2, · · · , and t + T because the “class of year t” just graduated and the “class of year t + T ” was just
“enrolled.”

362      Chapter 13 Switching

SW-QPS is a simple adaption of SB-QPS into the sliding-window switching framework. Each itera-
tion of SW-QPS is identical to that of SB-QPS. Hence SW-QPS has the same O(1) time complexity (per
port per matching computation) as SB-QPS. The only difference is that SW-QPS “graduates” a match-
ing in every time slot, whereas SB-QPS “batch-graduates” T matchings every T time slots. Clearly,
this “graduating a class each year” enables SW-QPS to completely eliminate the batching delay.
    SW-QPS inherits the FFA (first fit accepting) strategy of SB-QPS that is to arrange for an input-
output pairing – hence, the switching of a packet between the pair – at the earliest mutually available
time slot. In other words, an incoming packet is always “advanced to the most senior class that it can fit
in schedule-wise” so that it can “graduate” at the earliest “year” possible. This greedy strategy further
reduces the queuing delay of a packet, as shown in Meng et al. (2020).
