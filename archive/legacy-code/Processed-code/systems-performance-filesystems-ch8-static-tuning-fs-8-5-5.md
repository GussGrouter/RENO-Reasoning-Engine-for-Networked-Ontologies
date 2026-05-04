8.5.5 Static Performance Tuning
Static performance tuning focuses on issues of the configured environment. For file system
performance, Gregg provides a long static checklist: how many file systems are in use, record
size, atime, other mount/FS options (compression, encryption, etc.), page and supporting cache
configuration, second-level caches, storage device count and RAID layout, FS types and
versions, known bugs/patches, and I/O resource controls.

(Omitted in this processed extract: the full bullet checklist — see PDF.)

Answering these questions can reveal configuration choices that have been overlooked.
Sometimes a system has been configured for one workload, and then repurposed for another.
This method will remind you to revisit those choices.
