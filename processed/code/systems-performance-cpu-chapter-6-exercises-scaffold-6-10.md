6.10

Exercises

1. Answer the following questions about CPU terminology:
■

What is the difference between a process and a processor?

■

What is a hardware thread?

■

What is the run queue?

■

What is the difference between user time and kernel time?

2. Answer the following conceptual questions:
■

Describe CPU utilization and saturation.

■

Describe how the instruction pipeline improves CPU throughput.

■

Describe how processor instruction width improves CPU throughput.

■

Describe the advantages of multiprocess and multithreaded models.

3. Answer the following deeper questions:
■

Describe what happens when the system CPUs are overloaded with runnable work, including the effect on application performance.

299

300

Chapter 6 CPUs

■

■

When there is no runnable work to perform, what do the CPUs do?
When handed a suspected CPU performance issue, name two methodologies you would
use early during the investigation, and explain why.

4. Develop the following procedures for your environment:
■

■

A USE method checklist for CPU resources. Include how to fetch each metric (e.g., which
command to execute) and how to interpret the result. Try to use existing OS observability
tools before installing or using additional software products.
A workload characterization checklist for CPU resources. Include how to fetch each metric,
and try to use existing OS observability tools first.

5. Perform these tasks:
■

Calculate the load average for the following system, whose load is at steady state with no
significant disk/lock load:
q The system has 64 CPUs.
q The system-wide CPU utilization is 50%.
q The system-wide CPU saturation, measured as the total number of runnable and queued

threads on average, is 2.0.
■

Choose an application, and profile its user-level CPU usage. Show which code paths are
consuming the most CPU.

6. (optional, advanced) Develop bustop(1)—a tool that shows physical bus or interconnect
utilization—with a presentation similar to iostat(1): a list of buses, columns for throughput
in each direction, and utilization. Include saturation and error metrics if possible. This will
require using PMCs.

