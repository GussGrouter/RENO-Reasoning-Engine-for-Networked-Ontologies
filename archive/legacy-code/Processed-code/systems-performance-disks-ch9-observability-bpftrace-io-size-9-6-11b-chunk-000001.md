Disk I/O Size
Sometimes disk I/O is slow simply because it is large, especially for SSD drives. Another sizebased issue is when an application requests many small I/O, which instead could be aggregated
into larger sizes to reduce I/O stack overheads. Both of these issues can be investigated by examining the I/O size distribution.
Using bpftrace, the following shows a disk I/O size distribution broken down by the requesting
process name:
# bpftrace -e 't:block:block_rq_issue /args->bytes/ { @[comm] = hist(args->bytes); }'
Attaching 1 probe...
^C
[...]
@[kworker/3:1H]:
[4K, 8K)

1 |@@@@@@@@@@

|

[8K, 16K)

0 |

|

[16K, 32K)

0 |

|

[32K, 64K)

0 |

|

[64K, 128K)

0 |

|

[128K, 256K)

0 |

|

[256K, 512K)

0 |

|

[512K, 1M)

5 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

[1M, 2M)

3 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

|

9.6 Observability Tools

@[dmcrypt_write]:
[4K, 8K)

103 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

[8K, 16K)

46 |@@@@@@@@@@@@@@@@@@@@@@@

|

[16K, 32K)

11 |@@@@@

|

[32K, 64K)

0 |

|

[64K, 128K)

1 |

|

[128K, 256K)

1 |

|

The output shows processes named dmcrypt_write performing small I/O, mostly in the 4 to
32 Kbyte range.
