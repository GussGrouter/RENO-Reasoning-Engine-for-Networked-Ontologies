# network-algorithmics-11-2-1-threaded-indices-and-tag-switching (chunk 000003)

Life gets more exciting if R1 decides to “switch” packets going to D. R1 may decide to do so if, for
instance, there is a lot of traffic going to D. In that case R1 first picks an idle virtual circuit identifier
I , places the mapping I → L in its input port hardware, and then sends I back to R2. If R2 now sends
packets to D labeled with VCI I to the input port of R1, the input port looks up the mapping from I to
L and switches the packet directly to the output link L without going through the processor.
     Of course, R2 can repeat this switching process with the preceding router in the path, and so on.
Eventually, IP forwarding can be completely dispensed with in the switched portion of a sequence of
flow-switching routers.
     Despite its elegance, flow switching seems likely to work poorly in the backbone. This is because
backbone flows are short lived and exhibit poor locality. A contrarian opinion is presented in Molinero-
Fernandez and McKeown (2002) where the authors argue for the resurrection of flow switching based
on TCP connections. They claim that the current use of circuit-switched optical switches to link core
routers, the underutilization of backbone links running at 10% of capacity, and increasing optical band-
widths all favor the simplicity of circuit switching at higher speeds.
     Both IP and tag switching are techniques to finesse the need for IP lookups by passing information
in protocol headers. Like ATM, both schemes rely on passing indices (P10). However, tag switching
precomputes the index (P2a) at an earlier time scale (topology change time) than ATM (just before data
transfer). On the other hand, in IP switching the indices are computed on demand (P2c, lazy evaluation)
after the data begins to flow. However, neither tag nor IP switching completely avoids prefix lookups,
and each adds a complex protocol. We now look afresh at the supposed complexity of IP lookups.
