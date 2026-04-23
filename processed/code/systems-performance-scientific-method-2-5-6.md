# Systems Performance — scientific method (2.5.6) (scientific-method-2-5-6) (PDF pages 82–92)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-methodology-2-5-scout-p82-92.md

---

2.5.6     Scientific Method
     The scientific method studies the unknown by making hypotheses and then testing them. It
     can be summarized by the following steps:

        1. Question
        2. Hypothesis

        3. Prediction

        4. Test

        5. Analysis

     The question is the performance problem statement. From this you can hypothesize what the
     cause of poor performance may be. Then you construct a test, which may be observational or
     experimental, that tests a prediction based on the hypothesis. You finish with analysis of the test
     data collected.

     For example, you may find that application performance is degraded after migrating to a system
     with less main memory, and you hypothesize that the cause of poor performance is a smaller
     file system cache. You might use an observational test to measure the cache miss rate on both
                                                                                  2.5 Methodology      45


systems, predicting that cache misses will be higher on the smaller system. An experimental test
would be to increase the cache size (adding RAM), predicting that performance will improve.
Another, perhaps easier, experimental test is to artificially reduce the cache size (using tunable
parameters), predicting that performance will be worse.

The following are some more examples.


Example (Observational)
   1. Question: What is causing slow database queries?

   2. Hypothesis: Noisy neighbors (other cloud computing tenants) are performing disk I/O,
      contending with database disk I/O (via the file system).

   3. Prediction: If file system I/O latency is measured during a query, it will show that the file
      system is responsible for the slow queries.

   4. Test: Tracing of database file system latency as a ratio of query latency shows that less than
      5% of the time is spent waiting for the file system.

   5. Analysis: The file system and disks are not responsible for slow queries.

Although the issue is still unsolved, some large components of the environment have been
ruled out. The person conducting this investigation can return to step 2 and develop a new
hypothesis.


Example (Experimental)
   1. Question: Why do HTTP requests take longer from host A to host C than from host B to
      host C?

   2. Hypothesis: Host A and host B are in different data centers.

   3. Prediction: Moving host A to the same data center as host B will fix the problem.

   4. Test: Move host A and measure performance.
   5. Analysis: Performance has been fixed—consistent with the hypothesis.

If the problem wasn’t fixed, reverse the experimental change (move host A back, in this case)
before beginning a new hypothesis—changing multiple factors at once makes it harder to iden-
tify which one mattered!


Example (Experimental)
   1. Question: Why did file system performance degrade as the file system cache grew in size?

   2. Hypothesis: A larger cache stores more records, and more compute is required to manage a
      larger cache than a smaller one.

   3. Prediction: Making the record size progressively smaller, and therefore causing more
      records to be used to store the same amount of data, will make performance progressively
      worse.

   4. Test: Test the same workload with progressively smaller record sizes.
46   Chapter 2 Methodologies


        5. Analysis: Results are graphed and are consistent with the prediction. Drill-down analysis
           is now performed on the cache management routines.

     This is an example of a negative test—deliberately hurting performance to learn more about the
     target system.
