3.5.1 PGO Kernels
Profile-guided optimization (PGO), also known as feedback-directed optimization (FDO), uses
CPU profile information to improve compiler decisions [Yuan 14a]. This can be applied to kernel
builds, where the procedure is:
1. While in production, take a CPU profile.
2. Recompile the kernel based on that CPU profile.
3. Deploy the new kernel in production.
This creates a kernel with improved performance for a specific workload. Runtimes such as the
JVM do this automatically, recompiling Java methods based on their runtime performance, in
conjunction with just-in-time (JIT) compilation. The process for creating a PGO kernel instead
involves manual steps.
A related compile optimization is link-time optimization (LTO), where an entire binary is compiled at once to allow optimizations across the entire program. The Microsoft Windows kernel
makes heavy use of both LTO and PGO, seeing 5 to 20% improvements from PGO [Bearman 20].
Google also use LTO and PGO kernels to improve performance [Tolvanen 20].
The gcc and clang compilers, and the Linux kernel, all have support for PGO. Kernel PGO
typically involves running a specially instrumented kernel to collect profile data. Google has
released an AutoFDO tool that bypasses the need for such a special kernel: AutoFDO allows a
profile to be collected from a normal kernel using perf(1), which is then converted to the correct
format for compilers to use [Google 20a].
The only recent documentation on building a Linux kernel with PGO or AutoFDO is two talks
from Linux Plumber’s Conference 2020 by Microsoft [Bearman 20] and Google [Tolvanen 20].15
15
For a while the most recent documentation was from 2014 for Linux 3.13 [Yuan 14b], hindering adoption on newer
kernels.
