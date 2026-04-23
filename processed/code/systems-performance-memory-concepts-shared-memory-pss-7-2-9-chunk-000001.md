7.2.9

Shared Memory

Memory can be shared between processes. This is commonly used for system libraries to save
memory by sharing one copy of their read-only instruction text with all processes that use it.
This presents difficulties for observability tools that show per-process main memory usage.
Should shared memory be included when reporting the total memory size of a process? One
technique in use by Linux is to provide an additional measure, the proportional set size (PSS),
which includes private memory (not shared) plus shared memory divided by the number of
users. See Section 7.5.9, pmap, for a tool that can show PSS.
