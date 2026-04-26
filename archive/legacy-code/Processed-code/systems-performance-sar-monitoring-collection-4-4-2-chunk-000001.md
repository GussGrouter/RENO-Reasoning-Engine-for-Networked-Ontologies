require text parsing to process, costing some CPU cycles.

4.4

sar

sar(1) was introduced in Section 4.2.4, Monitoring, as a key monitoring facility. While there
has been much excitement recently with BPF tracing superpowers (and I’m partly responsible),
you should not overlook the utility of sar(1)—it’s an essential systems performance tool that
can solve many performance issues on its own. The Linux version of sar(1) is also well-designed,
having self-descriptive column headings, network metric groups, and detailed documentation
(man pages).
sar(1) is provided via the sysstat package.

4.4 sar

4.4.1

sar(1) Coverage

Figure 4.6 shows the observability coverage from the different sar(1) command line options.

Figure 4.6 Linux sar(1) observability
This figure shows that sar(1) provides broad coverage of the kernel and devices, and even has
observability for fans. The -m (power management) option also supports other arguments not
shown in this figure, including IN for voltage inputs, TEMP for device temperatures, and USB for
USB device power statistics.

4.4.2

sar(1) Monitoring

You may find that sar(1) data collecting (monitoring) is already enabled for your Linux systems.
If it isn’t, you need to enable it. To check, simply run sar without options. For example:
$ sar
Cannot open /var/log/sysstat/sa19: No such file or directory
Please check if data collecting is enabled

The output shows that sar(1) data collecting is not yet enabled on this system (the sa19 file refers
to the daily archive for the 19th of the month). The steps to enable it may vary based on your
distribution.

161

162

Chapter 4 Observability Tools

Configuration (Ubuntu)
On this Ubuntu system, I can enable sar(1) data collecting by editing the /etc/default/sysstat file
and setting ENABLED to be true:
ubuntu# vi /etc/default/sysstat
#
# Default settings for /etc/init.d/sysstat, /etc/cron.d/sysstat
# and /etc/cron.daily/sysstat files
#
