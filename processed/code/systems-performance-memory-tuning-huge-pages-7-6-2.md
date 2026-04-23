7.6.2 Multiple Page Sizes
Large page sizes can improve memory I/O performance by improving the hit ratio of the TLB
cache (increasing its reach). Most modern processors support multiple page sizes, such as a
4 Kbyte default and a 2 Mbyte large page.
On Linux, large pages (called huge pages) can be configured in a number of ways. For reference,
see Documentation/vm/hugetlbpage.txt.
These usually begin with the creation of huge pages:
# echo 50 > /proc/sys/vm/nr_hugepages
# grep Huge /proc/meminfo
AnonHugePages:

0 kB

HugePages_Total:

50

HugePages_Free:

50

HugePages_Rsvd:

0

HugePages_Surp:

0

Hugepagesize:

2048 kB

One way for an application to consume huge pages is via the shared memory segments, and the
SHM_HUGETLBS flag to shmget(2). Another way involves creating a huge page-based file system
for applications to map memory from:
# mkdir /mnt/hugetlbfs
# mount -t hugetlbfs none /mnt/hugetlbfs -o pagesize=2048K

7.6

Tuning

Other ways include the MAP_ANONYMOUS|MAP_HUGETLB flags to mmap(2) and use of the
libhugetlbfs API [Gorman 10].
Finally, transparent huge pages (THP) is another mechanism that uses huge pages by automatically
promoting and demoting normal pages to huge, without an application needing to specify huge
pages [Corbet 11]. In the Linux source see Documentation/vm/transhuge.txt and admin-guide/
mm/transhuge.rst.11

