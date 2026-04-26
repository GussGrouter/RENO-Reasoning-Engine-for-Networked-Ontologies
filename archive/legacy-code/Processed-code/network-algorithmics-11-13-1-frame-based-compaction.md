# Network Algorithmics — 11.13.1 Frame-based compaction (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 311
- Slice: from `11.13.1 Frame-based compaction` up to next detected section heading

---

11.13.1 Frame-based compaction
To show how simple local compaction schemes can be, we first describe an extremely simple scheme
that does minimal compaction and yet achieves 50% worst-case memory utilization. We then extend
this to improve utilization to closer to 100%.
                                                                                   M
     In frame merging, assume that all M words of memory are divided into Max          frames of size Max.
Frame merging seeks to keep the memory utilization to at least 50%. To do so, all nonempty frames
should be at least 50% full. Frame merging maintains the following simple invariant: All but one un-
                                                   M
filled frame is at least 50% full. If so, and if Max    is much larger than 1, this will yield a guaranteed
utilization of almost 50%.
     Allocate and deallocate requests are handled (Sikka and Varghese, 2000) with the help of tags added
to each word that help identify free memory and allocated blocks. The only additional restriction is that
all holes be contained within a frame; holes are not allowed to span frames.
     Call a frame flawed if it is nonempty but is less than 50% utilized. To maintain the invariant, frame
merging has one additional pointer to keep track of the current flawed frame, if any. Now, an allocate
could cause a previously empty frame to become flawed if the allocation is less than Max    2 .
     Similarly, a deallocate could cause a frame that was filled more than 50% to become less than 50%
full. For example, consider a frame that contains two allocated blocks of size 1 and size Max − 1
and hence has a utilization of 100%. The utilization could reduce to Max    1
                                                                                if the block of Max − 1 is
deallocated. This could cause two frames to become flawed, which would violate the invariant.
     A simple trick to maintain the invariant is as follows. Assume there is already a flawed frame F and
that a new flawed frame, F  , appears on the scene. The invariant is maintained by merging the contents

                                              11.14 Fixed Function Lookup-chip models                     285




FIGURE 11.17
Model of a lookup chip that does a search in hardware using a common SRAM that could be on or off chip. In some
cases, the external memory is cheap low-latency DRAM


of F and F  into F . This is clearly possible because both frames F and F  were less than half full. Note
that the only compaction done is local and is limited to the two flawed frames, F and F  . Such local
compaction leads to fast update times.
    The worst-case utilization of frame merging can be improved by increasing the frame size to kMax
and by changing the definition of a flawed frame to be one whose utilization is less than k +k 1 . The
scheme described earlier is a special case with k = 1. Increasing k improves the utilization, at the cost
of increased compaction. More complex allocators with even better performance are described in Sikka
and Varghese (2000).
