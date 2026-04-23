      9.8.5     ioping
      ioping(1) is an interesting disk micro-benchmark tool that resembles the ICMP ping(8) utility.
      Running ioping(1) on the nvme0n1 disk device:

      # ioping /dev/nvme0n1
      4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=1 time=438.7 us (warmup)
      4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=2 time=421.0 us
      4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=3 time=449.4 us
      4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=4 time=412.6 us
      4 KiB <<< /dev/nvme0n1 (block device 8 GiB): request=5 time=468.8 us
      ^C
      --- /dev/nvme0n1 (block device 8 GiB) ioping statistics ---
      4 requests completed in 1.75 ms, 16 KiB read, 2.28 k iops, 8.92 MiB/s
      generated 5 requests in 4.37 s, 20 KiB, 1 iops, 4.58 KiB/s
      min/avg/max/mdev = 412.6 us / 437.9 us / 468.8 us / 22.4 us

      By default ioping(1) issues a 4 Kbyte read per second and prints its I/O latency in microseconds.
      When terminated, various statistics are printed.

      What makes ioping(1) different to other benchmark tools is that its workload is lightweight.
      Here is some iostat(1) output while ioping(1) was running:

      $ iostat -xsz 1
      [...]
      Device                tps         kB/s      rqm/s   await aqu-sz      areq-sz   %util
      nvme0n1              1.00         4.00      0.00     0.00     0.00       4.00    0.40

      The disk was driven to only 0.4% utilization. ioping(1) could possibly be used to debug issues in
      production environments where other micro-benchmarks would be unsuitable, as they typically
      drive the target disks to 100% utilization.
                                                                                         9.9    Tuning   493



