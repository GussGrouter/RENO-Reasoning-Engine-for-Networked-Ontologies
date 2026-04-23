<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
There are a couple of techniques for finding the off-CPU time that matters:
■

■

Zoom into (or filter by) the application request handling function(s), since we care most
about off-CPU time during the handling of an application request. For MySQL server this
is the do_command() function. A search for do_command() and then zooming in produces
a similar flame graph to Figure 5.4. While this approach is effective, you will need to know
what function to search for in your specific application.
Use a kernel filter during collection to exclude uninteresting thread states. The effectiveness is dependent on the kernel; on Linux, matching on TASK_UNINTERRUPTIBLE
focuses on many interesting off-CPU events, but does exclude some as well.

You will sometimes find application-blocking code paths that are waiting on something else,
such as a lock. To drill down further, you need to know why the holder of the lock took so long
to release it. Apart from lock analysis, described in Section 5.4.7, Static Performance Tuning, a
generic technique is to instrument the waker event. This is an advanced activity: see Chapter 14
of BPF Performance Tools [Gregg 19], and the tools wakeuptime(8) and offwaketime(8) from BCC.
Section 5.5.3, offcputime, shows instructions for generating off-CPU flame graphs using
offcputime(8) from BCC. Apart from scheduler events, syscall events are another useful target
for studying applications.
