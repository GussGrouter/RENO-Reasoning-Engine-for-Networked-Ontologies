7.7

Exercises

1. Answer the following questions about memory terminology:
■

What is a page of memory?

■

What is resident memory?

■

What is virtual memory?

■

Using Linux terminology, what is the difference between paging and swapping?

2. Answer the following conceptual questions:
■

What is the purpose of demand paging?

■

Describe memory utilization and saturation.

■

What is the purpose of the MMU and the TLB?

■

What is the role of the page-out daemon?

■

What is the role of the OOM killer?

3. Answer the following deeper questions:
■

■

■

What is anonymous paging, and why is it more important to analyze than file system
paging?
Describe the steps the kernel takes to free up more memory when free memory becomes
exhausted on Linux-based systems.
Describe the performance advantages of slab-based allocation.

4. Develop the following procedures for your operating system:
■

■

A USE method checklist for memory resources. Include how to fetch each metric (e.g., which
command to execute) and how to interpret the result. Try to use existing OS observability
tools before installing or using additional software products.
Create a workload characterization checklist for memory resources. Include how to fetch
each metric, and try to use existing OS observability tools first.

7.8

References

5. Perform these tasks:
■

■

■

Choose an application, and summarize code paths that lead to memory allocation
(malloc(3)).
Choose an application that has some degree of memory growth (calling brk(2) or sbrk(2)),
and summarize code paths that lead to this growth.

■

Describe the memory activity visible in the included Linux vmstat training output.

**(Extended vmstat listing for exercise 5 omitted — see book PDF.)**

6. (optional, advanced) Find or develop metrics to show how well the kernel NUMA memory
locality policies are working in practice. Develop “known” workloads that have good or poor
memory locality for testing the metrics.
