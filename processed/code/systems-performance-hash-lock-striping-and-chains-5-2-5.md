<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (combined extract; Chapter 5 Applications §5.2.5–5.2.7) -->
Synchronization primitives manage access to memory to ensure integrity, and can operate similarly to traffic lights regulating access to an intersection. And, like traffic lights, they can halt the
flow of traffic, causing wait time (latency). The three commonly used types for applications are:
■

■

■

■

Mutex (MUTually EXclusive) locks: Only the holder of the lock can operate. Others
block and wait off-CPU.
Spin locks: Spin locks allow the holder to operate, while others spin on-CPU in a tight
loop, checking for the lock to be released. While these can provide low-latency access—
the blocked thread never leaves CPU and is ready to run in a matter of cycles once the lock
is available—they also waste CPU resources while threads spin, waiting.
RW locks: Reader/writer locks ensure integrity by allowing either multiple readers or one
writer only and no readers.
Semaphores: This is a variable type that can be counting to allow a given number of
parallel operations, or binary to allow only one (effectively a mutex lock).

Mutex locks may be implemented by the library or kernel as a hybrid of spin and mutex locks,
which spin if the holder is currently running on another CPU and block if it isn’t (or if a spin
threshold is reached). They were initially implemented for Linux in 2009 [Zijlstra 09] and now
have three paths depending on the state of the lock (as described in Documentation/locking/
mutex-design.rst [Molnar 20]):
1. fastpath: Attempts to acquire the lock using the cmpxchg instruction to set the owner.
This only succeeds if the lock is not held.
2. midpath: Also known as optimistic spinning, this spins on CPU while the lock holder is
also running, hoping that it is soon released and can be acquired without blocking.
3. slowpath: This blocks and deschedules the thread, to be woken up later when the lock is
available.
The Linux read-copy-update (RCU) mechanism is another synchronization mechanism in heavy
use for kernel code. It allows read operations without needing to acquire a lock, improving
performance over other lock types. With RCUs, writes create a copy of the protected data and
update the copy while in-flight reads can still access the original. It can detect when there are no
longer any readers (based on various per-CPU conditions) and then replace the original with the
