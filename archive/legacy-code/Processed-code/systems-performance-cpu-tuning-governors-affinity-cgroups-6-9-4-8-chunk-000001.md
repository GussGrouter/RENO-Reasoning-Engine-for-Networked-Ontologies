<!-- pdftotext -f 321 -l 360 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continued) -->

6.9.4 Scaling Governors
Linux supports different CPU scaling governors that control the CPU clock frequencies via software (the kernel). These can be set via /sys files. For example, for CPU 0:
# cat /sys/devices/system/cpu/cpufreq/policy0/scaling_available_governors
performance powersave
# cat /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
powersave

This is an example of an untuned system: the current governor is “powersave,” which will use
lower CPU frequencies to save power. This can be set to “performance” to always use the maximum frequency. For example:
# echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor

This must be done for all CPUs (policy0..N). This policy directory also contains files for setting
the frequency directly (scaling_setspeed) and determining the range of possible frequencies
(scaling_min_freq, scaling_max_freq).
Setting the CPUs to always run at maximum frequency may come with an enormous cost to the
environment. If this setting does not provide a significant performance improvement, consider
continuing to use the powersave setting for the sake of the planet. For hosts with the access
to power MSRs (cloud guests may filter them), you can also use these MSRs to instrument the
power consumed with and without a max CPU frequency setting, to quantify (part of20) the
environmental cost.

6.9.5 Power States
Processor power states can be enabled and disabled using the cpupower(1) tool. As seen earlier
in Section 6.6.21, Other Tools, deeper sleep states can have high exit latency (890 μs for C10
was shown). Individual states can be disabled using -d, and -D latency will disable all states
with higher exit latency than that given (in microseconds). This allows you to fine-tune which
lower-power states may be used, disabling those with excessive latency.

6.9.6

CPU Binding

A process may be bound to one or more CPUs, which may increase its performance by improving
cache warmth and memory locality.
On Linux, this can be performed using the taskset(1) command, which uses a CPU mask or
ranges to set CPU affinity. For example:
$ taskset -pc 7-10 10790
pid 10790's current affinity list: 0-15
pid 10790's new affinity list: 7-10
20

Host-based power measurements do not account for the environmental costs of server air conditioning, server
manufacturing and transportation, and other costs.

297

298

Chapter 6 CPUs

This sets PID 10790 to run only on CPUs 7 through 10.
The numactl(8) command can also set CPU binding as well as memory node binding (see
Chapter 7, Memory, Section 7.6.4, NUMA Binding).

6.9.7

Exclusive CPU Sets

Linux provides cpusets, which allow CPUs to be grouped and processes assigned to them. This
can improve performance similarly to CPU binding, but performance can be further improved
by making the cpuset exclusive, preventing other processes from using it. The trade-off is a
reduction in available CPU for the rest of the system.
The following commented example creates an exclusive set:
# mount -t cgroup -ocpuset cpuset /sys/fs/cgroup/cpuset

# may not be necessary

# cd /sys/fs/cgroup/cpuset
# mkdir prodset

# create a cpuset called "prodset"

# cd prodset
# echo 7-10 > cpuset.cpus

# assign CPUs 7-10

# echo 1 > cpuset.cpu_exclusive
# echo 1159 > tasks

# make prodset exclusive

# assign PID 1159 to prodset

For reference, see the cpuset(7) man page.
When creating CPU sets, you may also wish to study which CPUs will continue to service interrupts. The irqbalance(1) daemon will attempt to distribute interrupts across CPUs to improve
performance. You can manually set CPU affinity by IRQ via the /proc/irq/IRQ/smp_affinity files.

6.9.8 Resource Controls
Apart from associating processes with whole CPUs, modern operating systems provide resource
controls for fine-grained allocation of CPU usage.
For Linux, there are control groups (cgroups), which can also control resource usage by processes
or groups of processes. CPU usage can be controlled using shares, and the CFS scheduler allows
fixed limits to be imposed (CPU bandwidth), in terms of allocating microseconds of CPU cycles
per interval.
Chapter 11, Cloud Computing, describes a use case of managing the CPU usage of OS virtualized
tenants, including how shares and limits can be used in concert.

