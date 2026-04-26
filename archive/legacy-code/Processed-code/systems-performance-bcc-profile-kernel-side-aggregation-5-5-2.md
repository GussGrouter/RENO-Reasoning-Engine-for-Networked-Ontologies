<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
0x7fbdac072040, len: 11, flags: DONTWAIT) = 11
0.788 ( 0.010 ms): mysqld/14097 sendto(fd: 37<socket:[833323]>, buff:
0x7fbdac072040, len: 11, flags: DONTWAIT) = 11
[...]

The output shows two 12664-byte sends followed by two 11-byte sends, all with the DONTWAIT
flag. If I saw a flood of small sends, I might wonder if performance could be improved by coalescing them, or avoiding the DONTWAIT flag.
While perf(1) trace can be used for some I/O profiling, I often wish to dig further into the arguments and summarize them in custom ways. For example, this sendto(2) trace shows the file
descriptor (37) and socket number (833323), but I’d rather see the socket type, IP addresses, and
ports. For such custom tracing, you can switch to bpftrace in Section 5.5.7, bpftrace.

5.5.2 profile
profile(8)11 is timer-based CPU profiler from BCC (Chapter 15). It uses BPF to reduce overhead by
aggregating stack traces in kernel context, and only passes unique stacks and their counts to user
space.
The following profile(8) example samples at 49 Hertz across all CPUs, for 10 seconds:
# profile -F 49 10
Sampling at 49 Hertz of all threads by user + kernel stack for 10 secs.
[...]
SELECT_LEX::prepare(THD*)
Sql_cmd_select::prepare_inner(THD*)
Sql_cmd_dml::prepare(THD*)
Sql_cmd_dml::execute(THD*)
mysql_execute_command(THD*, bool)
Prepared_statement::execute(String*, bool)
Prepared_statement::execute_loop(String*, bool)
mysqld_stmt_execute(THD*, Prepared_statement*, bool, unsigned long, PS_PARAM*)
dispatch_command(THD*, COM_DATA const*, enum_server_command)
do_command(THD*)
[unknown]

11
Origin: I developed profile(8) for BCC on 15-Jul-2016, based on code from Sasha Goldshtein, Andrew Birchall,
Evgeny Vereshchagin, and Teng Qin.

203


204

Chapter 5 Applications

[unknown]
