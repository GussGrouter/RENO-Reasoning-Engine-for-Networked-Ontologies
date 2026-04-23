Advanced Usage Analysis/Checklist
Additional characteristics are listed here as questions for consideration, which may also serve as
a checklist when studying memory issues thoroughly:
■

What is the working set size (WSS) for the applications?

■

Where is the kernel memory used? Per slab?

■

How much of the file system cache is active as opposed to inactive?

■

Where is the process memory used (instructions, caches, buffers, objects, etc.)?

■

Why are processes allocating memory (call paths)?

■

Why is the kernel allocating memory (call paths)?

325

326

Chapter 7 Memory

■

Anything odd with process library mappings (e.g., changing over time)?

■

What processes are actively being swapped out?

■

What processes have previously been swapped out?

■

Could processes or the kernel have memory leaks?

■

In a NUMA system, how well is memory distributed across memory nodes?

■

What are the IPC and memory stall cycle rates?

■

How balanced are the memory buses?

■

How much local memory I/O is performed as opposed to remote memory I/O?

The sections that follow can help answer some of these questions. See Chapter 2, Methodologies,
for a higher-level summary of this methodology and the characteristics to measure (who, why,
what, how).
