8.6.10

opensnoop

opensnoop(8) is a BCC and bpftrace tool that traces file opens. It is useful for discovering the
location of data files, log files, and configuration files. It can also discover performance problems caused by frequent opens, or help troubleshoot issues caused by missing files.

(Omitted in this processed extract: full MySQL startup open trace — see PDF.)

This output includes the startup of a MySQL database, and opensnoop has revealed the
configuration files, log file, data files (binary logs), and more.
opensnoop(8) works by only tracing the open(2) variant syscalls: open(2) and openat(2). The
overhead is expected to be negligible as opens are typically infrequent.

Options for the BCC version include: **-T** timestamps; **-x** failed opens only; **-p PID**; **-n NAME**
process-name filter.

The -x option can be used for troubleshooting: focusing on cases where applications are unable
to open files.

Origin note (book): first opensnoop 2004; BCC 2015; bpftrace 2018.
