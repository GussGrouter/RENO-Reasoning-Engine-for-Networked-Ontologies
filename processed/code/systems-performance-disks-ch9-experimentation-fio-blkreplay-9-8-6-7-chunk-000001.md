9.8.6       fio
The flexible IO tester (fio) is a file system benchmark tool that can also shed light on disk device
performance, especially when used with the --direct=true option to use non-buffered I/O
(when non-buffered I/O is supported by the file system). It was introduced in Chapter 8, File
Systems, Section 8.7.2, Micro-Benchmark Tools.


9.8.7      blkreplay
The block I/O replay tool (blkreplay) can replay block I/O loads captured with blktrace (Section
9.6.10, blktrace) or Windows DiskMon [Schöbel-Theuer 12]. This can be useful when debugging
disk issues that are difficult to reproduce with micro-benchmark tools.

See Chapter 12, Benchmarking, Section 12.2.3, replay, for an example of how disk I/O replays
can be misleading if the target system has changed.



