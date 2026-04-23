3.4.2 systemd
systemd is a commonly used service manager for Linux, developed as a replacement for the original UNIX init system. systemd has various features including dependency-aware service startup
and service time statistics.
An occasional task in systems performance is to tune the system’s boot time, and the systemd time
statistics can show where to tune. The overall boot time can be reported using systemd-analyze(1):
# systemd-analyze
Startup finished in 1.657s (kernel) + 10.272s (userspace) = 11.930s
graphical.target reached after 9.663s in userspace

This output shows that the system booted (reached the graphical.target in this case) in 9.663
seconds. More information can be seen using the critical-chain subcommand:
# systemd-analyze critical-chain
The time when unit became active or started is printed after the "@" character.
The time the unit took to start is printed after the "+" character.
graphical.target @9.663s
└─multi-user.target @9.661s
└─snapd.seeded.service @9.062s +62ms
└─basic.target @6.336s
└─sockets.target @6.334s
└─snapd.socket @6.316s +16ms
└─sysinit.target @6.281s
└─cloud-init.service @5.361s +905ms
└─systemd-networkd-wait-online.service @3.498s +1.860s
└─systemd-networkd.service @3.254s +235ms
└─network-pre.target @3.251s
└─cloud-init-local.service @2.107s +1.141s
└─systemd-remount-fs.service @391ms +81ms
└─systemd-journald.socket @387ms
└─system.slice @366ms
└─-.slice @366ms

This output shows the critical path: the sequence of steps (in this case, services) that causes the
latency. The slowest service was systemd-networkd-wait-online.service, taking 1.86 seconds
to start.
There are other useful subcommands: blame shows the slowest initialization times, and plot
produces an SVG diagram. See the man page for systemd-analyze(1) for more information.

