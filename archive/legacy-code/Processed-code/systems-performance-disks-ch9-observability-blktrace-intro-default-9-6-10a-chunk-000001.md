9.6.10

blktrace

blktrace(8) is a custom tracing facility for block device I/O events on Linux that uses the kernel
blktrace tracer. This is a specialized tracer controlled via BLKTRACE ioctl(2) syscalls to disk
device files. The frontend tools include blktrace(8), blkparse(1), and btrace(8).

475

476

Chapter 9 Disks

blktrace(8) enables kernel block driver tracing and retrieves the raw trace data, which can be
processed using blkparse(1). For convenience, the btrace(8) tool runs both blktrace(8) and
blkparse(1), such that the following are equivalent:
# blktrace -d /dev/sda -o - | blkparse -i # btrace /dev/sda

blktrace(8) is a low-level tool that shows multiple events per I/O.

Default Output
The following shows the default output of btrace(8) and captures a single disk read event by the
cksum(1) command:
# btrace /dev/sdb
8,16

3

1

0.429604145 20442

A

R 184773879 + 8 <- (8,17) 184773816

8,16

3

2

0.429604569 20442

Q

R 184773879 + 8 [cksum]

8,16

3

3

0.429606014 20442

G

R 184773879 + 8 [cksum]

8,16

3

4

0.429607624 20442

P

N [cksum]

8,16

3

5

0.429608804 20442

I

R 184773879 + 8 [cksum]

8,16

3

6

0.429610501 20442

U

N [cksum] 1

8,16

3

7

0.429611912 20442

D

R 184773879 + 8 [cksum]

8,16

1

1

0.440227144

C

R 184773879 + 8 [0]

0

[...]

Eight lines of output were reported for this single disk I/O, showing each action (event) involving
the block device queue and the device.
By default, there are seven columns:
1. Device major, minor number
2. CPU ID
3. Sequence number
4. Action time, in seconds
5. Process ID
6. Action identifier: the type of event (see the Action Identifiers heading)
7. RWBS description: I/O flags (see the RWBS Description heading)
These output columns may be customized using the -f option. They are followed by custom
data based on the action.
The final data depends on the action. For example, 184773879 + 8 [cksum] means an I/O at
block address 184773879 with size 8 (sectors), from the process named cksum.
