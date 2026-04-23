8.6

Observability Tools

This section introduces file system observability tools for Linux-based operating systems. See the
previous section for strategies to follow when using these.

The tools in this section are listed in Table 8.6.

(Omitted in this processed extract: **Table 8.6** — observability tool index — see PDF.)

This is a selection of tools and capabilities to support Section 8.5, Methodology. It begins with
traditional and then covers tracing-based tools. Some of the traditional tools are likely available
on other Unix-like operating systems where they originated, including: mount(8), free(1), top(1),
vmstat(8), and sar(1). Many of the tracing tools are BPF-based, and use BCC and bpftrace frontends
(Chapter 15); they are: opensnoop(8), filetop(8), cachestat(8), ext4dist(8), and ext4slower(8).
See the documentation for each tool, including its man pages, for full references of its features.
