<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (book PDF region ~171–220) -->
"timestamp": {"date": "2020-01-19", "time": "18:45:01", "utc": 1,
"interval": 300},
"network": {
"net-tcp": {"active": 0.16, "passive": 0.00, "iseg": 10.98, "oseg": 9.27}
}
},
[...]

You can process the JSON output at the command line using the jq(1) tool.

SVG (-g):
sadf(1) can emit Scalable Vector Graphics (SVG) files that can be viewed in web browsers.
Figure 4.7 shows an example. You can use this output format to build rudimentary dashboards.

Figure 4.7 sar(1) sadf(1) SVG output12

12

Note that I edited the SVG file to make this figure more legible, changing colors and increasing font sizes.

4.4 sar

CSV (-d):
The comma-separated values (CSV) format is intended for import by databases (and uses a
semicolon):
$ sadf -d -- -n TCP
# hostname;interval;timestamp;active/s;passive/s;iseg/s;oseg/s
bgregg;300;2020-01-19 18:45:01 UTC;0.16;0.00;10.98;9.27
bgregg;299;2020-01-19 18:50:01 UTC;0.20;0.00;10.40;8.93
bgregg;300;2020-01-19 18:55:01 UTC;0.12;0.00;9.27;8.07
[...]

4.4.3

sar(1) Live

When executed with an interval and optional count, sar(1) does live reporting. This mode can
be used even when data collection is not enabled.
For example, showing the TCP statistics with an interval of one second and a count of five:
$ sar -n TCP 1 5
Linux 4.15.0-66-generic (bgregg)

01/19/2020

03:09:04 PM

active/s passive/s

_x86_64_

iseg/s

oseg/s

03:09:05 PM

1.00

0.00

33.00

42.00

03:09:06 PM

0.00

0.00

109.00

86.00

03:09:07 PM

0.00

0.00

107.00

67.00

03:09:08 PM

0.00
