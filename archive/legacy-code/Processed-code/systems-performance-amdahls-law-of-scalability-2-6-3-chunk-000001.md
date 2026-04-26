# systems-performance-amdahls-law-of-scalability-2-6-3 (chunk 000001)

# Systems Performance — amdahl's law of scalability (2.6.3) (amdahls-law-of-scalability-2-6-3) (PDF pages 98–114)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-modeling-scout-p98-106.md + processed/code/systems-performance-modeling-scout-p104-114.md

---

2.6.3      Amdahl’s Law of Scalability
     Named after computer architect Gene Amdahl [Amdahl 67], this law models system scalability,
     accounting for serial components of workloads that do not scale in parallel. It can be used to
     study the scaling of CPUs, threads, workloads, and more.

     Amdahl’s Law of Scalability was shown in the earlier scalability profiles as contention, which
     describes contention for the serial resource or workload component. It can be defined as
     [Gunther 97]:

         C(N) = N/(1 + α(N – 1))
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
