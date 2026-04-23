8.6.11

filetop

filetop(8) is a BCC tool that is like top(1) for files, showing the most frequently read or written
filenames.

(Omitted in this processed extract: full `filetop` and `filetop -a` ASCII tables — see PDF.)

By default, the top twenty files are shown, sorted by the read bytes column. Example interpretation:
the top line may show **mysqld** doing hundreds of reads from a large `.ibd` tablespace file.

This tool is used for workload characterization and general file system observability. Just as you
can discover an unexpected CPU-consuming process using top(1), this may help you discover an
unexpected I/O-busy file.

filetop by default also only shows regular files. The **-a** option shows all files, including TCP
sockets and device nodes (types include **O** “other” such as `/dev/ptmx`, **S** sockets).

Options include **-C** (rolling output, no clear—author prefers this for scrollback), **-a** all file types,
**-r ROWS**, **-p PID**.

The screen is refreshed every second (like top(1)) unless -C is used.

Origin note (book): BCC filetop created 2016.
