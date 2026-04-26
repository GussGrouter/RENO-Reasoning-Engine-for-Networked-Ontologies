# systems-performance-tuning-efforts-2-3-4 (chunk 000001)

# Systems Performance — 2.3.4 Tuning Efforts (PDF pages 64–71)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-concepts-2-3-3-to-2-3-6-p64-71.md
- Slice: 2.3.4 Tuning Efforts

---

2.3.4 Tuning Efforts
Performance tuning is most effective when done closest to where the work is performed. For
workloads driven by applications, this means within the application itself. Table 2.3 shows an
example software stack with tuning possibilities.

By tuning at the application level, you may be able to eliminate or reduce database queries and
improve performance by a large factor (e.g., 20x). Tuning down to the storage device level may
eliminate or improve storage I/O, but a tax has already been paid in executing higher-level OS
stack code, so this may improve resulting application performance only by percentages (e.g., 20%).


Table 2.3      Example targets of tuning
Layer                Example Tuning Targets
Application          Application logic, request queue sizes, database queries performed
Database             Database table layout, indexes, buffering
System calls         Memory-mapped or read/write, sync or async I/O flags
File system          Record size, cache size, file system tunables, journaling
Storage              RAID level, number and type of disks, storage tunables



There is another reason for finding large performance wins at the application level. Many of
today’s environments target rapid deployment for features and functionality, pushing software
28   Chapter 2 Methodologies


     changes into production weekly or daily.2 Application development and testing therefore tend
     to focus on correctness, leaving little or no time for performance measurement or optimization
     before production deployment. These activities are conducted later, when performance becomes
     a problem.

     While the application can be the most effective level at which to tune, it isn’t necessarily the
     most effective level from which to base observation. Slow queries may be best understood from
     their time spent on-CPU, or from the file system and disk I/O that they perform. These are
     observable from operating system tools.

     In many environments (especially cloud computing) the application level is under constant
     development, pushing software changes into production weekly or daily. Large performance
     wins, including fixes for regressions, are frequently found as the application code changes. In
     these environments, tuning for the operating system and observability from the operating
     system can be easy to overlook. Remember that operating system performance analysis can also
     identify application-level issues, not just OS-level issues, in some cases more easily than from the
     application alone.
