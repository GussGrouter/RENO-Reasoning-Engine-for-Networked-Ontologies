# network-algorithmics-6-4-4-speeding-up-select-without-changing-the-api (chunk 000002)

tors (e.g., newly opened sockets) must be checked. A third, subtle point is that even after network
    data has arrived for a socket (e.g., 1500 bytes), the application may read only 200 bytes. Thus a
    descriptor must be checked for readiness even after data first arrives, until there is no more data left
    (i.e., application reads all data) to signify readiness.
    To implement these ideas, besides the hints set H for each thread, the kernel implementation keeps
    two more sets. The first is an interest set I of all descriptors the thread is interested in. The second
    is a set of descriptors R that are known to be ready. The interest set I reflects long-term interest; for
    example, a socket is placed in I the first time it is mentioned in a select() call and is removed only
    when the socket is disconnected or reused. Let the set passed to select() be denoted by S. Then I
    is updated to Inew = Iold ∪ S. Note that this incorporates newly selected descriptors without losing
    previously selected descriptors.7
    Next, the kernel checks only those descriptors that are in Inew but are either (1) in the hints set H
    or (2) not in Iold or (3) in the old ready set Rold . Note that these three predicates reflect the three
    categories discussed two paragraphs back. They represent either recent activity, newly declared
    interest, or unconsumed data resulting from prior activity. The descriptors found by the check to be
    ready are recorded in Rnew . Finally, the select() call returns to the user the elements in Rnew ∩ S.
    This is because the user only cares about the readiness of descriptors specified in the selecting set S.
    As an example, socket 15 may be checked when it is first mentioned in a select() call and so enters
    I ; socket 15 may be checked next when a network packet of 500 bytes arrives, causing socket 15 to
    enter H ; finally, socket 15 may be checked repeatedly as part of R until the application consumes
    all 500 bytes, at which point socket 15 leaves R. The basis of this optimization is P12, adding state
    for speed. The optimization maintains state across calls (P12) to reduce redundant checks.
