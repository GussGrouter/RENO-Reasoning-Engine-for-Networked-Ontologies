by bundled tools or third-party tools, via API requests, or by processing operation logs.
Logs: What operation logs does the application create? What logs can be enabled? What
performance metrics, including latency, are available from the logs? For example, MySQL
supports a slow query log, providing valuable performance details for each query slower
than a certain threshold.
Version: Is the application the latest version? Have performance fixes or improvements
been noted in the release notes for recent versions?
Bugs: Is there a bug database for the application? What are the “performance” bugs for
your version of the application? If you have a current performance issue, search the bug
database to see if anything like it has happened before, how it was investigated, and what
else was involved.
Source code: Is the application open source? If so, code paths identified by profilers and
tracers can be studied, potentially leading to performance wins. You may be able to modify the application code yourself to improve performance, and submit your improvements
upstream for inclusion in the official application.
Community: Is there a community for the application where performance findings are
shared? Communities may include forums, blogs, Internet Relay Chat (IRC) channels,

5.1

Application Basics

other chat channels (e.g., Slack), meetups, and conferences. Meetups and conferences
often post slides and videos online, which are useful resources for years afterward. They
may also have a community manager who shares community updates and news.
■

■

Books: Are there books about the application and/or its performance? Are they good
books (e.g., written by an expert, practical/actionable, makes good use of reader’s time, up
to date, etc.)?
Experts: Who are the recognized performance experts for the application? Learning their
names can help you find material they have authored.

Regardless of the source, you are aiming to understand the application at a high level—what it
does, how it operates, and how it performs. An immensely useful resource, if you can find one, is
a functional diagram illustrating application internals.
The next sections cover other application basics: setting objectives, optimizing the common
case, observability, and big O notation.

5.1.1 Objectives
A performance goal provides direction for your performance analysis work and helps you select
which activities to perform. Without a clear goal, performance analysis risks turning into a
random “fishing expedition.”
For application performance, you can start with what operations the application performs (as
described earlier) and what the goal for performance is. The goal may be:
■

Latency: A low or consistent application response time

■

Throughput: A high application operation rate or data transfer rate

■

Resource utilization: Efficiency for a given application workload

■

Price: Improving the performance/price ratio, lowering computing costs

It is better if these can be quantified using metrics that may be derived from business or
quality-of-service requirements. Examples are:
■

An average application request latency of 5 ms

■

