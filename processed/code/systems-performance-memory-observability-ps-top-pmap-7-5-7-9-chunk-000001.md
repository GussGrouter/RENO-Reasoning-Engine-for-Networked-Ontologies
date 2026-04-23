7.5.7

ps

The process status command, ps(1), lists details on all processes, including memory usage statistics. Its usage was introduced in Chapter 6, CPUs.
For example, using the BSD-style options:
$ ps aux
USER

PID %CPU %MEM

VSZ

RSS TTY

STAT START

TIME COMMAND

[...]
bind

1152

0.0

0.4 348916 39568 ?

Ssl

Mar27

20:17 /usr/sbin/named -u bind

root

1371

0.0

0.0

2652 ?

Ss

Mar27

11:04 /usr/lib/postfix/master

0.6 207564 50684 ?

Sl

Mar27

1:57 /usr/sbin/console-kit-

S

Mar27

0:49 /usr/lib/erlang/erts-

Ssl

Mar27 453:29 /usr/lib/erlang/erts-

root
1386 0.0
daemon --no-daemon

rabbitmq 1469 0.0 0.0
5.7.4/bin/epmd -daemon

39004

10708

172 ?

rabbitmq 1486 0.1 0.0 150208 2884 ?
5.7.4/bin/beam.smp -W w -K true -A30 ...

This output includes the following columns:
■

%MEM: Main memory usage (physical memory, RSS) as a percentage of the total in the system

■

RSS: Resident set size (Kbytes)

■

VSZ: Virtual memory size (Kbytes)

While RSS shows main memory usage, it includes shared memory segments such as system
libraries, which may be mapped by dozens of processes. If you were to sum the RSS column,
you might find that it exceeds the memory available in the system, due to overcounting of this
shared memory. See Section 7.2.9, Shared Memory, for background on shared memory, and the
later pmap(1) command for analysis of shared memory usage.
These columns may be selected using the SVR4-style -o option, for example:
# ps -eo pid,pmem,vsz,rss,comm
PID %MEM

VSZ

RSS COMMAND

[...]
13419

0.0 5176 1796 /opt/local/sbin/nginx

335

336

Chapter 7 Memory

13879

0.1 31060 22880 /opt/local/bin/ruby19

13418

0.0 4984 1456 /opt/local/sbin/nginx

15101

0.0 4580

10933

0.0 3124 2212 /usr/sbin/rsyslogd

32 /opt/riak/lib/os_mon-2.2.6/priv/bin/memsup

[...]

The Linux version can also print columns for major and minor faults (maj_flt, min_flt).
The output of ps(1) can be post-sorted on the memory columns so that the highest consumers
can be quickly identified. Or, try top(1), which provides interactive sorting.

7.5.8 top
The top(1) command monitors top running processes and includes memory usage statistics. It
was introduced in Chapter 6, CPUs. For example, on Linux:
$ top -o %MEM
top - 00:53:33 up 242 days,
Tasks: 261 total,
Cpu(s):

2:38,

7 users,

load average: 1.48, 1.64, 2.10

0.0%us,

1 running, 260 sleeping,
0.0%sy,

0 stopped,

0.0%ni, 99.9%id,

0.0%wa,

0 zombie

0.0%hi,

0.0%si,

8181740k total,

6658640k used,

1523100k free,

404744k buffers

Swap:

2932728k total,

120508k used,

2812220k free,

2893684k cached

0.0%st

Mem:

VIRT

RES

SHR S %CPU %MEM

PID USER

PR

NI

29625 scott

20

0 2983m 2.2g 1232 S

45 28.7

5121 joshw

20

0

222m 193m

1386 root

20

0

202m

6371 stu

20

TIME+

COMMAND

81:11.31 node

804 S

0

2.4 260:13.40 tmux

49m 1224 S

0

0.6

1:57.70 console-kit-dae

0 65196

38m

292 S

0

0.5

23:11.13 screen
20:17.36 named

1152 bind

20

0

38m 1700 S

0

0.5

15841 joshw

20

0 67144

340m

23m

908 S

0

0.3 201:37.91 mosh-server

18496 root

20

0 57384

16m 1972 S

3

0.2

2:59.99 python

1258 root

20

0

125m 8684 8264 S

0

0.1

2052:01 l2tpns

16295 wesolows

20

0 95752 7396

944 S

0

0.1

4:46.07 sshd

23783 brendan

20

0 22204 5036 1676 S

0

0.1

0:00.15 bash

[...]

The summary at the top shows total, used, and free for both main memory (Mem) and virtual
memory (Swap). The sizes of the buffer cache (buffers) and page cache (cached) are also shown.
In this example, the per-process output has been sorted on %MEM using -o to set the sort column.
The largest process in this example is node, using 2.2 Gbytes of main memory and almost 3 Gbytes
of virtual memory.
The main memory percentage column (%MEM), virtual memory size (VIRT), and resident set size
(RES) have the same meanings as the equivalent columns from ps(1) described earlier. For more

7.5 Observability Tools

details on top(1) memory statistics, see the section “Linux Memory Types” in the top(1) man
page, which explains what type of memory is shown by each of the possible memory columns.
You can also type “?” when using top(1) to see its built-in summary of interactive commands.

7.5.9

pmap

The pmap(1) command lists the memory mappings of a process, showing their sizes, permissions,
and mapped objects. This allows process memory usage to be examined in more detail, and
shared memory to be quantified.
For example, on a Linux-based system:
# pmap -x 5187
5187:

/usr/sbin/mysqld

Address

Kbytes

RSS

000055dadb0dd000

58284

10748

Dirty Mode

0 r-x-- mysqld

Mapping

000055dade9c8000

1316

1316

1316 r---- mysqld

000055dadeb11000

3592

816

764 rw--- mysqld

000055dadee93000

1168

1080

1080 rw---

[ anon ]

000055dae08b5000

5168

4836

4836 rw---

[ anon ]

00007f018c000000

4704

4696

4696 rw---

[ anon ]

00007f018c498000

60832

0

0 -----

[ anon ]

00007f0190000000

132

24

24 rw---

[ anon ]

[...]
00007f01f99da000

4

4

0 r---- ld-2.30.so

00007f01f99db000

136

136

0 r-x-- ld-2.30.so

00007f01f99fd000

32

32

0 r---- ld-2.30.so

00007f01f9a05000

4

0

0 rw-s- [aio] (deleted)

00007f01f9a06000

4

4

4 r---- ld-2.30.so

00007f01f9a07000

4

4

4 rw--- ld-2.30.so

00007f01f9a08000

4

4

4 rw---

[ anon ]

00007ffd2c528000

132

52

52 rw---

[ stack ]

00007ffd2c5b3000

12

0

0 r----

[ anon ]

00007ffd2c5b6000

4

4

0 r-x--

[ anon ]

ffffffffff600000

4

0

0 --x--

[ anon ]

---------------- ------- ------- ------total kB

1828228

450388

434200

This shows the memory mappings of a MySQL database server, including virtual memory
(Kbytes), main memory (RSS), private anonymous memory (Anon), and permissions (Mode). For
many of the mappings, very little memory is anonymous, and many mappings are read-only
(r-...), allowing those pages to be shared with other processes. This is especially the case for
system libraries. The bulk of the memory consumed in this example is in the heap, shown as the
first wave of [ anon ] segments (truncated in this output).

337

338

Chapter 7 Memory

The -x option prints extended fields. There is also -X for even more details, and -XX for “everything” the kernel provides. Just showing the headers for these modes:
# pmap -X $(pgrep mysqld) | head -2
5187:

/usr/sbin/mysqld

Address Perm
Offset Device
Inode
Size
Rss
Pss Referenced
Anonymous LazyFree ShmemPmdMapped Shared_Hugetlb Private_Hugetlb Swap SwapPss Locked
THPeligible ProtectionKey Mapping
[...]
# pmap -XX
5187:

$(pgrep mysqld) | head -2

/usr/sbin/mysqld

Address Perm
Offset Device
Inode
Size KernelPageSize MMUPageSize
Rss
Pss Shared_Clean Shared_Dirty Private_Clean Private_Dirty Referenced Anonymous
LazyFree AnonHugePages ShmemPmdMapped Shared_Hugetlb Private_Hugetlb Swap SwapPss
Locked THPeligible ProtectionKey
VmFlags Mapping
[...]

These extra fields are kernel version dependent. They include details of huge page use, swap use,
and the proportional set size (Pss) for mappings (highlighted). PSS shows how much private
memory a mapping has, plus shared memory divided by the number of users. This provides a
more realistic value for the main memory usage.

