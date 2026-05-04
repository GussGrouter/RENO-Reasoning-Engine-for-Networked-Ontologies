7.3.3

Process Virtual Address Space

Managed by both hardware and software, the process virtual address space is a range of virtual
pages that are mapped to physical pages as needed. The addresses are split into areas called segments for storing the thread stacks, process executable, libraries, and heap. Examples for 32-bit
processes on Linux are shown in Figure 7.10, for both x86 and SPARC processors.
On SPARC the kernel resides in a separate full address space (which is not shown in Figure 7.10).
Note that on SPARC it is not possible to distinguish between a user and kernel address based
only on the pointer value; x86 employs a different scheme where the user and kernel addresses
are non-overlapping.5
The program executable segment contains separate text and data segments. Libraries are also
composed of separate executable text and data segments. These different segment types are:
■

■

■

■

Executable text: Contains the executable CPU instructions for the process. This is
mapped from the text segment of the binary program on the file system. It is read-only
with the execute permission.
Executable data: Contains initialized variables mapped from the data segment of the
binary program. This has read/write permissions so that the variables can be modified
while the program is running. It also has a private flag so that modifications are not
flushed to disk.
Heap: This is the working memory for the program and is anonymous memory (no file
system location). It grows as needed and is allocated via malloc(3).
Stack: Stacks of the running threads, mapped read/write.

5
Note that for 64-bit addresses, the full 64-bit range may not be supported by the processor: the AMD specification
allows implementations to only support 48-bit addresses, where the unused higher-order bits are set to the last bit:
this creates two usable address ranges, called canonical address, of 0 to 0x00007fffffffffff, used for user space, and
0xffff800000000000 to 0xffffffffffffffff, used for kernel space. This is why x86 kernel addresses begin with 0xffff.

Figure 7.10 Example process virtual memory address space
The library text segments may be shared by other processes that use the same library, each of
which has a private copy of the library data segment.
