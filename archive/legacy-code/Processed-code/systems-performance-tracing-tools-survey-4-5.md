<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (book PDF region ~171–220) -->

made

a

direct

SYN-RCVD state from the LISTEN state

per second [tcpPassiveOpens].
iseg/s
The total number of segments received per second, including

those

received

in

error

[tcpInSegs].

This count

includes segments received on currently established

con-

nections.
[...]

Specific uses of sar(1) are described later in this book; see Chapters 6 to 10. Appendix C is a summary of the sar(1) options and metrics.

4.5 Tracing Tools
Linux tracing tools use the previously described events interfaces (tracepoints, kprobes, uprobes,
