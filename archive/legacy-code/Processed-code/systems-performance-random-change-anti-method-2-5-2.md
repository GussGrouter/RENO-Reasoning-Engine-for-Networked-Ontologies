# Systems Performance — random change anti-method (2.5.2) (random-change-anti-method-2-5-2) (PDF pages 78–84)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-methodology-2-5-scout-p78-84.md

---

2.5.2 Random Change Anti-Method
     This is an experimental anti-methodology. The user randomly guesses where the problem may
     be and then changes things until it goes away. To determine whether performance has improved
     or not as a result of each change, a metric is studied, such as application runtime, operation
     time, latency, operation rate (operations per second), or throughput (bytes per second). The
     approach is as follows:

        1. Pick a random item to change (e.g., a tunable parameter).

        2. Change it in one direction.

        3. Measure performance.

        4. Change it in the other direction.

        5. Measure performance.

        6. Were the results in step 3 or step 5 better than the baseline? If so, keep the change and go
           back to step 1.

     While this process may eventually unearth tuning that works for the tested workload, it is very
     time-consuming and can also result in tuning that doesn’t make sense in the long term. For
                                                                                 2.5 Methodology       43


example, an application change may improve performance because it works around a database
or operating system bug that is later fixed. But the application will still have that tuning that no
longer makes sense, and that no one understood properly in the first place.

Another risk is where a change that isn’t properly understood causes a worse problem during
peak production load, and a need to back out the change.
