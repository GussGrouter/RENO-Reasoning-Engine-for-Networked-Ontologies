8.3 Concepts
The following are a selection of important file system performance concepts.

8.3.1 File System Latency
File system latency is the primary metric of file system performance, measured as the time from
a logical file system request to its completion. It includes time spent in the file system and disk
I/O subsystem, and waiting on disk devices—the physical I/O. Application threads often block
during an application request in order to wait for file system requests to complete—in this way,
file system latency directly and proportionally affects application performance.
Cases where applications may not be directly affected include the use of non-blocking I/O,
prefetch (Section 8.3.4), and when I/O is issued from an asynchronous thread (e.g., a background
flush thread). It may be possible to identify these cases from the application, if it provides
detailed metrics for its file system usage. If not, a generic approach is to use a kernel tracing tool

8.3

Concepts

that can show the user-level stack trace that led to a logical file system I/O. This stack trace can
then be studied to see which application routines issued it.
Operating systems have not historically made file system latency readily observable, instead
providing disk device-level statistics. But there are many cases where such statistics are unrelated
to application performance, and where they are also misleading. An example of this is where
file systems perform background flushing of written data, which may appear as bursts of highlatency disk I/O. From the disk device-level statistics, this looks alarming; however, no application is waiting on these to complete. See Section 8.3.12, Logical vs. Physical I/O, for more cases.

