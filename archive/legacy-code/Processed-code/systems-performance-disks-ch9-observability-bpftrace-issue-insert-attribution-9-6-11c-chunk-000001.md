The tracepoint block:block_rq_issue shows when I/O were sent to the device driver for delivery to
the disk device. There is no guarantee that the originating process is still on CPU, especially if the
I/O is queued by a scheduler, so the process name shown may be for a later kernel worker thread
that reads I/O from a queue for device delivery. You can switch the tracepoint to block:block_rq_
insert to measure from the insertion of the queue, which may improve the accuracy of the process
name, but it may also miss instrumenting I/O that bypasses queueing (this was also mentioned in
Section 9.6.5, perf).
If you add args->rwbs as a histogram key, the output will be further broken down by I/O type:
# bpftrace -e 't:block:block_rq_insert /args->bytes/ { @[comm, args->rwbs] =
hist(args->bytes); }'
Attaching 1 probe...
^C
[...]
@[dmcrypt_write, WS]:
[4K, 8K)

4 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

[8K, 16K)

1 |@@@@@@@@@@@@@

|

[16K, 32K)

0 |

|

[32K, 64K)

1 |@@@@@@@@@@@@@

|

[64K, 128K)

1 |@@@@@@@@@@@@@

|

[128K, 256K)

1 |@@@@@@@@@@@@@

|

[512K, 1M)

8 |@@@@@@@@@@

|

[1M, 2M)

38 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

@[dmcrypt_write, W]:

The output now includes W for writes, WS for synchronous writes, etc. See the earlier RWBS
Description section for an explanation of these letters.

481

