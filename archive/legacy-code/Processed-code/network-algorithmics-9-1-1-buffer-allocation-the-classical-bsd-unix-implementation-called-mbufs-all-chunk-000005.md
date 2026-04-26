# network-algorithmics-9-1-1-buffer-allocation-the-classical-bsd-unix-implementation-called-mbufs-all (chunk 000005)

the threshold is too small) or unduly dangerous (if the threshold is too high). Using a static value of
threshold is no different from using a fixed window size for flow control. But TCP uses a dynamic
window size that adapts to congestion. Similarly, it makes sense to exploit a degree of freedom (P13)
and use dynamic thresholds.
    Intuitively, TCP window flow control increases a connection’s window size if there appears to be
unused bandwidth, as measured by the lack of packet drops. Similarly, the simplest way to adapt to
congestion in a shared buffer is to monitor the free space remaining and to increase the threshold
proportional to the free space. Thus user i is limited to no more than cF bytes, where c is a constant
and F is the current amount of free space. If c is chosen to be a power of 2, this scheme only requires
the use of a shifter (to multiply by c) and a comparator (to compare with cF ). This is far simpler than
even the buffer-stealing algorithm.
    Choudhury and Hahne recommend a value of c = 1. This implies that a single user is limited to
taking no more than half the available bandwidth. This is because when the user takes half, the free
space is equal to the user allocation and the threshold check fails. Similarly, if c = 2, any user is limited
to no more than 2/3 of the available buffer space. Thus unlike buffer stealing, this scheme always holds
some free space in reserve for new arrivals, trading slightly suboptimal use of memory for a simpler
implementation.
    Now suppose there are two users and that c = 1. One might naively think that since each user is
limited to no more than half, two active users are limited to a quarter. The scheme does better, however.
Each user can now take 1/3, leaving 1/3 free. Next, if two new users arrive and the old users do not
free their buffers, the two new users can get up to 1/9 of the buffer space.
    Thus, unlike buffer stealing, the scheme is not fair in a short-term sense. However, if the same set
of users is present for sufficiently long periods, the scheme should be fair in a long-term sense. In the
previous example after the buffers allocated to the first two users are deallocated, a fairer allocation
should result.
