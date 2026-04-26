<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs §6.5 continued) -->

6.5.7 Static Performance Tuning
Static performance tuning focuses on issues of the configured environment. For CPU performance, examine the following aspects of the static configuration:
■

How many CPUs are available for use? Are they cores? Hardware threads?

■

Are GPUs or other accelerators available and in use?

■

Is the CPU architecture single- or multiprocessor?

■

What is the size of the CPU caches? Are they shared?

■

■

■

■

What is the CPU clock speed? Is it dynamic (e.g., Intel Turbo Boost and SpeedStep)? Are
those dynamic features enabled in the BIOS?
What other CPU-related features are enabled or disabled in the BIOS? E.g., turboboost, bus
settings, power saving settings?
Are there performance issues (bugs) with this processor model? Are they listed in the
processor errata sheet?
What is the microcode version? Does it include performance-impacting mitigations for
security vulnerabilities (e.g., Spectre/Meltdown)?

■

Are there performance issues (bugs) with this BIOS firmware version?

■

Are there software-imposed CPU usage limits (resource controls) present? What are they?

The answers to these questions may reveal previously overlooked configuration choices.
The last question is especially true for cloud computing environments, where CPU usage is
commonly limited.

