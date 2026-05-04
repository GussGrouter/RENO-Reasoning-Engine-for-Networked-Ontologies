Action Identifiers
These are described in the blkparse(1) man page:
A

IO was remapped to a different device

B

IO bounced

C

IO completion

D

IO issued to driver

F

IO front merged with request on queue

G

Get request

I

IO inserted onto request queue

M

IO back merged with request on queue

P

Plug request

Q

IO handled by request queue code

S

Sleep request

T

Unplug due to timeout

U

Unplug request

X

Split

This list has been included because it also shows the events that the blktrace framework can
observe.

RWBS Description
For tracing observability, the kernel provides a way to describe the type of each I/O using a character string named rwbs. rwbs is used by blktrace(8) and other disk tracing tools. It is defined in
the kernel blk_fill_rwbs() function and uses the characters:
■

R: Read

■

W: Write

■

M: Metadata

■

S: Synchronous

■

A: Read-ahead

■

F: Flush or force unit access

■

D: Discard

■

E: Erase

■

N: None

The characters can be combined. For example, “WM” is for writes of metadata.

477

478

Chapter 9 Disks

Action Filtering
The blktrace(8) and btrace(8) commands can filter actions to show only the event type of interest.
For example, to trace only the D actions (I/O issued), use the filter option -a issue:
# btrace -a issue /dev/sdb
8,16

1

1

0.000000000

448

D

W 38978223 + 8 [kjournald]

8,16

1

2

0.000306181

448

D

W 104685503 + 24 [kjournald]

8,16

1

3

0.000496706

448

D

W 104685527 + 8 [kjournald]

8,16

1

1

0.010441458 20824

D

R 184944151 + 8 [tar]

[...]

Other filters are described in the blktrace(8) man page, including options to trace only reads (-a
read), writes (-a write), or synchronous operations (-a sync).
