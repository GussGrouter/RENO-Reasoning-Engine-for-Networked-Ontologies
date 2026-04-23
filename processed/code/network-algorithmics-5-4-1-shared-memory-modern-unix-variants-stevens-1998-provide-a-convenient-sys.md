# Network Algorithmics — 5.4.1 Shared memory Modern UNIX variants (Stevens, 1998) provide a convenient system call known as mmap() to allow an (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 158
- Slice: from `5.4.1 Shared memory Modern UNIX variants (Stevens, 1998) provide a convenient system call known as mmap() to allow an` up to next detected section heading

---

5.4.1 Shared memory
Modern UNIX variants (Stevens, 1998) provide a convenient system call known as mmap() to allow an
application such as a server to map a file into its VM address space. Other operating systems provide
equivalent functions. Conceptually, when a file is mapped into an application’s address space, it is as if
the application has cached a copy of the file in its memory. This seems redundant because the file system
also maintains cached files. However, using the magic of VM (P4, leverage off system components),
the cached file is really only a set of mappings, so other applications and the file server cache can gain
common access to one set of physical pages for the file.
    The Flash Web server (Pai et al., 1999a) avoids Copy 1 and Copy 2 in Fig. 5.1 by having the server
application map frequently used files into memory. Given that there are limits on the number of physical
pages that can be allocated to file pages and limits on page table mappings, the Flash Web server has to
treat these mapped files as a cache. Instead of caching whole files, it caches segments of files and uses
an LRU (least recently used) policy to unmap files that have not been used for a while.
    Note that such cache maintenance functions are duplicated by the file system cache (which has a
more precise view of resources such as free pages because it is kernel resident). However, this can be
looked on as a necessary evil to avoid Copies 1 and 2 in Fig. 5.1. While Flash uses mmap() to avoid file
system copying, it runs over the UNIX API. Hence, Flash is constrained to make an extra copy in the
network subsystem (Copy 3 in Fig. 5.1). Just when progress is being made to eliminate Copy 2, pesky
Copy 3 reappears again!
    Copy 3 can be avoided by combining emulated copying using TCOW (Brustoloni and Steenkiste,
1996) with mmap(). However, this has some of the disadvantages of TCOW mentioned earlier. It is
also not a complete solution that generalizes to avoid copying for interaction with a CGI process via a
UNIX pipe.

132        Chapter 5 Copying data
