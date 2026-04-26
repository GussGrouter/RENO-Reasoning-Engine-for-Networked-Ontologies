5.3.3

Virtual Machines

A language virtual machine (also called a process virtual machine) is software that simulates a computer. Some programming languages, including Java and Erlang, are commonly executed using
virtual machines (VMs) that provide them with a platform-independent programming environment. The application program is compiled to the virtual machine instruction set (bytecode) and
then executed by the virtual machine. This allows portability of the compiled objects, provided
a virtual machine is available to run them on the target platform.
The bytecode can be executed by the language virtual machine in different ways. The Java
HotSpot Virtual Machine supports execution via interpretation and also JIT compilation, which
compiles bytecode to machine code for direct execution by the processor. This provides the performance advantages of compiled code, together with the portability of a virtual machine.
Virtual machines are typically the most difficult of the language types to observe. By the time
the program is executing on-CPU, multiple stages of compilation or interpretation may have
passed, and information about the original program may not be readily available. Performance
analysis usually focuses on the toolset provided with the language virtual machine, many of
which provide USDT probes, and on third-party tools.

