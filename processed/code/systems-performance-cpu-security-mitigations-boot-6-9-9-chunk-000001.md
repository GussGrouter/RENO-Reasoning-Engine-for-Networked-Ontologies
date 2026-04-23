6.9.9 Security Boot Options
Various kernel mitigations for the Meltdown and Spectre security vulnerabilities have the side
effect of reducing performance. There may be some scenario where security is not a requirement but high performance is, and you wish to disable these mitigations. Because this is not
recommended (due to the security risk), I will not include all the options here; but you should
know that they exist. They are grub command line options that include nospectre_v1 and
nospectre_v2. These are documented in Documentation/admin-guide/kernel-parameters.txt in
the Linux source [Linux 20f]; an excerpt:
nospectre_v1

[PPC] Disable mitigations for Spectre Variant 1 (bounds
check bypass). With this option data leaks are possible
in the system.

nospectre_v2

[X86,PPC_FSL_BOOK3E,ARM64] Disable all mitigations for
the Spectre variant 2 (indirect branch prediction)
vulnerability. System may allow data leaks with this
option.

There is also a website that lists them: https://make-linux-fast-again.com. This website lacks the
warnings listed in the kernel documentation.
