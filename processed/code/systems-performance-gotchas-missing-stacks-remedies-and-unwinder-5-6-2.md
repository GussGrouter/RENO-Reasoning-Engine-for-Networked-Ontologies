<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
entry_SYSCALL_64_after_hwframe
pthread_cond_timedwait@@GLIBC_2.3.2
[unknown]

This stack is incomplete: after pthread_cond_timedwait() is a single “[unknown]” frame. It’s
missing the MySQL functions beneath this point, and it’s those MySQL functions we really need
to understand application context.
Sometimes the stack is a single frame:
send

In flame graphs this can appear as “grass”: many thin single frames at the bottom of the profile.
Incomplete stack traces are unfortunately common, and are usually caused by a confluence of
two factors: 1) the observability tool using a frame pointer-based approach for reading the stack
trace, and 2) the target binary not reserving a register (RBP on x86_64) for the frame pointer,
instead reusing it as a general-purpose register as a compiler performance optimization. The
observability tool reads this register expecting it to be a frame pointer, but in fact it could now
contain anything: numbers, object address, pointers to strings, etc. The observability tool tries
to resolve this number in the symbol table and, if it is lucky, it doesn’t find it and can print
“[unknown]”. If it is unlucky, that random number resolves to an unrelated symbol, and now the
printed stack trace has a function name that is wrong, confusing you, the end user.
Since the libc library is typically compiled without frame pointers, broken stacks are common
in any path through libc, including the two examples earlier: pthread_cond_timedwait() and
send().17
The easiest solution is usually to fix the frame pointer register:
■

