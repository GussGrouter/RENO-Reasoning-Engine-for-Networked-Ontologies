
0.00

104.00

119.00

03:09:09 PM

0.00

0.00

70.00

70.00

Average:

0.20

0.00

84.60

76.80

(8 CPU)

Data collecting is intended for long intervals, such as five or ten minutes, whereas live reporting
allows you to look at per-second variation.
Later chapters include various examples of live sar(1) statistics.

4.4.4

sar(1) Documentation

The sar(1) man page documents the individual statistics and includes SNMP names in square
brackets. For example:
$ man sar
[...]
active/s
The number of times TCP connections have
transition

to

the

made

a

direct

SYN-SENT state from the CLOSED state

per second [tcpActiveOpens].

165

166

Chapter 4 Observability Tools

passive/s
The number of times TCP connections have
transition

to

