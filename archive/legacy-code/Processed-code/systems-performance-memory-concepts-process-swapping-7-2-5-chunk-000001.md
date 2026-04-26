7.2.5

Process Swapping

Process swapping is the movement of entire processes between main memory and the physical
swap device or swap file. This is the original Unix technique for managing main memory and is
the origin of the term swap [Thompson 78].
To swap out a process, all of its private data must be written to the swap device, including the
process heap (anonymous data), its open file table, and other metadata that is only needed when
the process is active. Data that originated from file systems and has not been modified can be
dropped and read from the original locations again when needed.

Process swapping severely hurts performance, as a process that has been swapped out requires
numerous disk I/O to run again. It made more sense on early Unix for the machines of the time,
such as the PDP-11, which had a maximum process size of 64 Kbytes [Bach 86]. (Modern systems
allow process sizes measured in the Gbytes.)
This description is provided for historical background. Linux systems do not swap processes at
all and rely only on paging.
