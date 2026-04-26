9.6.11

bpftrace

bpftrace is a BPF-based tracer that provides a high-level programming language, allowing the
creation of powerful one-liners and short scripts. It is well suited for custom disk analysis based
on clues from other tools.
bpftrace is explained in Chapter 15. This section shows some examples for disk analysis: oneliners, disk I/O size, and disk I/O latency.

One-Liners
The following one-liners are useful and demonstrate different bpftrace capabilities.
Count block I/O tracepoints events:
bpftrace -e 'tracepoint:block:* { @[probe] = count(); }'

Summarize block I/O size as a histogram:
bpftrace -e 't:block:block_rq_issue { @bytes = hist(args->bytes); }'

Count block I/O request user stack traces:
bpftrace -e 't:block:block_rq_issue { @[ustack] = count(); }'
bpftrace -e 't:block:block_rq_insert { @[ustack] = count(); }'

479

480

Chapter 9 Disks

Count block I/O type flags:
bpftrace -e 't:block:block_rq_issue { @[args->rwbs] = count(); }'

Trace block I/O errors with device and I/O type:
bpftrace -e 't:block:block_rq_complete /args->error/ {
printf("dev %d type %s error %d\n", args->dev, args->rwbs, args->error); }'

Count SCSI opcodes:
bpftrace -e 't:scsi:scsi_dispatch_cmd_start { @opcode[args->opcode] =
count(); }'

Count SCSI result codes:
bpftrace -e 't:scsi:scsi_dispatch_cmd_done { @result[args->result] = count(); }'

Count SCSI driver functions:
bpftrace -e 'kprobe:scsi* { @[func] = count(); }'

