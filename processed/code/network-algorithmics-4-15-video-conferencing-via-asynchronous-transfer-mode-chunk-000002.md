# network-algorithmics-4-15-video-conferencing-via-asynchronous-transfer-mode (chunk 000002)

Solution
As suggested in the hint, the designers chose to exploit the many-to-many VC capability of the switch
to replace N one-to-many VCs with a constant number of many-to-many VCs. This allowed the fixed
switch bandwidth to scale to a large number of participants. However, this generic idea requires elab-
oration. How many many-to-many VCs should be used? How is the potential confusion caused by
many-to-many VCs resolved? Here are the details of a solution worked out by Jon Turner at Washing-
ton University.
    First, consider the use of a single many-to-many VC named C. A naive solution to the confusion
problem entails a protocol (say, a round-robin protocol) that ensures that only one workstation at a time
connects its video output to C. Such protocols require coordination, and the coordination adds latency
and expense. Instead, as systems thinkers, the designers observed that, at a minimum, only the current
speaker needs to be displayed.

4.15 Video conferencing via asynchronous transfer mode                         107

FIGURE 4.29
Replacing N one-to-many VCs with two many-to-many VCs through the use of a speech detector and a simple
hardware state machine at each input.

Thus the designers added extra hardware (P5) in the form of a speech detector to the input at each
workstation. If the detector detects significant speech activity at a workstation X, then the detector
connects the video input of X to C; otherwise, the video input of X is not connected to C. Since this
hardware was quite cheap, the extra scalability came at a reasonable price.
    Next, the designers observed that keeping a video image of the last speaker provides visual con-
tinuity in the expected case when there is a dialog between two participants. Thus instead of one
many-to-many VC, they used two many-to-many VCs, C and L, one for the current speaker and one
for the last speaker, as shown in Fig. 4.29.

Exercises

• Write pseudocode (using some state variables) for the hardware at each workstation to update its
  connections to C and L. Assume the speech detector output is a function.
• What happens if more than one user speaks at one time? What could you add to the hardware state
  machine so that the application displays something reasonable? For instance, it would be unreason-
  able for the images of the two speakers to be morphed together in this case.

This page intentionally left blank

PART

Playing with endnodes
                                                                                   2
                                       The supreme accomplishment is to blur the line between work and play.
                                                                                           —Arnold Toynbee

The second part of the book deals with endnode algorithmics. This is the application of network algo-
rithmics to building fast protocol implementations at endnodes, especially at servers. If you like, you
can think of it as a systematic collection of techniques for building fast servers. The techniques are ap-
plied mostly in a software setting. Much of it has to do with getting around operating system structure
to enable high-speed data transfers. We study how to reduce the overhead incurred by copying, control
transfer, demultiplexing, timers, and other generic protocol-processing tasks.

This page intentionally left blank

CHAPTER

Copying data
                                                                                                                            5
                                                                           Copy from one, it’s plagiarism; copy from two, it’s research.
                                                                                                                      —Wilson Mizner
