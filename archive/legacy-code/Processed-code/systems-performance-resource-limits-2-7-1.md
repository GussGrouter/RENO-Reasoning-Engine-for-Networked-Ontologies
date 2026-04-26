# Systems Performance — resource limits (2.7.1) (resource-limits-2-7-1) (PDF pages 108–116)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-capacity-planning-scout-p108-116.md

---

2.7.1      Resource Limits
     This method is a search for the resource that will become the bottleneck under load. For con-
     tainers, a resource may encounter a software-imposed limit that becomes the bottleneck. The
     steps for this method are:

        1. Measure the rate of server requests, and monitor this rate over time.

       2. Measure hardware and software resource usage. Monitor this rate over time.

        3. Express server requests in terms of resources used.

        4. Extrapolate server requests to known (or experimentally determined) limits for each
           resource.

     Begin by identifying the role of the server and the type of requests it serves. For example, a web
     server serves HTTP requests, a Network File System (NFS) server serves NFS protocol requests
     (operations), and a database server serves query requests (or command requests, for which que-
     ries are a subset).

     The next step is to determine the system resource consumption per request. For an existing sys-
     tem, the current rate of requests along with resource utilization can be measured. Extrapolation
     can then be used to see which resource will hit 100% utilization first, and what the rate of
     requests will be.

     For a future system, micro-benchmarking or load generation tools can be used to simulate the
     intended requests in a test environment, while measuring resource utilization. Given sufficient
     client load, you may be able to find the limit experimentally.

     The resources to monitor include:

         ■   Hardware: CPU utilization, memory usage, disk IOPS, disk throughput, disk capacity
             (volume used), network throughput
         ■   Software: Virtual memory usage, processes/tasks/threads, file descriptors

     Let’s say you’re looking at an existing system currently performing 1,000 requests/s. The
     busiest resources are the 16 CPUs, which are averaging 40% utilization; you predict that they
     will become the bottleneck for this workload once they become 100% utilized. The question
     becomes: What will the requests-per-second rate be at that point?

         CPU% per request = total CPU%/requests = 16 × 40%/1,000 = 0.64% CPU per request

         max requests/s = 100% × 16 CPUs/CPU% per request = 1,600 / 0.64 = 2,500 requests/s

     The prediction is 2,500 requests/s, at which point the CPUs will be 100% busy. This is a rough
     best-case estimate of capacity, as some other limiting factor may be encountered before the
     requests reach that rate.

     This exercise used only one data point: application throughput (requests per second) of 1,000
     versus device utilization of 40%. If monitoring over time is enabled, multiple data points at
     different throughput and utilization rates can be included, to improve the accuracy of the
                                                                         2.7   Capacity Planning   71


estimation. Figure 2.20 illustrates a visual method for processing these and extrapolating the
maximum application throughput.




Figure 2.20 Resource limit analysis

Is 2,500 requests/s enough? Answering this question requires understanding what the peak
workload will be, which shows up in daily access patterns. For an existing system that you have
monitored over time, you may already have an idea of what the peak will look like.

Consider a web server that is processing 100,000 website hits per day. This may sound like many,
but as an average is only one request/s—not much. However, it may be that most of the 100,000
website hits occur in the seconds after new content is posted, so the peak is significant.
