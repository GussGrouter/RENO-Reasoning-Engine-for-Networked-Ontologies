<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->

USE Method

As introduced in Chapter 2, Methodologies, and applied in later chapters, the USE method
checks the utilization, saturation, and errors of all hardware resources. Many application performance issues may be solved this way, by showing that a resource has become a bottleneck.
The USE method can also be applied to software resources. If you can find a functional diagram
showing the internal components of an application, consider the utilization, saturation, and
error metrics for each software resource and see what makes sense.
For example, the application may use a pool of worker threads to process requests, with a
queue for requests waiting their turn. Treating this as a resource, the three metrics could then
be defined in this way:
■

■

■

Utilization: Average number of threads busy processing requests during an interval, as a
percentage of the total threads. For example, 50% would mean that, on average, half the
threads were busy working on requests.
Saturation: Average length of the request queue during an interval. This shows how many
requests have backed up waiting for a worker thread.
Errors: Requests denied or failed for any reason.

Your task is then to find how these metrics can be measured. They may already be provided by
the application somewhere, or they may need to be added or measured using another tool, such
as dynamic tracing.
Queueing systems, like this example, can also be studied using queueing theory (see Chapter 2,
Methodologies).
For a different example, consider file descriptors. The system may impose a limit, such that these
are a finite resource. The three metrics could be as follows:
■

■

■

Utilization: Number of in-use file descriptors, as a percentage of the limit
Saturation: Depends on the OS behavior: if threads block waiting for file descriptors, this
can be the number of blocked threads waiting for this resource
Errors: Allocation error, such as EFILE, “Too many open files”

Repeat this exercise for the components of your application, and skip any metrics that don’t
make sense. This process may help you develop a short checklist for checking application health
