22   Chapter 2 Methodologies


     Of all the chapters in this book, this one has changed the least since the first edition. Software,
     hardware, performance tools, and performance tunables have all changed over the course of
     my career. What have remained the same are the theory and methodologies: the durable skills
     covered in this chapter.

     This chapter has three parts:

         ■   Background introduces terminology, basic models, key performance concepts, and
             perspectives. Much of this will be assumed knowledge for the rest of this book.
         ■   Methodology discusses performance analysis methodologies, both observational and
             experimental; modeling; and capacity planning.
         ■   Metrics introduces performance statistics, monitoring, and visualizations.

     Many of the methodologies introduced here are explored in more detail in later chapters,
     including the methodology sections in Chapters 5 through 10.



     2.1        Terminology
     The following are key terms for systems performance. Later chapters provide additional terms
     and describe some of these in different contexts.
         ■   IOPS: Input/output operations per second is a measure of the rate of data transfer opera-
             tions. For disk I/O, IOPS refers to reads and writes per second.
         ■   Throughput: The rate of work performed. Especially in communications, the term is
             used to refer to the data rate (bytes per second or bits per second). In some contexts (e.g.,
             databases) throughput can refer to the operation rate (operations per second or transactions
             per second).
         ■   Response time: The time for an operation to complete. This includes any time spent
             waiting and time spent being serviced (service time), including the time to transfer the
             result.
         ■   Latency: A measure of time an operation spends waiting to be serviced. In some contexts
             it can refer to the entire time for an operation, equivalent to response time. See Section 2.3,
             Concepts, for examples.
         ■   Utilization: For resources that service requests, utilization is a measure of how busy a
             resource is, based on how much time in a given interval it was actively performing work.
             For resources that provide storage, utilization may refer to the capacity that is consumed
             (e.g., memory utilization).
         ■   Saturation: The degree to which a resource has queued work it cannot service.
         ■   Bottleneck: In systems performance, a bottleneck is a resource that limits the perfor-
             mance of the system. Identifying and removing systemic bottlenecks is a key activity of
             systems performance.
         ■   Workload: The input to the system or the load applied is the workload. For a database, the
             workload consists of the database queries and commands sent by the clients.
                                                                                    2.2 Models       23


   ■   Cache: A fast storage area that can duplicate or buffer a limited amount of data, to avoid
       communicating directly with a slower tier of storage, thereby improving performance. For
       economic reasons, a cache is often smaller than the slower tier.

The Glossary includes more terminology for reference if needed.



2.2       Models
The following simple models illustrate some basic principles of system performance.


2.2.1 System Under Test
The performance of a system under test (SUT) is shown in Figure 2.1.




Figure 2.1 Block diagram of system under test

It is important to be aware that perturbations (interference) can affect results, including those
caused by scheduled system activity, other users of the system, and other workloads. The origin
of the perturbations may not be obvious, and careful study of system performance may be
required to determine it. This can be particularly difficult in some cloud environments, where
other activity (by guest tenants) on the physical host system may not be observable from within
a guest SUT.

Another difficulty with modern environments is that they may be composed of several net-
worked components servicing the input workload, including load balancers, proxy servers, web
servers, caching servers, application servers, database servers, and storage systems. The mere act
of mapping the environment may help to reveal previously overlooked sources of perturbations.
The environment may also be modeled as a network of queueing systems, for analytical study.


2.2.2      Queueing System
Some components and resources can be modeled as a queueing system so that their performance
under different situations can be predicted based on the model. Disks are commonly modeled
as a queueing system, which can predict how response time degrades under load. Figure 2.2
shows a simple queueing system.
24   Chapter 2 Methodologies




     Figure 2.2 Simple queueing model

     The field of queueing theory, introduced in Section 2.6, Modeling, studies queueing systems and
     networks of queueing systems.



     2.3 Concepts
     The following are important concepts of systems performance and are assumed knowledge
     for the rest of this chapter and this book. The topics are described in a generic manner, before
     implementation-specific details are introduced in the Architecture sections of later chapters.


     2.3.1 Latency
     For some environments, latency is the sole focus of performance. For others, it is the top one or
     two key metrics for analysis, along with throughput.

     As an example of latency, Figure 2.3 shows a network transfer, such as an HTTP GET request,
     with the time split into latency and data transfer components.




     Figure 2.3 Network connection latency

     The latency is the time spent waiting before an operation is performed. In this example, the
     operation is a network service request to transfer data. Before this operation can take place,
     the system must wait for a network connection to be established, which is latency for this
     operation. The response time spans this latency and the operation time.

     Because latency can be measured from different locations, it is often expressed with the target of
     the measurement. For example, the load time for a website may be composed of three different
     times measured from different locations: DNS latency, TCP connection latency, and then TCP data
