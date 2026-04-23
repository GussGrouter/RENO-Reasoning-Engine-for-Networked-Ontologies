Advanced Workload Characterization/Checklist
Gregg lists many additional yes/no questions (cache hit ratio and sizing; other caches; prior tuning; which apps/users; which paths; errors; call paths; sync fraction; inter-arrival distribution, etc.).

(Omitted in this processed extract: the long bullet checklist — see PDF. Cross-reference Chapter 2 §2.5.10 workload characterization — who / why / what / how.)

Performance Characterization
The previous workload characterization lists examine the workload applied. The following
examines the resulting performance:

■ What is the average file system operation latency?

■ Are there any high-latency outliers?

■ What is the full distribution of operation latency?

■ Are system resource controls for file system or disk I/O present and active?

The first three questions may be asked for each operation type separately.

Event Tracing
Tracing tools can be used to record all file system operations and details to a log for later analysis.
This can include the operating type, operation arguments, file pathname, start and end
timestamps, completion status, and process ID and name, for every I/O. While this may be the
ultimate tool for workload characterization, in practice it can cost significant overhead due to
the rate of file system operations, often making it impractical unless heavily filtered (e.g., only
including slow I/O in the log: see the ext4slower(8) tool in Section 8.6.14).
