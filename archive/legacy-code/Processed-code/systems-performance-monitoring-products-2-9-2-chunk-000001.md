# systems-performance-monitoring-products-2-9-2 (chunk 000001)

# Systems Performance — monitoring products (2.9.2) (monitoring-products-2-9-2) (PDF pages 110–120)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-statistics-scout-p110-120.md

---

2.9.2       Monitoring Products
There are many third-party products for system performance monitoring. Typical features
include archiving data and presenting it as browser-based interactive graphs, and providing
configurable alerts.

Some of these operate by running agents (also known as exporters) on the system to gather their sta-
tistics. These agents either execute operating system observability tools (such as iostat(1) or sar(1))
and parse the text of the output (which is considered inefficient) or read directly from operating
system libraries and kernel interfaces. Monitoring products support a collection of custom agents
for exporting statistics from specific targets: web servers, databases, and language runtimes.

As systems become more distributed and the usage of cloud computing continues to grow, you
will more often need to monitor numerous systems: hundreds, thousands, or more. This is
where a centralized monitoring product can be especially useful, allowing an entire environ-
ment to be monitored from one interface.

As a specific example: the Netflix cloud is composed of over 200,000 instances and is monitored
using the Atlas cloud-wide monitoring tool, which was custom built by Netflix to operate at this
scale and is open source [Harrington 14]. Other monitoring products are discussed in Chapter 4,
Observability Tools, Section 4.2.4, Monitoring.
