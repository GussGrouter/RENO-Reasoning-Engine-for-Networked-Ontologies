# Systems Performance — Section 3.4 Linux (intro) (linux-intro-3-4) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.4 Linux
Linux was created in 1991 by Linus Torvalds as a free operating system for Intel personal computers. He announced the project in a Usenet post:
I’m doing a (free) operating system (just a hobby, won’t be big and professional like gnu)
for 386(486) AT clones. This has been brewing since April, and is starting to get ready. I’d
like any feedback on things people like/dislike in minix, as my OS resembles it somewhat
(same physical layout of the file-system (due to practical reasons) among other things).
This refers to the MINIX operating system, which was being developed as a free and small
(mini) version of Unix for small computers. BSD was also aiming to provide a free Unix version
although at the time it had legal troubles.

3.4 Linux

The Linux kernel was developed taking general ideas from many ancestors, including:
■

■

■

■

Unix (and Multics): Operating system layers, system calls, multitasking, processes, process priorities, virtual memory, global file system, file system permissions, device nodes,
buffer cache
BSD: Paged virtual memory, demand paging, fast file system (FFS), TCP/IP network stack,
sockets
Solaris: VFS, NFS, page cache, unified page cache, slab allocator
Plan 9: Resource forks (rfork), for creating different levels of sharing between processes
and threads (tasks)

Linux now sees widespread use for servers, cloud instances, and embedded devices including
mobile phones.

