3.5.2 Unikernels
A unikernel is a single-application machine image that combines kernel, library, and application
software together, and can typically run this in a single address space in either a hardware VM
or on bare metal. This potentially has performance and security benefits: less instruction text
means higher CPU cache hit ratios and fewer security vulnerabilities. This also creates a problem: there may be no SSH, shells, or performance tools available for you to log in and debug the
system, nor any way to add them.
For unikernels to be performance tuned in production, new performance tooling and metrics
must be built to support them. As a proof of concept, I built a rudimentary CPU profiler that
ran from Xen dom0 to profile a domU unikernel guest and then built a CPU flame graph, just to
show that it was possible [Gregg 16a].
Examples of unikernels include MirageOS [MirageOS 20].

