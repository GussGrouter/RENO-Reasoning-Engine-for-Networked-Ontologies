# Should sadc collect system activity informations? Valid values
# are "true" and "false". Please do not put other values, they
# will be overwritten by debconf!
ENABLED="true"

And then restarting sysstat using:
ubuntu# service sysstat restart

The schedule of statistic recording can be modified in the crontab file for sysstat:
ubuntu# cat /etc/cron.d/sysstat
# The first element of the path is a directory where the debian-sa1
# script is located
PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin
# Activity reports every 10 minutes everyday
5-55/10 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1
# Additional run at 23:59 to rotate the statistics file
59 23 * * * root command -v debian-sa1 > /dev/null && debian-sa1 60 2

The syntax 5-55/10 means it will record every 10 minutes for the minute range 5 to 55 minutes
past the hour. You can adjust this to suit the resolution desired: the syntax is documented in the
crontab(5) man page. More frequent data collection will increase the size of the sar(1) archive
files, which can be found in /var/log/sysstat.
I often change data collection to:
*/5 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1 -S ALL

The */5 will record every five minutes, and the -S ALL will record all statistics. By default sar(1)
will record most (but not all) statistic groups. The -S ALL option is used to record all statistic
groups—it is passed to sadc(1), and documented in the man page for sadc(1). There is also an
extended version, -S XALL, which records additional breakdowns of statistics.

4.4 sar

Reporting
sar(1) can be executed with any of the options shown in Figure 4.6 to report the selected statistic
group. Multiple options can be specified. For example, the following reports CPU statistics (-u),
TCP (-n TCP), and TCP errors (-n ETCP):
$ sar -u -n TCP,ETCP
Linux 4.15.0-66-generic (bgregg)

01/19/2020

_x86_64_

(8 CPU)

10:40:01 AM

CPU

%user

%nice

%system

%iowait

%steal

%idle

10:45:01 AM

all

6.87

0.00

2.84

0.18

0.00

90.12

10:50:01 AM

all

6.87

0.00

2.49

0.06

0.00

90.58

iseg/s

oseg/s

[...]
10:40:01 AM

active/s passive/s

10:45:01 AM

0.16

0.00

10.98

9.27

10:50:01 AM

0.20

0.00

10.40

8.93

[...]
10:40:01 AM

atmptf/s

10:45:01 AM

0.04

estres/s retrans/s isegerr/s
0.02

0.46

0.00

orsts/s
0.03

10:50:01 AM

0.03

0.02

0.53

0.00

0.03

[...]

The first line of output is a system summary, showing the kernel type and version, the hostname,
the date, processor architecture, and number of CPUs.
Running sar -A will dump all statistics.

Output Formats
The sysstat package comes with an sadf(1) command for viewing sar(1) statistics in different
formats, including JSON, SVG, and CSV. The following examples emit the TCP (-n TCP) statistics
in these formats.

JSON (-j):
JavaScript Object Notation (JSON) can be easily parsed and imported by many programming
languages, making it a suitable output format when building other software upon sar(1).
$ sadf -j -- -n TCP
{"sysstat": {
"hosts": [
{
"nodename": "bgregg",
"sysname": "Linux",
"release": "4.15.0-66-generic",
"machine": "x86_64",
"number-of-cpus": 8,

163

164

Chapter 4 Observability Tools

"file-date": "2020-01-19",
"file-utc-time": "18:40:01",
"statistics": [
{
