# network-algorithmics-12-15-exercises-1-range-to-prefix-mappings-cams-require-the-use-of-prefix-rang (chunk 000003)

In the early years of telephones the telephone operator helped knit together the social fabric of a com-
munity. If John wanted to talk to Martha, John would call the operator and ask for Martha; the operator
would then manually plug a wire into a patch panel that connected John’s telephone to Martha’s. The
switchboard, of course, allowed parallel connections between disjoint pairs. James could talk to Mary
at the same time that John and Martha conversed. However, each new call could be delayed for a brief
period while the operator finished putting through the previous call.
    When transistors were invented at Bell Labs, the fact that each transistor was basically a voltage-
controlled switch was immediately exploited to manufacture all-electronic telephone switches using an
array of transistors. The telephone operator was then relegated to functions that required human inter-
vention, such as making collect calls. The use of electronics greatly increased the speed and reliability
of telephone switches.
    A router is basically an automated post office for packets. Recall that we are using the word router
in a generic sense to refer to a general interconnection device, such as a gateway or a SAN switch.
Returning to the familiar model of a router in Fig. 13.1, recall that in essence a router is a box that
switches packets from input links to output links. The lookup process (B1 in Fig. 13.1) that determines
which output link a packet will be switched to was described in Chapter 11. The packet scheduling
done at the outbound link (B3 in Fig. 13.1) is described in Chapter 14. However, the guts of a router
remain its internal switching system (B2 in Fig. 13.1), which is discussed in this chapter.
    This chapter is organized as follows. Section 13.1 compares router switches to telephone switches.
Section 13.2 details the simplicity and limitations of a shared memory switch. Section 13.3 describes
router evolution, from shared buses to crossbars. Section 13.4 presents a simple matching algorithm
for a crossbar scheduler that was used in DEC’s first GigaSwitch product. Section 13.5 describes a
fundamental problem with DEC’s first GigaSwitch and other input-queued switches, called head-of-
line (HOL) blocking, which occurs when packets waiting for a busy output delay packets waiting for
idle outputs. Section 13.6 covers the knockout switch, which avoids HOL blocking, at the cost of some
complexity, by queuing packets at the output.
    Section 13.7 introduces the now standard solution approach to HOL blocking called virtual output
queueing (VOQ). The VOQ approach however leads to the problem of computing bipartite matchings,
introduced in Section 13.8, which is much more sophisticated and challenging than that in the case
of GigaSwitch. Section 13.9 presents the first such bipartite matching algorithm called PIM. PIM is a
randomized algorithm that retains the simplicity of input queuing; this scheme was deployed in DEC’s
second GigaSwitch product. Section 13.10 describes iSLIP, a scheme that appears to emulate PIM, but
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00020-8
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                  331

332      Chapter 13 Switching

FIGURE 13.1
Router model.
