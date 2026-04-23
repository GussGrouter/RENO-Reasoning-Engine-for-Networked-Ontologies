the frameworks as well. Dynamic instrumentation is especially useful for this purpose, as custom
tools can be created to double-check metrics.
Another verification technique is to apply known workloads and then to check that the observability tools agree with the results you expect. This can involve the use of micro-benchmarking
tools that report their own statistics for comparison.
Sometimes it isn’t the tool or statistic that is in error, but the documentation that describes
it, including man pages. The software may have evolved without the documentation being
updated.
Realistically, you may not have time to double-check every performance measurement you use
and will do this only if you encounter unusual results or a result that is company critical. Even
if you do not double-check, it can be valuable to be aware that you didn’t and that you assumed
the tools were correct.
Metrics can also be incomplete. When faced with a large number of tools and metrics, it may
be tempting to assume that they provide complete and effective coverage. This is often not the
case: metrics may have been added by programmers to debug their own code, and later built into
observability tools without much study of real customer needs. Some programmers may not
have added any at all to new subsystems.

13
In this case the tool and measurement are correct, but an automated collector has introduced errors. At Surge 2013
I gave a lightning talk on an astonishing case [Gregg 13c]: a benchmarking company reported poor metrics for a product I was supporting, and I dug in. It turned out the shell script they used to automate the benchmark had two bugs.
First, when processing output from fio(1), it would take a result such as “100KB/s” and use a regular expression
to elide nun-numeric characters, including “KB/s” to turn this into “100”. Since fio(1) reported results with different
units (bytes, Kbytes, Mbytes), this introduced massive (1024x) errors. Second, they also elided decimal places, so a
result of “1.6” became “16”.

167

168

Chapter 4 Observability Tools

An absence of metrics can be more difficult to identify than the presence of poor metrics.
Chapter 2, Methodologies, can help you find these missing metrics by studying the questions
you need answered for performance analysis.

4.7
