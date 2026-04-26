# network-algorithmics-13-21-exercises-1-take-a-ticket-state-machine-draw-a-state-machine-for-take-a (chunk 000001)

# Network Algorithmics — 13.21 Exercises 1. Take-a-Ticket State Machine: Draw a state machine for take-a-ticket. Describe the state machine (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 406
- Slice: from `13.21 Exercises 1. Take-a-Ticket State Machine: Draw a state machine for take-a-ticket. Describe the state machine` up to next detected section heading

---

13.21 Exercises
1. Take-a-Ticket State Machine: Draw a state machine for take-a-ticket. Describe the state machine
   using pseudocode, with a state machine for each sender and each receiver. Extend the state machine
   to handle hunt groups.
2. Knockout Implementation: There are dependencies between the knockout trees. The simplest im-
   plementation passes all the losers from the Position j − 1 tree to the Position j tree. This would take
   k log N gate delays because each tree takes log N gate delays. Find a way to pipeline this process
   such that Tree j begins to work on each batch of losers as they are determined by Tree j − 1, as
   opposed to waiting for all losers to be determined. Draw your implementation using 2-by-2 concen-
   trators as your building block and estimate the worst-case delay in concentrator delays.

380      Chapter 13 Switching
