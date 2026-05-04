# network-algorithmics-6-2-avoiding-scheduling-overhead-in-networking-code (chunk 000002)

However, the transport-send process may not send data immediately because of flow control lim-
itations. When the flow control limits are removed (because of acks arriving), the Send Process will
execute the transport-send routine for this connection. The send call will first upcall the application
protocol, which exports a routine called display-get-data that actually provides the transport protocol
with the data for the application. This is advantageous because the application may have received more
keyboard data by the time the transport protocol is ready to send, and one might as well send as much
data as possible in a packet. Finally, within the context of the same process, transport adds a transport-
layer header and makes a call to the network protocol to actually send the packet.
    At the receiving end, the packet is received by the receive interrupt handler using a network-layer
routine called net-dispatch that needs to find which process to dispatch the received packet to. To find
out, net-dispatch makes an upcall to transport-get-port. This is a routine exported by the transport
layer that looks at port numbers in the header to figure out which application (e.g., FTP) must handle
the packet. Then a context switch is made and the Receive Handler relinquishes control and wakes
up the Receive Process, which executes network-layer functions, transport-layer functions, and finally
the application-level code to display the data. Note that a single process is executing all the layers of
protocol.
    The idea was a bit unusual at the time because the conventional dogma until that point was that layers
should only use services of layers below; thus calls between layers had, historically, been “downcalls.”
However, Clark pointed out that downcalls were perhaps required for protocol specifications but were
not the only alternative for protocol implementations. In our example in particular, upcalls are used to
obtain data (e.g., the upcall to display-get-data) and for advice from upper layers (upcall to transport-
get-port).
    While upcalls are commonly used in real implementations, there is probably no difference between
an upcall and a standard procedure call except for its possible novelty in the context of a networking
layered implementation. However, the more important idea, which is perhaps more lasting, is the idea
of using only one or two processes to process a message, each process consisting of routines from

6.2 Avoiding scheduling overhead in networking code                  151

two or more protocol layers. This idea found its way into systems like the x-kernel (Hutchinson and
Peterson, 1991) and into user-level networking, which is described in the next section.
    More generally, the idea of considering alternative implementation structures that preserve modular-
ity without sacrificing performance is a classic example of Principle P8, which says that implementors
should consider alternatives to reference implementations described in specifications. Notice that each
protocol layer can still be implemented modularly but the upcalled routines can be registered by upper
layers when the system starts up.
