# network-algorithmics-14-16-3-edge-aggregation-with-policing (chunk 000003)

(b) What is the service order of these packets under WFQ?
  (c) What is the service order of these packets under WF2 Q?
  (d) What is the service order of these packets under DRR when the quantum size is 3 bits?
 8. Reuse distance (Bennett and Kruskal, 1975) is a heavily studied concept in computer architecture
    and programming languages. Given a sequence of memory references (addresses accessed during
    the execution of a computer program), the reuse distance of a memory reference (say, to memory
    address a) is the number of distinct memory references that have happened between the previous ref-
    erence to a and this reference. For example, suppose the list of memory references is a, b, c, b, c, a.
    Then the reuse distance between the two consecutive references to a is 2, since only two distinct
    addresses, namely b and c, are referenced in between. Please design and implement in C++/C an
    augmented data structure that, given as input a long list of memory references (by a program), al-
    lows a companion algorithm to compute, for each memory access, its reuse distance in O(log N )
    time, where N is the number of distinct addresses in the list. (Hint: This augmented data structure
    subsumes one for implementing dynamic order statistics, which is the sole topic of Section 14.1
    in Cormen et al. (2009). Reading and understanding that section will make this problem much eas-
    ier to tackle.)
 9. As mentioned in Section 14.13, an augmented data structure and algorithm was proposed in Stoica
    and Abdel-Wahab (1995) for implementing the Earliest Eligible Virtual Deadline First (EEVDF)
    scheduling policy, in a computationally efficient manner. The EEVDF policy is used to schedule
    tasks in a system for service. Each task has a virtual deadline, that like a virtual time, is determined
    when this task arrives (to the system), and its value does not change thereafter. Each task also has a
    virtual eligible time te (that is also determined when the task arrives) in the sense when the current
    virtual time is at least te this task is eligible for service. The EEVDF policy is that, whenever the
    server becomes idle (right after finishing serving the current task), the scheduler needs to pick,
    among the eligible tasks (as determined by their eligible times), the one with the earliest virtual
    deadline for service. Now, please design an augmented data structure that can carry out the following
    three operations (and hence implements the EEVDF policy), all in O(log n) time, where n is the
    number of tasks in the system.
    • Insertion. When a new task arrives with a virtual eligible time and a virtual deadline, this method
      is called to insert the task into the data structure.
    • Searching. This method, with the current virtual time as its argument, is called when the sched-
      uler selects the next task for service. This method shall return, among the eligible tasks, the one
      with the earliest virtual deadline.
    • Deletion. This method is called to delete a task after the server finishes serving the task.
    Note in both insertion and deletion, rebalancing the base data structure (and correspondingly re-
    pairing the invariants of the augmented data structure) is necessary for guaranteeing O(log n) time
    complexity in the worse case. The design of this augmented data structure is much simpler than that
    of the shape data structure, so please refrain from reading Stoica and Abdel-Wahab (1995) while
    working on this problem.
10. Prove that the WF2 Q packet scheduling policy is work-conserving.
11. Construct a counterexample to show that the WF2 Q packet scheduling policy is not PIFO-
    compatible.

CHAPTER

Routers as distributed systems
                                                                                        15
                                                                           Come now and let us reason together.
                                                                                     —Isaiah 1:18, The Bible
