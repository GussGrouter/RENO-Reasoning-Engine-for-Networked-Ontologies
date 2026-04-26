7.6.5

Resource Controls

Basic resource controls, including setting a main memory limit and a virtual memory limit, may
be available using ulimit(1).
For Linux, the container groups (cgroups) memory subsystem provides various additional controls.
These include:
■

memory.limit_in_bytes: The maximum allowed user memory, including file cache usage,
in bytes

11
Note that historically there were performance issues with transparent huge pages, deterring its usage. These
issues have hopefully been fixed.

353

354

Chapter 7 Memory

■

memory.memsw.limit_in_bytes: The maximum allowed memory and swap space, in bytes
(when swap is in use)

■

memory.kmem.limit_in_bytes: The maximum allowed kernel memory, in bytes

■

memory.tcp.limit_in_bytes: The maximum tcp buffer memory, in bytes.

■

memory.swappiness: Similar to vm.swappiness described earlier but can be set for a cgroup

■

memory.oom_control: Can be set to 0, to allow the OOM killer for this cgroup, or 1, to
disable it

Linux also allows system-wide configuration in /etc/security/limits.conf.
For more on resource controls, see Chapter 11, Cloud Computing.

