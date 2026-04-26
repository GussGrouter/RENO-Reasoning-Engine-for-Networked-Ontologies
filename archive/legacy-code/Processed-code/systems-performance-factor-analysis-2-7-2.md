# Systems Performance — factor analysis (2.7.2) (factor-analysis-2-7-2) (PDF pages 108–116)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-capacity-planning-scout-p108-116.md

---

2.7.2    Factor Analysis
When purchasing and deploying new systems, there are often many factors that can be changed
to achieve the desired performance. These may include varying the number of disks and CPUs,
the amount of RAM, the use of flash devices, RAID configurations, file system settings, and so
forth. The task is usually to achieve the performance required for the minimum cost.

Testing all combinations would determine which has the best price/performance ratio; however,
this can quickly get out of hand: eight binary factors would require 256 tests.

A solution is to test a limited set of combinations. Here is an approach based on knowing the
maximum system configuration:

   1. Test performance with all factors configured to maximum.

  2. Change factors one by one, testing performance (it should drop for each).

   3. Attribute a percentage performance drop to each factor, based on measurements, along
      with the cost savings.

   4. Starting with maximum performance (and cost), choose factors to save cost, while main-
      taining the required requests per second based on their combined performance drop.

   5. Retest the calculated configuration for confirmation of delivered performance.

For an eight-factor system, this approach may require only ten tests.
72   Chapter 2 Methodologies


     As an example, consider capacity planning for a new storage system, with a requirement of
     1 Gbyte/s read throughput and a 200 Gbyte working set size. The maximum configuration
     achieves 2 Gbytes/s and includes four processors, 256 Gbytes of DRAM, 2 dual-port 10 GbE
     network cards, jumbo frames, and no compression or encryption enabled (which is costly to
     activate). Switching to two processors reduces performance by 30%, one network card by 25%,
     non-jumbo by 35%, encryption by 10%, compression by 40%, and less DRAM by 90% as the
     workload is no longer expected to fully cache. Given these performance drops and their known
     savings, the best price/performance system that meets the requirements can now be calculated;
     it might be a two-processor system with one network card, which meets the throughput needed:
     2 × (1 – 0.30) × (1 – 0.25) = 1.04 Gbytes/s estimated. It would then be wise to test this configura-
     tion, in case these components perform differently from their expected performance when used
     together.
