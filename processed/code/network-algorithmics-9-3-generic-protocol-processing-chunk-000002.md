# network-algorithmics-9-3-generic-protocol-processing (chunk 000002)

FIGURE 9.7
TCP header fields: the fields most likely to change are the checksum and the ack fields. The other fields carry very
little information and can often be predicted from past values.

IF (No unexpected flags) AND (Window in packet is as before)
AND (Packet sequence number is the next expected) THEN
    IF (Packet contains only headers and no data)
    Do Ack Processing
/* Release acked bytes, stop timers, awaken process */
ELSE IF (Packet does not ack anything new) /* pure data */
    Copy data to user buffer while checksumming;
    Update next sequence number expected;
    Send Acks if needed and release buffer;
ENDIF
ELSE /* header prediction failed -\/- take long path */
...

Clearly, this code is considerably shorter than the complete TCP receive processing code. However,
some of the checks can be made more efficient by leveraging off the fact that most machines can do
efficient comparisons in units of a machine word size (P4a, exploit locality).
     For example, consider the TCP flags contained in the control bits of Fig. 9.7. There are six flags,
each encoded as a bit: SYN, FIN, RESET, PUSH, URG, ACK. If it is business as usual, all the flags
must be clear, with the exception of ACK, which must be set, and PUSH, which is irrelevant. Checking
for each of these conditions individually would require several instructions to extract and compare each
bit.
     Instead, observe that the flags field is the fourth word of the TCP header and that the window size is
contained in the last 16 bits. In the header prediction code the sender precomputes (P2a) the expected
value of this word by filling in all the expected values of the flag and using the last advertised value of
the window size.
     The expected value of the fourth TCP header word is stored in the PCB entry for the connection.
Given this setup, the first two checks in the pseudocode shown earlier can be accomplished in one
stroke by comparing the fourth word of the TCP header in the incoming packet with the expected value
stored in the PCB. If all goes well, and tests indicate they often do, the expected value of the fourth
field is computed only at the start of the connection. It is this test that explains the origin of the name
header prediction: a portion of the header is being predicted and checked against an incoming segment.

226      Chapter 9 Protocol processing
