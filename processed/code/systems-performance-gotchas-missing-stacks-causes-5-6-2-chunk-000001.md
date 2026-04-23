[Gregg 20c], which should be run immediately after the profile and before symbol translation.
For example, using perf(1) (Chapter 13):
# perf record -F 49 -a -g -- sleep 10; jmaps
# perf script --header > out.stacks
# [...]

And using bpftrace (Chapter 15):
# bpftrace --unsafe -e 'profile:hz:49 { @[ustack] = count(); }
interval:s:10 { exit(); } END { system("jmaps"); }'

A symbol mapping may change between the profile sample and the symbol table dump, producing
invalid function names in the profile. This is called symbol churn, and running jmaps immediately after perf record reduces it. It has so far not been a serious problem; if it was, a symbol
dump could be taken before and after the profile to look for changes.
There are other approaches for resolving JIT symbols. One is to use symbol-timestamp logging,
which is supported by perf(1) and solves the symbol churn problem, albeit with higher overhead while enabled. Another is for perf(1) to call into the runtime’s own stack walker (which
typically exists for exception stacks). This approach is sometimes called using stack helpers, and
for Java it has been implemented by the async-profiler [Pangin 20].
Note that JIT runtimes also also have precompiled components: the JVM also uses libjvm and
libc. See the previous ELF binaries section for addressing those components.


5.6 Gotchas

5.6.2 Missing Stacks
Another common problem is missing or incomplete stack traces, perhaps as short as one or two
frames. For example, from an off-CPU profile of MySQL server:
finish_task_switch
schedule
futex_wait_queue_me
futex_wait
do_futex
__x64_sys_futex
do_syscall_64
