7.6.4 NUMA Binding
On NUMA systems, the numactl(8) command can be used to bind processes to NUMA nodes.
This can improve performance for applications that do not need more than a single NUMA node
of main memory. Example usage:
# numactl --membind=0 3161

This binds PID 3161 to NUMA node 0. Future memory allocations for this process will fail if they
cannot be satisfied from this node. When using this option, you should also investigate using
the --physcpubind option to also restrict CPU usage to CPUs connected to that NUMA node. I
commonly use both NUMA and CPU bindings to restrict a process to a single socket, to avoid
the performance penalty of CPU interconnect access.
Use numastat(8) (Section 7.5.6) to list available NUMA nodes.
