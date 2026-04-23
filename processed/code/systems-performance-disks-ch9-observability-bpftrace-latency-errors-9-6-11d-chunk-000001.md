      Disk I/O Latency
      The disk response time, often referred to as disk I/O latency, can be measured by instrumenting
      device issue to completion events. The biolatency.bt tool does this, showing disk I/O latency as a
      histogram. For example:

      # biolatency.bt
      Attaching 4 probes...
      Tracing block device I/O... Hit Ctrl-C to end.
      ^C


      @usecs:
      [32, 64)                  2 |@                                                           |
      [64, 128)                 1 |                                                            |
      [128, 256)                1 |                                                            |
      [256, 512)               27 |@@@@@@@@@@@@@@@@@@@@@@@@@@                                  |
      [512, 1K)                43 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   |
      [1K, 2K)                 54 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
      [2K, 4K)                 41 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     |
      [4K, 8K)                 47 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               |
      [8K, 16K)                16 |@@@@@@@@@@@@@@@                                             |
      [16K, 32K)                4 |@@@                                                         |

      This output shows that I/O were typically completing between 256 microseconds and 16 milli-
      seconds (16K microseconds).

      The source code is:

      #!/usr/local/bin/bpftrace
      BEGIN
      {
                printf("Tracing block device I/O... Hit Ctrl-C to end.\n");
      }


      tracepoint:block:block_rq_issue
      {
                @start[args->dev, args->sector] = nsecs;
      }


      tracepoint:block:block_rq_complete
      /@start[args->dev, args->sector]/
      {
                @usecs = hist((nsecs - @start[args->dev, args->sector]) / 1000);
                delete(@start[args->dev, args->sector]);
      }
                                                                            9.6 Observability Tools        483


END
{
             clear(@start);
}

Measuring I/O latency requires storing a custom timestamp for the start of each I/O, and then
referring to it when the I/O has completed in order to calculate the elapsed time. When VFS
latency was measured in Chapter 8, File Systems, Section 8.6.15, bpftrace, the start timestamp
was stored in a BPF map keyed by the thread ID: that worked because the same thread ID will
be on CPU for the start and completion events. That is not the case with disk I/O, as the com-
pletion event will interrupt whatever else is on CPU. The unique ID in biolatency.bt has been
constructed from the device and sector number: it assumes that only one I/O will be in flight to
a given sector at a time.

As with the I/O size one-liner, you can add args->rwbs to the map key to break down by
I/O type.


Disk I/O Errors
I/O error status is an argument to the block:block_rq_complete tracepoint, and the following
bioerr(8) tool15 uses it to print details for I/O operations that error (a one-liner version of this was
included earlier):

#!/usr/local/bin/bpftrace


BEGIN
{
             printf("Tracing block I/O errors. Hit Ctrl-C to end.\n");
}


tracepoint:block:block_rq_complete
/args->error != 0/
{
             time("%H:%M:%S ");
             printf("device: %d,%d, sector: %d, bytes: %d, flags: %s, error: %d\n",
                   args->dev >> 20, args->dev & ((1 << 20) - 1), args->sector,
                   args->nr_sector * 512, args->rwbs, args->error);
}

Finding more information on a disk error may require lower-level disk tools, such as the next
three (MegaCli, smartctl, SCSI logging).




15
     Origin: I created it for the BPF book on 19-Mar-2019 [Gregg 19].
484   Chapter 9 Disks


