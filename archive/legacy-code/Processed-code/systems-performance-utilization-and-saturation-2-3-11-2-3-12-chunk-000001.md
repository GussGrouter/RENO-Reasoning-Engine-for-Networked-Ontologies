# systems-performance-utilization-and-saturation-2-3-11-2-3-12 (chunk 000001)

# Systems Performance — utilization + saturation (2.3.11–2.3.12) (PDF pages 70–75)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-scalability-scout-p70-75.md
- Slice: from `2.3.11 Utilization` through `2.3.12 Saturation`

---

2.3.11 Utilization
The term utilization3 is often used for operating systems to describe device usage, such as for the
CPU and disk devices. Utilization can be time-based or capacity-based.


Time-Based
Time-based utilization is formally defined in queueing theory. For example [Gunther 97]:

        the average amount of time the server or resource was busy

along with the ratio

        U = B/T

where U = utilization, B = total time the system was busy during T, the observation period.

This is also the “utilization” most readily available from operating system performance tools.
The disk monitoring tool iostat(1) calls this metric %b for percent busy, a term that better conveys
the underlying metric: B/T.

This utilization metric tells us how busy a component is: when a component approaches 100%
utilization, performance can seriously degrade when there is contention for the resource. Other
metrics can be checked to confirm and to see if the component has therefore become a system
bottleneck.

Some components can service multiple operations in parallel. For them, performance may not
degrade much at 100% utilization as they can accept more work. To understand this, consider a


3
    Spelled utilisation in some parts of the world.
34   Chapter 2 Methodologies


     building elevator. It may be considered utilized when it is moving between floors, and not uti-
     lized when it is idle waiting. However, the elevator may be able to accept more passengers even
     when it is busy 100% of the time responding to calls—that is, it is at 100% utilization.

     A disk that is 100% busy may also be able to accept and process more work, for example, by buff-
     ering writes in the on-disk cache to be completed later. Storage arrays frequently run at 100%
     utilization because some disk is busy 100% of the time, but the array has plenty of idle disks and
     can accept more work.


     Capacity-Based
     The other definition of utilization is used by IT professionals in the context of capacity planning
     [Wong 97]:

         A system or component (such as a disk drive) is able to deliver a certain amount of
         throughput. At any level of performance, the system or component is working at some
         proportion of its capacity. That proportion is called the utilization.

     This defines utilization in terms of capacity instead of time. It implies that a disk at 100% utiliza-
     tion cannot accept any more work. With the time-based definition, 100% utilization only means
     it is busy 100% of the time.

         100% busy does not mean 100% capacity.

     For the elevator example, 100% capacity may mean the elevator is at its maximum payload
     capacity and cannot accept more passengers.

     In an ideal world, we would be able to measure both types of utilization for a device, so that, for
     example, you would know when a disk is 100% busy and performance begins to degrade due to
     contention, and also when it is at 100% capacity and cannot accept more work. Unfortunately,
     this usually isn’t possible. For a disk, it would require knowledge of what the disk’s on-board con-
     troller was doing and a prediction of capacity. Disks do not currently provide this information.

     In this book, utilization usually refers to the time-based version, which you could also call non-
     idle time. The capacity version is used for some volume-based metrics, such as memory usage.


     2.3.12      Saturation
     The degree to which more work is requested of a resource than it can process is saturation.
     Saturation begins to occur at 100% utilization (capacity-based), as extra work cannot be
     processed and begins to queue. This is pictured in Figure 2.8.

     The figure pictures saturation increasing linearly beyond the 100% capacity-based utilization
     mark as load continues to increase. Any degree of saturation is a performance issue, as time
     is spent waiting (latency). For time-based utilization (percent busy), queueing and therefore
     saturation may not begin at the 100% utilization mark, depending on the degree to which the
     resource can operate on work in parallel.
                                                                                     2.3    Concepts    35




Figure 2.8 Utilization versus saturation
