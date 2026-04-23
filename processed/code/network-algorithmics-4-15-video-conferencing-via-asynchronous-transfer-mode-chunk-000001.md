# network-algorithmics-4-15-video-conferencing-via-asynchronous-transfer-mode (chunk 000001)

# Network Algorithmics — 4.15 Video conferencing via asynchronous transfer mode (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 132
- Slice: from `4.15 Video conferencing via asynchronous transfer mode` up to next detected section heading

---

4.15 Video conferencing via asynchronous transfer mode
In ATM, the network first sets up a VC through a series of switches before data can be sent. Standard
ATM allows one-to-many VCs, where a VC can connect a single source to multiple receivers. Any data
sent by the source is replicated and sent to every receiver in the one-to-many VC.
    Although it is not standardized, it is also easy to have many-to-many VCs, where every endpoint
can be both a source and a receiver. The idea is that when any source sends data, the switches replicate
the data to every receiver. Of course, the main problem in many-to-many VCs is that if two sources talk
at the same time, then the data from the two sources can be arbitrarily interleaved at the receivers and
cause confusion. This is possibly why many-to-many VCs are not supported by standards, though it is
often easy for switch hardware to support many-to-many VCs.
    Fig. 4.28 shows a simple topology consisting of an ATM switch that connects N workstations.
To showcase the bandwidth of the switch, the system designers have designed a videoconferencing
application. The conferencing application can allow users at any of the N workstations to have a video-
conference with each other. The application should bring up a screen (on every workstation in the
conference) that displays at least the current speaker and also plays the speech of the current speaker.
In addition, in the event of a conversation, it is desirable to see the expressions of the participants. The
designers soon run into the following problem.

106      Chapter 4 Principles in action

FIGURE 4.28
A videoconferencing system that uses an ATM switch with the ability to support many-to-many VCs.

Problem
The naivest solution would use up to N 2 point-to-point connections between every pair of participating
workstations. A better solution is shown in Fig. 4.28. It uses up to N many-to-many VCs between
each participating workstation and the other workstations. The video and speech of each workstation
is connected by a one-to-many VC to every other participating workstation. Thus every participating
workstation gets the video output of all participants and the application can choose which one (or ones)
to display. Unfortunately, the ATM switch requires that bandwidth on the switch be statically divided
among the N one-to-many VCs. Given a minimum bandwidth for video quality of Bmin and a total
switch bandwidth of B, this limits the number of participating workstations to be less than B/Bmin . Is
there a more scalable solution?

Hint: Consider exploiting the switch hardware’s ability to support many-to-many VCs (P4c). However,
to prevent confusion, only one source should transmit at a time in any many-to-many VC. Instead
of developing a complex protocol to ensure such a constraint, what hardware can be added (P5) to
ensure this constraint?
