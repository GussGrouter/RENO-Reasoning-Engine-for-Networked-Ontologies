# systems-performance-latency-analysis-2-5-13 (chunk 000001)

# Systems Performance — latency analysis (2.5.13) (latency-analysis-2-5-13) (PDF pages 92–98)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-drilldown-latency-scout-p92-98.md

---

2.5.13      Latency Analysis
     Latency analysis examines the time taken to complete an operation and then breaks it into
     smaller components, continuing to subdivide the components with the highest latency so that
     the root cause can be identified and quantified. Similarly to drill-down analysis, latency analysis
     may drill down through layers of the software stack to find the origin of latency issues.

     Analysis can begin with the workload applied, examining how that workload was processed in
     the application, and then drill down into the operating system libraries, system calls, the kernel,
     and device drivers.

     For example, analysis of MySQL query latency could involve answering the following questions
     (example answers are given here):

        1. Is there a query latency issue? (yes)

        2. Is the query time largely spent on-CPU or waiting off-CPU? (off-CPU)

        3. What is the off-CPU time spent waiting for? (file system I/O)

        4. Is the file system I/O time due to disk I/O or lock contention? (disk I/O)

        5. Is the disk I/O time mostly spent queueing or servicing the I/O? (servicing)

        6. Is the disk service time mostly I/O initialization or data transfer? (data transfer)

     For this example, each step of the process posed a question that divided the latency into two
     parts and then proceeded to analyze the larger part: a binary search of latency, if you will. The
     process is pictured in Figure 2.14.

     As the slower of A or B is identified, it is then further split into A or B, analyzed, and so on.

     Latency analysis of database queries is the target of method R.
                                                                               2.5 Methodology        57




Figure 2.14 Latency analysis procedure
