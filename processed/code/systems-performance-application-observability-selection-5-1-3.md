<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (combined extract; Chapter 5 Applications) -->
1

If the server size is variable (as with cloud instances). This may be better expressed in terms of the bounding
resource: e.g., a maximum 1,000 application requests per second per CPU, for a CPU-bound workload.

173

174

Chapter 5 Applications

For throughput-based goals, note that not all operations are equal in terms of performance or
cost. If the goal is a certain rate of operations, it may be important to also specify what type of
operations they are. This may be a distribution based on expected or measured workloads.
Section 5.2, Application Performance Techniques, describes common methods for improving
