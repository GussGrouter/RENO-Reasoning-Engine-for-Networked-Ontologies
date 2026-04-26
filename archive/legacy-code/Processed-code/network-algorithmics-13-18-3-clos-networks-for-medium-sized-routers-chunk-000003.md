# network-algorithmics-13-18-3-clos-networks-for-medium-sized-routers (chunk 000003)

What happens to a Clos network when k reduces from 2n − 1 to n? If k = n, the Clos network is
no longer nonblocking. Instead, the Clos network becomes what is called rearrangeably nonblocking.
In other words, the new input i can be connected to o as long as it’s possible to rearrange some of
the existing connections between inputs and outputs to use different middle-stage switches. A proof
and possible switching algorithm is described in Appendix A. It can be safely skipped by readers
uninterested in the theory.
    The bottom line behind all the math in Section A.3.1 in Appendix A is as follows. First, k = n is
clearly much more economical than k = 2n − 1 because it reduces the number of middle-layer switches
by a factor of two. However, while the Clos network is rearrangeably nonblocking, deterministic edge-
coloring algorithms for switch scheduling appear at this time to be quite complex. Second, the matching
proof for telephone calls assumes that all calls appear at the inputs at the same time; when a new call
arrives, existing calls have to be potentially rearranged to fit the new routes.

Clos networks and multichassis routers
Whereas the Clos network is required to be nonblocking or at least rearrangeably nonblocking for it
to be used for a telephone network, there is no such requirement for it to be used for a multichassis
router (i.e., a packet switch), due to a key difference between the two applications: a telephone switch
has no buffer, whereas a (small) packet switch does. Roughly speaking, requiring a Clos network to
be nonblocking, or rearrangeably nonblocking, equates to requiring it to achieve perfect load-balance
among the intermediate switches during every time slot, which is necessary where there is no buffering.

13.18 Scaling to larger and faster switches              369
