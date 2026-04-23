
17

For C/C++ software, and others compiled with gcc(1) or LLVM: Recompile the software
with -fno-omit-frame-pointer.
For Java: Run java(1) with -XX:+PreserveFramePointer.

I’ve sent build instructions to package maintainers asking for a libc with frame pointers to be packaged.

215


216

Chapter 5 Applications

This may come with a performance cost, but it has often been measured at less than 1%; the
benefits of being able to use stack traces to find performance wins usually far outweigh this cost.
The other approach is to switch to a stack walking technique that is not frame pointer-based.
perf(1) supports DWARF-based stack walking, ORC, and last branch record (LBR). Other stack
walking methods are mentioned in Chapter 13, perf, Section 13.9, perf record.
At the time of writing, DWARF-based and LBR stack walking are not available from BPF, and
ORC is not yet available for user-level software.

5.7

Exercises

1. Answer the following questions about terminology:
