<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
5.4.8 Distributed Tracing
In a distributed environment, an application may be composed of services that run on separate
systems. While each service can be studied as though it is its own mini-application, it is also
necessary to study the distributed application as a whole. This requires new methodologies and
tools, and is commonly performed using distributed tracing.
Distributed tracing involves logging information on each service request and then later combining this information for study. Each application request that spans multiple services can then
be broken down into its dependency requests, and the service responsible for high application
latency or errors can be identified.
Collected information can include:
■

A unique identifier for the application request (external request ID)

■

Information about its location in the dependency hierarchy

■

Start and end times

■

Error status

A challenge with distributed tracing is the amount of log data generated: multiple entries for
every application request. One solution is to perform head-based sampling where at the start
(“head”) of the request, a decision is made whether to sample (“trace”) it: for example, to trace
one in every ten thousands requests. This is sufficient to analyze the performance of the bulk
of the requests, but it may make the analysis of intermittent errors or outliers difficult due to
limited data. Some distributed tracers are tail-based, where all events are first captured and then
a decision is made as to what to keep, perhaps based on latency and errors.
Once a problematic service has been identified, it can be analyzed in more detail using other
methodologies and tools.
