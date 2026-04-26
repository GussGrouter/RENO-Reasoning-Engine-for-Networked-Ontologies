# network-algorithmics-13-10-avoiding-randomization-with-islip (chunk 000002)

Similarly, iSLIP provides fairness by choosing the next winner among multiple contenders in round-
robin fashion using a rotating pointer. While the round-robin pointers can be initially synchronized and
cause something akin to HOL blocking, they tend to break free and result in maximal matchings over
the long run, at least as measured in simulation. Thus the subtlety in iSLIP is not the use of round-
robin pointers but the apparent lack of long-term synchronization among N such pointers running
concurrently.
    More precisely, each output (respectively input) maintains a pointer g initially set to the first input
(respectively output) port. When an output has to choose between multiple input requests, it chooses
the lowest input number that is equal to or greater than g. Similarly, when an input port has to choose
between multiple output-port requests, it chooses the lowest output-port number that is equal to or
greater than a, where a is the pointer of the input port. If an output port is matched to an input port X,
then the output-port pointer is incremented to the first port number greater than X in circular order (i.e.,
g becomes X + 1, unless X was the last port, in which case g wraps around to the first port number).
    This simple device of a “rotating priority” assures that each resource (output port, input port) is
shared reasonably fairly across all contenders at the cost of 2N extra log2 N pointers, in addition to the
N 2 scheduling state needed on every iteration.
    Figs. 13.8 and 13.9 show the same scenario as in Fig. 13.7 (and Fig. 13.5), but using a two-iteration
iSLIP. Since each row is an iteration of a match, each match is shown using two rows. Thus the three
rows of Fig. 13.8 show the first 1.5 matches of the scenario. Similarly, Fig. 13.9 shows the remaining
1.5 matches.
    The upper left diagram of Fig. 13.8 is identical to Fig. 13.7, in that each input port sends requests
to each output port for which it has a cell destined. However, one difference is that each output port
has a so-called grant pointer g, which is initialized for all outputs to be A. Similarly, each input has a
so-called accept pointer called a, which is initialized for all inputs to 1.
    The determinism of iSLIP causes a divergence immediately in the Grant phase. Compare the upper
middle of Fig. 13.8 with the upper middle of Fig. 13.7. For example, when output 1 receives requests
from all three input ports, it grants to A because A is the smallest input greater than or equal to g1 = A.
By contrast, in Fig. 13.7 port 1 randomly chooses input port B. At this stage, the determinism of iSLIP
seems a real disadvantage because A has sent requests to both output ports 3 and 4. Because 3 and 4
also have grant pointers g3 = g4 = A, ports 3 and 4 grant to A as well, ignoring the claims of B and C.
As before, since C is the lone requester for port 4, C gets the grant from 4.
    When the popular A gets three grants back from ports 1, 2, and 3, A accepts 1. This is because port
1 is the first output equal to greater than A’s accept pointer, aA , which was equal to 1. Similarly C
chooses 4. Having done so, A increments aA to 2, and C increments aC to 1 (1 greater than 4 in circular
order is 1). Only at this stage does output 1 increment its grant pointer, g1 , to B (1 greater than the last
successful grant) and port 4 similarly increments to A (1 greater than C in circular order).
    Note that, although ports 2 and 3 gave grants to A, they do not increment their grant pointers because
A spurned their grants. If they did, it would be possible to construct a scenario where output ports keep
incrementing their grant pointer beyond some input port I after unsuccessful grants, thereby continually
starving input port I . Note also that the match is only of size 2; thus unlike Fig. 13.7, this iSLIP scenario
can be improved by a second iteration, shown in the second row of Fig. 13.8. Notice that, at the end
of the first iteration, the matched inputs and outputs are not connected by solid lines (denoting data
transfer), as shown at the top right of Fig. 13.7. This data transfer will await the end of the final (in this
case second) iteration.
