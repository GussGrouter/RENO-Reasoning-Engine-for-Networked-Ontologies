# Systems Performance — timeline charts (2.10.4) (timeline-charts-2-10-4) (PDF pages 118–140)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch2-tail-scout-p118-140.md

---

2.10.4      Timeline Charts
A timeline chart shows a set of activities as bars on a timeline. These are commonly used for
front-end performance analysis (web browsers), where they are also called waterfall charts, and
show the timing of network requests. An example from the Firefox web browser is shown in
Figure 2.32.

In Figure 2.32, the first network request is highlighted: apart from showing its duration as a hor-
izontal bar, components of this duration are also shown as colored bars. These are also explained
in the right panel: the slowest component for the first request is “Waiting,” which is waiting
for the HTTP response from the server. Requests two to six begin after the first request begins
receiving data, and are likely dependent on that data. If explicit dependency arrows are included
in the chart, it becomes a type of Gantt chart.

For back-end performance analysis (servers), similar charts are used to show timelines for
threads or CPUs. Example software includes KernelShark [KernelShark 20] and Trace Compass
[Eclipse 20]. For an example KernelShark screenshot, see Chapter 14, Ftrace, Section 14.11.5,
KernelShark. Trace Compass also draws arrows showing dependencies, where one thread has
woken up another.
84   Chapter 2 Methodologies




     Figure 2.32 Firefox timeline chart
