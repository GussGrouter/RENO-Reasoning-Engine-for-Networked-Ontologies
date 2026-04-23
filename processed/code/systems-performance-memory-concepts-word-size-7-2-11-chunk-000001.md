7.2.11

Word Size

As introduced in Chapter 6, CPUs, processors may support multiple word sizes, such as 32-bit
and 64-bit, allowing software for either to run. As the address space size is bounded by the
addressable range from the word size, applications requiring more than 4 Gbytes of memory are
too large for a 32-bit address space and need to be compiled for 64 bits or higher.2
Depending on the kernel and processor, some of the address space may be reserved for kernel
addresses and is unavailable for application use. An extreme case is Windows with a 32-bit word
size, where by default 2 Gbytes is reserved for the kernel, leaving only 2 Gbytes for the application [Hall 09]. On Linux (or Windows with the /3GB option enabled) the kernel reservation is
1 Gbyte. With a 64-bit word size (if the processor supports it) the address space is so much larger
that the kernel reservation should not be an issue.
Depending on the CPU architecture, memory performance may also be improved by using
larger bit widths, as instructions can operate on larger word sizes. A small amount of memory
may be wasted, in cases where a data type has unused bits at the larger bit width.

2
There is also the Physical Address Extension (PAE) feature (workaround) for x86 allowing 32-bit processors to
access larger memory ranges (but not in a single process).
