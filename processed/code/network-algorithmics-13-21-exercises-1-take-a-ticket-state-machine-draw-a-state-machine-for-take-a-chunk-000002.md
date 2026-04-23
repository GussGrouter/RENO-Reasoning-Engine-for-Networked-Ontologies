# network-algorithmics-13-21-exercises-1-take-a-ticket-state-machine-draw-a-state-machine-for-take-a (chunk 000002)

3. PIM unfairness: In the knockout example using just one tree can lead to unfairness; a collection of
   locally fair decisions can lead to global unfairness. Surprisingly, PIM can also lead to some form of
   unfairness (but not to persistent starvation). Consider a 2-by-2 switch, where input 1 has unlimited
   traffic to outputs 1 and 2, and input 2 has unlimited traffic to output 1.
   • Show that, on average, input 1 will get two grants from outputs 2 and 1 for half the cell slots and
     one grant (for output 2 only) for the remaining cell slots. What fraction of output 2’s link should
     input 1 receive?
   • Infer, based on the preceding fraction of output 1’s bandwidth, what input 1 receives on average
     versus input 2. Is this fair?
4. Motivating the iSLIP Pointer Increment Rule: The following is one unfairness scenario if point-
   ers in iSLIP are incremented incorrectly. For example, suppose in Fig. 13.10 that input port A always
   has traffic to output ports 1, 2, and 3, whose grant pointers are initialized to A. Suppose also that
   input ports B and C also always have traffic to 2. Thus initially A, B, and C all grant to 1, which
   chooses A. In the second iteration since input port 2 has traffic to B, 2 and B are matched.
   • Suppose B increments its grant pointer to 3 based on this second iteration match. Between which
     port pairs can traffic be continually starved if this scenario persists?
   • How does iSLIP prevent this scenario?
5. Clos Proof Revisited: The Clos proof is based on a reduction that looks and is simple. However,
   until you try a few twists that do not work, you may not appreciate its simplicity. In our reduction
   each iteration routed n pairs, one per input stage, using just one middle switch. Suppose instead that
   any set of middle switches is used that had free input and output links. Show, by counterexample,
   why the reduction does not work.
6. Benes Switch Load-Balancing Proof: In the Benes switch the chapter argued that any link one
   hop from the output cannot be overloaded, assuming perfect load balancing at the first stage. It is
   helpful to work out with some simple cases to provide intuition before turning, if needed, to the
   proof provided in Turner (1997).
   • Repeat the same proof for links one hop away from the network, but this time for a two-copy
     network. Does the proof change for a three-copy network?
   • Repeat all the proofs for links two hops away. Do you see a pattern that can now be stated
     algebraically (Turner, 1997)?
7. Avici TSR and 3D Grid Layout: It seems a good bet that layout and packaging will be increasingly
   important as switches scale up in speeds. Extend the layout drawing in Fig. 13.22 for a 1D torus to
   a 2D and a 3D torus. Then, read Dally (2002) to learn how the Avici TSR packages its 3D mesh in
   a box.
8. Switching Using iSLIP: As shown in Fig. 13.23, the switch is the same as shown in Fig. 13.8.
   However, the inputs and the starting values of accept–grant pointers are different. You need to show
   intermediate steps like in Figs. 13.8 and 13.9.
   • Please draw a cell transmission timing chart like Fig. 13.10.
   • Please write down the values of grant and accept pointers after the transmission of all these cells.

13.21 Exercises         381

FIGURE 13.23
Switching using iSLIP.

FIGURE 13.24
R(t).
