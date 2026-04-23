# A Philosophy of Software Design — deep modules

- Source: raw/code/pdf/a-philosophy-of-software-design.pdf
- Extraction: pdftotext -f 38 -l 42 -layout
- Slice: from `4.4 Deep modules` up to (excluding) `4.5 Shallow modules`

---

## PDF page 38

4.4 Deep modules
The best modules are those that provide powerful functionality yet have simple
interfaces. I use the term deep to describe such modules. To visualize the notion
of depth, imagine that each module is represented by a rectangle, as shown in
Figure 4.1. The area of each rectangle is proportional to the functionality
implemented by the module. The top edge of a rectangle represents the module’s
interface; the length of that edge indicates the complexity of the interface. The
best modules are deep: they have a lot of functionality hidden behind a simple
interface. A deep module is a good abstraction because only a small fraction of
its internal complexity is visible to its users.
     Module depth is a way of thinking about cost versus benefit. The benefit
provided by a module is its functionality. The cost of a module (in terms of
system complexity) is its interface. A module’s interface represents the
complexity that the module imposes on the rest of the system: the smaller and
simpler the interface, the less complexity that it introduces. The best modules are
those with the greatest benefit and the least cost. Interfaces are good, but more,
or larger, interfaces are not necessarily better!
     The mechanism for file I/O provided by the Unix operating system and its
descendants, such as Linux, is a beautiful example of a deep interface. There are
only five basic system calls for I/O, with simple signatures:
    int open(const char* path, int flags, mode_t permissions);
    ssize_t read(int fd, void* buffer, size_t count);
    ssize_t write(int fd, const void* buffer, size_t count);

---

## PDF page 39

off_t lseek(int fd, off_t offset, int referencePosition);
   int close(int fd);
The open system call takes a hierarchical file name such as /a/b/c and returns an
integer file descriptor, which is used to reference the open file. The other
arguments for open provide optional information such as whether the file is being
opened for reading or writing, whether a new file should be created if there is no
existing file, and access permissions for the file, if a new file is created. The read
and write system calls transfer information between buffer areas in the
application’s memory and the file; close ends the access to the file. Most files
are accessed sequentially, so that is the default; however, random access can be
achieved by invoking the lseek system call to change the current access position.
    A modern implementation of the Unix I/O interface requires hundreds of
thousands of lines of code, which address complex issues such as:

     How are files represented on disk in order to allow efficient access?
     How are directories stored, and how are hierarchical path names processed
     to find the files they refer to?
     How are permissions enforced, so that one user cannot modify or delete
     another user’s files?
     How are file accesses implemented? For example, how is functionality
     divided between interrupt handlers and background code, and how do these
     two elements communicate safely?
     What scheduling policies are used when there are concurrent accesses to
     multiple files?
     How can recently accessed file data be cached in memory in order to reduce
     the number of disk accesses?
     How can a variety of different secondary storage devices, such as disks and
     flash drives, be incorporated into a single file system?

    All of these issues, and many more, are handled by the Unix file system
implementation; they are invisible to programmers who invoke the system calls.
Implementations of the Unix I/O interface have evolved radically over the years,
but the five basic kernel calls have not changed.
    Another example of a deep module is the garbage collector in a language
such as Go or Java. This module has no interface at all; it works invisibly behind
the scenes to reclaim unused memory. Adding garbage collection to a system

---

## PDF page 40

actually shrinks its overall interface, since it eliminates the interface for freeing
objects. The implementation of a garbage collector is quite complex, but that
complexity is hidden from programmers.
    Deep modules such as Unix I/O and garbage collectors provide powerful
abstractions because they are easy to use, yet they hide significant
implementation complexity.
