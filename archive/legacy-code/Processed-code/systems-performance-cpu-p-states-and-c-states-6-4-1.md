<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

P-States and C-States
The advanced configuration and power interface (ACPI) standard, in use by Intel processors, defines
processor performance states (P-states) and processor power states (C-states) [ACPI 17].
P-states provide different levels of performance during normal execution by varying the CPU
frequency: P0 is the highest frequency (for some Intel CPUs this is the highest “turbo boost”
level) and P1...N are lower-frequency states. These states can be controlled by both hardware
(e.g., based on the processor temperature) or via software (e.g., kernel power saving modes). The
current operating frequency and available states can be observed using model-specific registers
(MSRs) (e.g., using the showboost(8) tool in Section 6.6.10, showboost).
C-states provide different idle states for when execution is halted, saving power. The C-states are
shown in Table 6.2: C0 is for normal operation, and C1 and above are for idle states: the higher
the number, the deeper the state.

Table 6.2

Processor power states (C-states)

C-state

Description

C0

Executing. The CPU is fully on, processing instructions.

C1

Halts execution. Entered by the hlt instruction. Caches are maintained. Wakeup
latency is the lowest from this state.

C1E

Enhanced halt with lower power consumption (supported by some processors).

C2

Halts execution. Entered by a hardware signal. This is a deeper sleep state with
higher wakeup latency.

C3

A deeper sleep state with improved power savings over C1 and C2. The caches
may maintain state, but stop snooping (cache coherency), deferring it to the OS.

Processor manufacturers can define additional states beyond C3. Some Intel processors define
additional levels up to C10 where more processor functionality is powered down, including
cache contents.

