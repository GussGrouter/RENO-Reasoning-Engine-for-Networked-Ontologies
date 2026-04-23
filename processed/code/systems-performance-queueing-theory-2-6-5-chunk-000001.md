# systems-performance-queueing-theory-2-6-5 (chunk 000001)

# Systems Performance — queueing theory (2.6.5) (queueing-theory-2-6-5) (PDF pages 98–114)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-modeling-scout-p98-106.md + processed/code/systems-performance-modeling-scout-p104-114.md

---

2.6.5     Queueing Theory
     Queueing theory is the mathematical study of systems with queues, providing ways to analyze
     their queue length, wait time (latency), and utilization (time-based). Many components in
     computing, both software and hardware, can be modeled as queueing systems. The modeling of
     multiple queueing systems is called queueing networks.

     This section summarizes the role of queueing theory and provides an example to help you under-
     stand that role. It is a large field of study, covered in detail in other texts [Jain 91][Gunther 97].

     Queueing theory builds upon various areas of mathematics and statistics, including probability
     distributions, stochastic processes, Erlang’s C formula (Agner Krarup Erlang invented queueing
     theory), and Little’s Law. Little’s Law can be expressed as

          L = λW

     which determines the average number of requests in a system, L, as the average arrival rate, λ,
     multiplied by the average request time in the system, W. This can be applied to a queue, such
     that L is the number of requests in the queue, and W is the average wait time on the queue.
                                                                                     2.6   Modeling    67


Queueing systems can be used to answer a variety of questions, including the following:

    ■   What will the mean response time be if the load doubles?
    ■   What will be the effect on mean response time after adding an additional processor?
    ■   Can the system provide a 90th percentile response time of under 100 ms when the load
        doubles?

Apart from response time, other factors, including utilization, queue lengths, and number of
resident jobs, can be studied.

A simple queueing system model is shown in Figure 2.18.




Figure 2.18 Queueing model

This has a single service center that processes jobs from the queue. Queueing systems can have
multiple service centers that process work in parallel. In queueing theory, the service centers are
often called servers.

Queueing systems can be categorized by three factors:

    ■   Arrival process: This describes the inter-arrival time for requests to the queueing system,
        which may be random, fixed-time, or a process such as Poisson (which uses an exponen-
        tial distribution for arrival time).
    ■   Service time distribution: This describes the service times for the service center. They
        may be fixed (deterministic), exponential, or of another distribution type.
    ■   Number of service centers: One or many.

These factors can be written in Kendall’s notation.


Kendall’s Notation
This notation assigns codes for each attribute. It has the form

    A/S/m

These are the arrival process (A), service time distribution (S), and number of service centers (m).
There is also an extended form of Kendall’s notation that includes more factors: number of buf-
fers in the system, population size, and service discipline.

                                                                                    2.6   Modeling     65


The relative capacity is C(N), and N is the scaling dimension, such as the CPU count or user load.
The α parameter (where 0 <= α <= 1) represents the degree of seriality and is how this deviates
from linear scalability.

Amdahl’s Law of Scalability can be applied by taking the following steps:

   1. Collect data for a range of N, either by observation of an existing system or experimentally
      using micro-benchmarking or load generators.

   2. Perform regression analysis to determine the Amdahl parameter (α); this may be done
      using statistical software, such as gnuplot or R.

   3. Present the results for analysis. The collected data points can be plotted along with the
      model function to predict scaling and reveal differences between the data and the model.
      This may also be done using gnuplot or R.

The following is example gnuplot code for Amdahl’s Law of Scalability regression analysis, to
provide a sense of how this step can be performed:

inputN = 10                          # rows to include as model input
alpha = 0.1                          # starting point (seed)
amdahl(N) = N1 * N/(1 + alpha * (N - 1))
# regression analysis (non-linear least squares fitting)
fit amdahl(x) filename every ::1::inputN using 1:2 via alpha

A similar amount of code is required to process this in R, involving the nls() function for non-
linear least squares fitting to calculate the coefficients, which are then used during plotting. See
the Performance Scalability Models toolkit in the references at the end of this chapter for the full
code in both gnuplot and R [Gregg 14a].

An example Amdahl’s Law of Scalability function is shown in the next section.


2.6.4 Universal Scalability Law
The Universal Scalability Law (USL), previously called the super-serial model [Gunther 97], was
developed by Dr. Neil Gunther to include a parameter for coherency delay. This was pictured
earlier as the coherence scalability profile, which includes the effects of contention.

USL can be defined as:

    C(N) = N/(1 + α(N – 1) + βN(N – 1))

C(N), N, and α are as with Amdahl’s Law of Scalability. β is the coherence parameter. When
β == 0, this becomes Amdahl’s Law of Scalability.

Examples of both USL and Amdahl’s Law of Scalability analysis are graphed in Figure 2.17.
66   Chapter 2 Methodologies




     Figure 2.17 Scalability models

     The input dataset has a high degree of variance, making it difficult to visually determine the
     scalability profile. The first ten data points, drawn as circles, were provided to the models. An
     additional ten data points are also plotted, drawn as crosses, which check the model prediction
     against reality.

     For more on USL analysis, see [Gunther 97] and [Gunther 07].


     2.6.5     Queueing Theory
     Queueing theory is the mathematical study of systems with queues, providing ways to analyze
     their queue length, wait time (latency), and utilization (time-based). Many components in
     computing, both software and hardware, can be modeled as queueing systems. The modeling of
     multiple queueing systems is called queueing networks.

     This section summarizes the role of queueing theory and provides an example to help you under-
     stand that role. It is a large field of study, covered in detail in other texts [Jain 91][Gunther 97].

     Queueing theory builds upon various areas of mathematics and statistics, including probability
     distributions, stochastic processes, Erlang’s C formula (Agner Krarup Erlang invented queueing
     theory), and Little’s Law. Little’s Law can be expressed as

          L = λW

     which determines the average number of requests in a system, L, as the average arrival rate, λ,
     multiplied by the average request time in the system, W. This can be applied to a queue, such
     that L is the number of requests in the queue, and W is the average wait time on the queue.
                                                                                     2.6   Modeling    67


Queueing systems can be used to answer a variety of questions, including the following:

    ■   What will the mean response time be if the load doubles?
    ■   What will be the effect on mean response time after adding an additional processor?
    ■   Can the system provide a 90th percentile response time of under 100 ms when the load
        doubles?

Apart from response time, other factors, including utilization, queue lengths, and number of
resident jobs, can be studied.

A simple queueing system model is shown in Figure 2.18.




Figure 2.18 Queueing model

This has a single service center that processes jobs from the queue. Queueing systems can have
multiple service centers that process work in parallel. In queueing theory, the service centers are
often called servers.

Queueing systems can be categorized by three factors:

    ■   Arrival process: This describes the inter-arrival time for requests to the queueing system,
        which may be random, fixed-time, or a process such as Poisson (which uses an exponen-
        tial distribution for arrival time).
    ■   Service time distribution: This describes the service times for the service center. They
        may be fixed (deterministic), exponential, or of another distribution type.
    ■   Number of service centers: One or many.

These factors can be written in Kendall’s notation.


Kendall’s Notation
This notation assigns codes for each attribute. It has the form

    A/S/m

These are the arrival process (A), service time distribution (S), and number of service centers (m).
There is also an extended form of Kendall’s notation that includes more factors: number of buf-
fers in the system, population size, and service discipline.
68   Chapter 2 Methodologies


     Examples of commonly studied queueing systems are

         ■   M/M/1: Markovian arrivals (exponentially distributed arrival times), Markovian service
             times (exponential distribution), one service center
         ■   M/M/c: same as M/M/1, but multiserver
         ■   M/G/1: Markovian arrivals, general distribution of service times (any), one service center
         ■   M/D/1: Markovian arrivals, deterministic service times (fixed), one service center

     M/G/1 is commonly applied to study the performance of rotational hard disks.


     M/D/1 and 60% Utilization
     As a simple example of queueing theory, consider a disk that responds to a workload determinis-
     tically (this is a simplification). The model is M/D/1.

     The question posed is: How does the disk’s response time vary as its utilization increases?

     Queueing theory allows the response time for M/D/1 to be calculated:

         r = s(2 - ρ)/2(1 - ρ)

     where the response time, r, is defined in terms of the service time, s, and the utilization, ρ.

     For a service time of 1 ms, and utilizations from 0 to 100%, this relationship has been graphed in
     Figure 2.19.




     Figure 2.19 M/D/1 mean response time versus utilization
                                                                          2.7   Capacity Planning    69


Beyond 60% utilization, the average response time doubles. By 80%, it has tripled. As disk I/O
latency is often the bounding resource for an application, increasing the average latency by dou-
ble or higher can have a significant negative effect on application performance. This is why disk
utilization can become a problem well before it reaches 100%, as it is a queueing system where
requests (typically) cannot be interrupted and must wait their turn. This is different from CPUs,
for example, where higher-priority work can preempt.

This graph can visually answer an earlier question—what will the mean response time be if the
load doubles?—when utilization is relative to load.

This model is simple, and in some ways it shows the best case. Variations in service time can
drive the mean response time higher (e.g., using M/G/1 or M/M/1). There is also a distribution
of response times, not pictured in Figure 2.19, such that the 90th and 99th percentiles degrade
much faster beyond 60% utilization.

As with the earlier gnuplot example for Amdahl’s Law of Scalability, it may be illustrative to
show some actual code, for a sense of what may be involved. This time the R statistics software
was used [R Project 20]:

svc_ms <- 1                       # average disk I/O service time, ms
util_min <- 0                     # range to plot
util_max <- 100                   # "
ms_min <- 0                       # "
ms_max <- 10                      # "
# Plot mean response time vs utilization (M/D/1)
plot(x <- c(util_min:util_max), svc_ms * (2 - x/100) / (2 * (1 - x/100)),
    type="l", lty=1, lwd=1,
    xlim=c(util_min, util_max), ylim=c(ms_min, ms_max),
    xlab="Utilization %", ylab="Mean Response Time (ms)")

The earlier M/D/1 equation has been passed to the plot() function. Much of this code specifies
limits to the graph, line properties, and axis labels.
