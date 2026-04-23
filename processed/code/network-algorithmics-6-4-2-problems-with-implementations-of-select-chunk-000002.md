# network-algorithmics-6-4-2-problems-with-implementations-of-select (chunk 000002)

Implementation
Having understood the parameters of the select() call, it is important to understand how select() is
implemented in the kernel of a typical UNIX variant (Wright and Stevens, 1995). The kernel does the
following (annotated with sources of overhead):
• Prune: The kernel starts by using the bitmaps passed as parameters to build a summary of descriptors
  marked in at least one bitmap (called the selected set).
   This requires a linear search through bitmaps of size N regardless of how many descriptors
   the application is currently interested in.
• Check: Next, for each descriptor in the selected set, the kernel checks if the descriptor is ready; if
  not, the kernel queues the application thread ID on the select queue of the descriptor. The kernel
  puts the calling application thread to sleep if no descriptors are ready.
   This requires investigation of all selected descriptors, independent of how many are actually
   ready. This step is more expensive than simply scanning a bitmap.
• Resume: When I/O occurs to make a descriptor ready (i.e., a packet arrives to a socket that the server
  is waiting for data from), the kernel I/O module checks its select queue and wakes up all threads
  waiting for a descriptor.
   This requires scheduler overhead, which seems fundamentally unavoidable without polling
   or busy waiting.

162      Chapter 6 Transferring control

• Rediscover: Finally, select() rediscovers the list of ready descriptors by making a scan of all selected
  descriptors to see which have become ready between the time select() was put to sleep and was later
  awakened. This requires repeating the same expensive checks made in Step 2.
   They are repeated despite the fact that the I/O module knew which descriptors became
   ready but did not inform the select() implementation.
