<!-- pdftotext -f 182 -l 230 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
5.3.1 Compiled Languages
Compilation takes a program and generates machine instructions in advance of runtime that
are stored in binary executable files called binaries, which commonly use the Executable and
Linking Format (ELF) on Linux and other Unix derivatives, and the Portable Executable (PE) format on Windows. These can be run at any time without compiling again. Compiled languages
include C, C++, and assembly. Some languages may have both interpreters and compilers.
Compiled code is generally high-performing as it does not require further translation before
execution by the CPUs. A common example of compiled code is the Linux kernel, which is
written mostly in C, with some critical paths written in assembly.
Performance analysis of compiled languages is usually straightforward, as the executed machine
code usually maps closely to the original program (although this depends on compilation
optimizations). During compilation, a symbol table can be generated that maps addresses to
program functions and object names. Later profiling and tracing of CPU execution can then
be mapped directly to these program names, allowing the analyst to study program execution.
Stack traces, and the numerical addresses they contain, can also be mapped and translated to
function names to provide code path ancestry.
Compilers can improve performance by use of compiler optimizations—routines that optimize the
choice and placement of CPU instructions.

Compiler Optimizations
The gcc(1) compiler offers seven levels of optimization: 0, 1, 2, 3, s, fast, and g. The numbers are a
range where 0 uses the least optimizations and 3 uses the most. There are also “s” to optimize for
size, “g” for debugging, and “fast” to use all optimizations plus extras that disregard standards
compliance. You can query gcc(1) to show which optimizations it uses for different levels. For
example:
$ gcc -Q -O3 --help=optimizers
The following options control optimizations:
-O<number>
-Ofast
-Og
-Os
-faggressive-loop-optimizations

[enabled]

-falign-functions

[disabled]

-falign-jumps

[disabled]

-falign-label

[enabled]

-falign-loops

[disabled]

-fassociative-math

[disabled]

-fasynchronous-unwind-tables

[enabled]

183

184

Chapter 5 Applications

-fauto-inc-dec

[enabled]

-fbranch-count-reg

[enabled]

-fbranch-probabilities

[disabled]

-fbranch-target-load-optimize

[disabled]

[...]
-fomit-frame-pointer

[enabled]

[...]

The full list for gcc version 7.4.0 includes about 230 options, some of which are enabled even at
–O0. As an example of what one of these options does, the -fomit-frame-pointer option, seen in
this list, is described in the gcc(1) man page:
Don’t keep the frame pointer in a register for functions that don’t need one. This avoids
the instructions to save, set up and restore frame pointers; it also makes an extra register
available in many functions. It also makes debugging impossible on some machines.
This is an example of a trade-off: omitting the frame pointer typically breaks the operation of
analyzers that profile stack traces.
Given the usefulness of stack profilers, this option may sacrifice much in terms of later performance wins that can no longer be easily found, which may far outweigh the performance gains
that this option initially offers. A solution, in this case, can be to compile with -fno-omitframe-pointer to avoid this optimization.6 Another recommended option is -g to include
debuginfo, to aid later debugging. Debuginfo can be removed or stripped later if need be.7
Should performance issues arise, it may be tempting to simply recompile the application with a
reduced optimization level (from –O3 to –O2, for example) in the hope that any debugging needs
could then be met. This turns out not to be simple: the changes to the compiler output can be
massive and important, and may affect the behavior of the issue you were originally trying to
analyze.

