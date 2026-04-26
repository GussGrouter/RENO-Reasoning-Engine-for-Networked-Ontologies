8.3.12

Logical vs. Physical I/O

Although it may seem counterintuitive, I/O requested by applications to the file system (logical
I/O) may not match disk I/O (physical I/O), for several reasons.
File systems do much more than present persistent storage (the disks) as a file-based interface.
They cache reads, buffer writes, map files to address spaces, and create additional I/O to maintain the on-disk physical layout metadata that they need to record where everything is. This can
cause disk I/O that is unrelated, indirect, implicit, inflated, or deflated as compared to application I/O. Examples follow.

**(Subsections *Unrelated* / *Indirect* / *Implicit* / *Deflated* / *Inflated* — detailed bullet lists omitted here; see book PDF. The categories name *why* disk activity can diverge from application syscall-level stories.)**

Example
To show how these factors can occur in concert, the following example describes what can happen with a 1-byte application write:
1. An application performs a 1-byte write to an existing file.
2. The file system identifies the location as part of a 128 Kbyte file system record, which is
not cached (but the metadata to reference it is).
3. The file system requests that the record be loaded from disk.
4. The disk device layer breaks the 128 Kbyte read into smaller reads suitable for the device.
5. The disks perform multiple smaller reads, totaling 128 Kbytes.
6. The file system now replaces the 1 byte in the record with the new byte.
7. Sometime later, the file system or kernel requests that the 128 Kbyte dirty record be
written back to disk.
8. The disks write the 128 Kbyte record (broken up if needed).
9. The file system writes new metadata, for example, to update references (for copy-on-write)
or access time.
10. The disks perform more writes.
So, while the application performed only a single 1-byte write, the disks performed multiple
reads (128 Kbytes in total) and more writes (over 128 Kbytes).

