ZFS
ZFS comes with zpool(1M), which has an iostat suboption for observing ZFS pool statistics. It
reports pool operation rates (reads and writes) and throughput.

A popular add-on has been the arcstat.pl tool, which reports ARC and L2ARC size and hit and
miss rates.

(Omitted in this processed extract: full `arcstat 1` numeric grid — see PDF.)

The statistics are per interval and include (among others): total ARC accesses and misses; ARC miss
percent total/demand/prefetch/metadata; misses split by demand/prefetch/metadata; ARC size and
target size (`arcsz`, `c`).

arcstat.pl is a Perl program that reads statistics from kstat.
