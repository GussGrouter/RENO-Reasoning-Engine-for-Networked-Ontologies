<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs begins in this extract) -->
example, a 4 GHz CPU performs 4 billion clock cycles per second.
Some processors are able to vary their clock rate, increasing it to improve performance or
decreasing it to reduce power consumption. The rate may be varied on request by the operating
system, or dynamically by the processor itself. The kernel idle thread, for example, can request
the CPU to throttle down to save power.
Clock rate is often marketed as the primary feature of a processor, but this can be a little misleading. Even if the CPU in your system appears to be fully utilized (a bottleneck), a faster clock rate
may not speed up performance—it depends on what those fast CPU cycles are actually doing.
If they are mostly stall cycles while waiting on memory access, executing them more quickly
doesn’t actually increase the CPU instruction rate or workload throughput.

6.3.2 Instructions
CPUs execute instructions chosen from their instruction set. An instruction includes the following steps, each processed by a component of the CPU called a functional unit:
1. Instruction fetch
2. Instruction decode
3. Execute
4. Memory access
5. Register write-back
The last two steps are optional, depending on the instruction. Many instructions operate on
registers only and do not require the memory access step.
Each of these steps takes at least a single clock cycle to be executed. Memory access is often the
slowest, as it may take dozens of clock cycles to read or write to main memory, during which
instruction execution has stalled (and these cycles while stalled are called stall cycles). This is why
CPU caching is important, as described in Section 6.4.1, Hardware: it can dramatically reduce
the number of cycles needed for memory access.

223


224

Chapter 6 CPUs

6.3.3 Instruction Pipeline
The instruction pipeline is a CPU architecture that can execute multiple instructions in parallel by
executing different components of different instructions at the same time. It is similar to a factory
assembly line, where stages of production can be executed in parallel, increasing throughput.
Consider the instruction steps previously listed. If each were to take a single clock cycle, it would
take five cycles to complete the instruction. At each step of this instruction, only one functional
unit is active and four are idle. By use of pipelining, multiple functional units can be active at
the same time, processing different instructions in the pipeline. Ideally, the processor can then
complete one instruction with every clock cycle.
Instruction pipelining may involve breaking down an instruction into multiple simple steps for
execution in parallel. (Depending on the processor, these steps may become simple operations
called micro-operations (uOps) for execution by a processor area called the back-end. The front-end
of such a processor is responsible for fetching instructions and branch prediction.)

Branch Prediction
Modern processors can perform out-of-order execution of the pipeline, where later instructions
can be completed while earlier instructions are stalled, improving instruction throughput.
However, conditional branch instructions pose a problem. Branch instructions jump execution
to a different instruction, and conditional branches do so based on a test. With conditional
branches, the processor does not know what the later instructions will be. As an optimization,
processors often implement branch prediction, where they will guess the outcome of the test and
begin processing the outcome instructions. If the guess later proves to be wrong, the progress
in the instruction pipeline must be discarded, hurting performance. To improve the chances of
guessing correctly, programmers can place hints in the code (e.g., likely() and unlikely() macros
in the Linux Kernel sources).

6.3.4 Instruction Width
