3.4.4 Extended BPF
BPF stands for Berkeley Packet Filter, an obscure technology first developed in 1992 that
improved the performance of packet capture tools [McCanne 92]. In 2013, Alexei Starovoitov
proposed a major rewrite of BPF [Starovoitov 13], which was further developed by himself and
Daniel Borkmann and included in the Linux kernel in 2014 [Borkmann 14b]. This turned BPF
into a general-purpose execution engine that can be used for a variety of things, including networking, observability, and security.
BPF itself is a flexible and efficient technology composed of an instruction set, storage objects
(maps), and helper functions. It can be considered a virtual machine due to its virtual instruction set specification. BPF programs run in kernel mode (as pictured earlier in Figure 3.2) and
are configured to run on events: socket events, tracepoints, USDT probes, kprobes, uprobes, and
perf_events. These are shown in Figure 3.16.

Figure 3.16 BPF components

121

122

Chapter 3 Operating Systems

BPF bytecode must first pass through a verifier that checks for safety, ensuring that the BPF
program will not crash or corrupt the kernel. It may also use a BPF Type Format (BTF) system for
understanding data types and structures. BPF programs can output data via a perf ring buffer, an
efficient way to emit per-event data, or via maps, which are suited for statistics.
Because it is powering a new generation of efficient, safe, and advanced tracing tools, BPF is
important for systems performance analysis. It provides programmability to existing kernel
event sources: tracepoints, kprobes, uprobes, and perf_events. A BPF program can, for example,
record a timestamp on the start and end of I/O to time its duration, and record this in a custom
histogram. This book contains many BPF-based programs using the BCC and bpftrace frontends. These front-ends are covered in Chapter 15.

