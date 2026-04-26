7.6

Tuning

The most important memory tuning you can do is to ensure that applications remain in main
memory, and that paging and swapping do not occur frequently. Identifying this problem was
covered in Section 7.4, Methodology, and Section 7.5, Observability Tools. This section discusses
other memory tuning: kernel tunable parameters, configuring large pages, allocators, and
resource controls.
The specifics of tuning—the options available and what to set them to—depend on the operating
system version and the intended workload. The following sections, organized by tuning type,
provide examples of which tunable parameters may be available, and why they may need to
be tuned.

