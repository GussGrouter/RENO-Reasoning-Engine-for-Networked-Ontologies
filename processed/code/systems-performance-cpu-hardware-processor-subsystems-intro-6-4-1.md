<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

6.4.1 Hardware
CPU hardware includes the processor and its subsystems, and the CPU interconnect for multiprocessor systems.

Processor
Components of a generic two-core processor are shown in Figure 6.5.

Figure 6.5 Generic two-core processor components
The control unit is the heart of the CPU, performing instruction fetch, decoding, managing execution, and storing results.
This example processor depicts a shared floating-point unit and (optional) shared Level 3 cache.
The actual components in your processor will vary depending on its type and model. Other
performance-related components that may be present include:
■

P-cache: Prefetch cache (per CPU core)

■

W-cache: Write cache (per CPU core)

■

Clock: Signal generator for the CPU clock (or provided externally)

■

Timestamp counter: For high-resolution time, incremented by the clock

■

Microcode ROM: Quickly converts instructions to circuit signals

■

Temperature sensors: For thermal monitoring

■

Network interfaces: If present on-chip (for high performance)

Some processor types use the temperature sensors as input for dynamic overclocking of individual cores (including Intel Turbo Boost technology), increasing the clock rate while the core
remains in its temperature envelope. The possible clock rates can be defined by P-states.
