  Systems
Performance

  Second Edition
This page intentionally left blank
                 Systems
               Performance
             Enterprise and the Cloud
                             Second Edition


                                  Brendan Gregg




          Boston • Columbus • New York • San Francisco • Amsterdam • Cape Town
Dubai • London • Madrid • Milan • Munich • Paris • Montreal • Toronto • Delhi • Mexico City
            São Paulo • Sydney • Hong Kong • Seoul • Singapore • Taipei • Tokyo
Many of the designations used by manufacturers and sellers to distinguish their products         Publisher
are claimed as trademarks. Where those designations appear in this book, and the                 Mark L. Taub
publisher was aware of a trademark claim, the designations have been printed with initial
                                                                                                 Executive Editor
capital letters or in all capitals.
                                                                                                 Greg Doench
The author and publisher have taken care in the preparation of this book, but make no            Managing Producer
expressed or implied warranty of any kind and assume no responsibility for errors or             Sandra Schroeder
omissions. No liability is assumed for incidental or consequential damages in connection
with or arising out of the use of the information or programs contained herein.                  Sr. Content
                                                                                                 Producer
For information about buying this title in bulk quantities, or for special sales opportunities   Julie B. Nahil
(which may include electronic versions; custom cover designs; and content particular to
                                                                                                 Project Manager
your business, training goals, marketing focus, or branding interests), please contact our
corporate sales department at corpsales@pearsoned.com or (800) 382-3419.                         Rachel Paul
                                                                                                 Copy Editor
For government sales inquiries, please contact governmentsales@pearsoned.com.
                                                                                                 Kim Wimpsett
For questions about sales outside the U.S., please contact intlcs@pearson.com.                   Indexer
Visit us on the Web: informit.com/aw                                                             Ted Laux
                                                                                                 Proofreader
Library of Congress Control Number: 2020944455
                                                                                                 Rachel Paul
Copyright © 2021 Pearson Education, Inc.                                                         Compositor
All rights reserved. This publication is protected by copyright, and permission must be          The CIP Group
obtained from the publisher prior to any prohibited reproduction, storage in a retrieval
system, or transmission in any form or by any means, electronic, mechanical, photocopy-
ing, recording, or likewise. For information regarding permissions, request forms and
the appropriate contacts within the Pearson Education Global Rights & Permissions
Department, please visit www.pearson.com/permissions.
Cover images by Brendan Gregg
Page 9, Figure 1.5: Screenshot of System metrics GUI (Grafana) © 2020 Grafana Labs
Page 84, Figure 2.32: Screenshot of Firefox timeline chart © Netflix
Page 164, Figure 4.7: Screenshot of sar(1) sadf(1) SVG output © 2010 W3C
Page 560, Figure 10.12: Screenshot of Wireshark screenshot © Wireshark
Page 740, Figure 14.3: Screenshot of KernelShark © KernelShark
ISBN-13: 978-0-13-682015-4
ISBN-10: 0-13-682015-8
ScoutAutomatedPrintCode
     For Deirdré Straughan,
 an amazing person in technology,
and an amazing person—we did it.
This page intentionally left blank
Contents at a Glance
    Contents     ix
    Preface    xxix
    Acknowledgments xxxv
    About the Author        xxxvii

 1 Introduction       1
 2 Methodologies          21

 3 Operating Systems            89

 4 Observability Tools          129

 5 Applications 171

 6 CPUs       219

 7 Memory 303

 8 File Systems 359

 9 Disks      423

10 Network 499

11 Cloud Computing           579

12 Benchmarking           641

13 perf 671

14 Ftrace     705

15 BPF     751

16 Case Study         783

 A USE Method: Linux            795

 B sar Summary            801

 C bpftrace One-Liners          803

D Solutions to Selected Exercises     809

 E Systems Performance Who’s Who 811

    Glossary 815

    Index 825
This page intentionally left blank
Contents
   Preface    xxix
   Acknowledgments xxxv
   About the Author              xxxvii

1 Introduction         1
   1.1    Systems Performance                   1
   1.2    Roles      2
   1.3    Activities         3
   1.4 Perspectives 4
   1.5    Performance Is Challenging                     5
     1.5.1 Subjectivity 5
     1.5.2 Complexity 5
     1.5.3     Multiple Causes                 6
     1.5.4     Multiple Performance Issues 6
   1.6    Latency        6
   1.7    Observability           7
     1.7.1     Counters, Statistics, and Metrics             8
     1.7.2     Profiling          10
     1.7.3     Tracing           11
   1.8    Experimentation              13
   1.9    Cloud Computing                 14
   1.10    Methodologies               15
     1.10.1 Linux Perf Analysis in 60 Seconds                    15
   1.11    Case Studies               16
     1.11.1       Slow Disks              16
     1.11.2       Software Change                   18
     1.11.3 More Reading                       19
   1.12 References                19

2 Methodologies              21
   2.1    Terminology            22
   2.2    Models         23
     2.2.1     System Under Test                    23
     2.2.2     Queueing System                     23
   2.3    Concepts           24
     2.3.1     Latency            24
     2.3.2     Time Scales                25
x   Contents


           2.3.3    Trade-Offs 26
           2.3.4    Tuning Efforts      27
           2.3.5    Level of Appropriateness             28
           2.3.6    When to Stop Analysis           29
           2.3.7    Point-in-Time Recommendations                29
           2.3.8    Load vs. Architecture 30
           2.3.9    Scalability    31
           2.3.10 Metrics 32
           2.3.11    Utilization    33
           2.3.12    Saturation      34
           2.3.13    Profiling     35
           2.3.14    Caching       35
           2.3.15    Known-Unknowns            37
        2.4 Perspectives 37
           2.4.1    Resource Analysis          38
           2.4.2 Workload Analysis 39
        2.5 Methodology 40
           2.5.1    Streetlight Anti-Method            42
           2.5.2 Random Change Anti-Method 42
           2.5.3    Blame-Someone-Else Anti-Method                43
           2.5.4 Ad Hoc Checklist Method                 43
           2.5.5 Problem Statement 44
           2.5.6 Scientific Method 44
           2.5.7 Diagnosis Cycle 46
           2.5.8 Tools Method           46
           2.5.9 The USE Method              47
           2.5.10    The RED Method            53
           2.5.11 Workload Characterization                 54
           2.5.12    Drill-Down Analysis 55
           2.5.13    Latency Analysis          56
           2.5.14    Method R 57
           2.5.15 Event Tracing 57
           2.5.16    Baseline Statistics          59
           2.5.17    Static Performance Tuning              59
           2.5.18    Cache Tuning         60
           2.5.19 Micro-Benchmarking                60
           2.5.20    Performance Mantras               61
                                                                      Contents   xi



  2.6    Modeling 62
     2.6.1    Enterprise vs. Cloud          62
     2.6.2    Visual Identification         62
     2.6.3    Amdahl’s Law of Scalability              64
     2.6.4 Universal Scalability Law 65
     2.6.5    Queueing Theory         66
  2.7    Capacity Planning       69
     2.7.1    Resource Limits         70
     2.7.2    Factor Analysis     71
     2.7.3    Scaling Solutions        72
  2.8 Statistics 73
     2.8.1    Quantifying Performance Gains                 73
     2.8.2 Averages 74
     2.8.3    Standard Deviation, Percentiles, Median            75
     2.8.4    Coefficient of Variation           76
     2.8.5    Multimodal Distributions            76
     2.8.6 Outliers 77
  2.9    Monitoring    77
     2.9.1 Time-Based Patterns              77
     2.9.2    Monitoring Products           79
     2.9.3 Summary-Since-Boot 79
  2.10    Visualizations    79
     2.10.1 Line Chart 80
     2.10.2    Scatter Plots      81
     2.10.3 Heat Maps 82
     2.10.4 Timeline Charts            83
     2.10.5 Surface Plot         84
     2.10.6    Visualization Tools         85
  2.11    Exercises    85
  2.12    References    86

3 Operating Systems         89
  3.1    Terminology   90
  3.2    Background    91
     3.2.1    Kernel   91
     3.2.2    Kernel and User Modes              93
     3.2.3 System Calls 94
xii   Contents


             3.2.4    Interrupts      96
             3.2.5    Clock and Idle 99
             3.2.6    Processes        99
             3.2.7    Stacks       102
             3.2.8    Virtual Memory         104
             3.2.9    Schedulers         105
             3.2.10      File Systems       106
             3.2.11      Caching      108
             3.2.12      Networking        109
             3.2.13      Device Drivers        109
             3.2.14 Multiprocessor 110
             3.2.15      Preemption        110
             3.2.16 Resource Management                 110
             3.2.17      Observability      111
          3.3    Kernels     111
             3.3.1    Unix 112
             3.3.2    BSD       113
             3.3.3    Solaris      114
          3.4    Linux    114
             3.4.1 Linux Kernel Developments 115
             3.4.2 systemd 120
             3.4.3 KPTI (Meltdown) 121
             3.4.4 Extended BPF 121
          3.5    Other Topics      122
             3.5.1    PGO Kernels          122
             3.5.2 Unikernels 123
             3.5.3    Microkernels and Hybrid Kernels          123
             3.5.4    Distributed Operating Systems           123
          3.6    Kernel Comparisons          124
          3.7    Exercises      124
          3.8    References      125
             3.8.1    Additional Reading          127

       4 Observability Tools          129
          4.1    Tool Coverage        130
             4.1.1    Static Performance Tools          130
             4.1.2    Crisis Tools       131
                                                              Contents   xiii



  4.2 Tool Types 133
     4.2.1   Fixed Counters          133
     4.2.2   Profiling    135
     4.2.3   Tracing     136
     4.2.4   Monitoring        137
  4.3 Observability Sources 138
     4.3.1 /proc 140
     4.3.2 /sys 143
     4.3.3 Delay Accounting            145
     4.3.4 netlink 145
     4.3.5   Tracepoints       146
     4.3.6 kprobes 151
     4.3.7 uprobes 153
     4.3.8 USDT        155
     4.3.9   Hardware Counters (PMCs)             156
     4.3.10 Other Observability Sources 159
  4.4 sar 160
     4.4.1 sar(1) Coverage 161
     4.4.2 sar(1) Monitoring          161
     4.4.3 sar(1) Live         165
     4.4.4 sar(1) Documentation 165
  4.5   Tracing Tools     166
  4.6 Observing Observability 167
  4.7 Exercises 168
  4.8 References 168

5 Applications 171
  5.1   Application Basics       172
     5.1.1 Objectives 173
     5.1.2   Optimize the Common Case             174
     5.1.3 Observability 174
     5.1.4 Big O Notation            175
  5.2   Application Performance Techniques              176
     5.2.1   Selecting an I/O Size          176
     5.2.2   Caching      176
     5.2.3   Buffering    177
     5.2.4   Polling     177
     5.2.5 Concurrency and Parallelism 177
xiv   Contents


             5.2.6 Non-Blocking I/O 181
             5.2.7   Processor Binding       181
             5.2.8 Performance Mantras 182
          5.3    Programming Languages           182
             5.3.1 Compiled Languages 183
             5.3.2   Interpreted Languages         184
             5.3.3   Virtual Machines       185
             5.3.4 Garbage Collection 185
          5.4 Methodology 186
             5.4.1   CPU Profiling     187
             5.4.2 Off-CPU Analysis 189
             5.4.3 Syscall Analysis 192
             5.4.4 USE Method 193
             5.4.5 Thread State Analysis 193
             5.4.6 Lock Analysis 198
             5.4.7 Static Performance Tuning 198
             5.4.8 Distributed Tracing 199
          5.5 Observability Tools 199
             5.5.1 perf    200
             5.5.2   profile   203
             5.5.3 offcputime        204
             5.5.4 strace      205
             5.5.5 execsnoop 207
             5.5.6   syscount    208
             5.5.7 bpftrace      209
          5.6 Gotchas 213
             5.6.1 Missing Symbols 214
             5.6.2   Missing Stacks        215
          5.7 Exercises 216
          5.8 References 217

       6 CPUs     219
          6.1    Terminology    220
          6.2    Models   221
             6.2.1   CPU Architecture        221
             6.2.2   CPU Memory Caches 221
             6.2.3   CPU Run Queues          222
                                                         Contents   xv



6.3   Concepts    223
  6.3.1    Clock Rate      223
  6.3.2    Instructions        223
  6.3.3    Instruction Pipeline 224
  6.3.4    Instruction Width         224
  6.3.5    Instruction Size      224
  6.3.6    SMT    225
  6.3.7    IPC, CPI      225
  6.3.8    Utilization    226
  6.3.9 User Time/Kernel Time 226
  6.3.10    Saturation       226
  6.3.11    Preemption         227
  6.3.12 Priority Inversion           227
  6.3.13 Multiprocess, Multithreading              227
  6.3.14    Word Size 229
  6.3.15    Compiler Optimization 229
6.4   Architecture     229
  6.4.1 Hardware          230
  6.4.2 Software         241
6.5 Methodology 244
  6.5.1 Tools Method            245
  6.5.2 USE Method             245
  6.5.3 Workload Characterization                246
  6.5.4    Profiling     247
  6.5.5 Cycle Analysis 251
  6.5.6    Performance Monitoring           251
  6.5.7    Static Performance Tuning             252
  6.5.8    Priority Tuning 252
  6.5.9    Resource Controls          253
  6.5.10 CPU Binding 253
  6.5.11 Micro-Benchmarking                253
6.6 Observability Tools 254
  6.6.1 uptime         255
  6.6.2 vmstat         258
  6.6.3 mpstat         259
  6.6.4 sar 260
  6.6.5 ps 260
xvi   Contents


             6.6.6    top    261
             6.6.7    pidstat     262
             6.6.8    time, ptime       263
             6.6.9    turbostat     264
             6.6.10    showboost         265
             6.6.11    pmcarch      265
             6.6.12 tlbstat 266
             6.6.13 perf 267
             6.6.14 profile 277
             6.6.15 cpudist 278
             6.6.16    runqlat 279
             6.6.17    runqlen 280
             6.6.18 softirqs 281
             6.6.19 hardirqs 282
             6.6.20 bpftrace 282
             6.6.21    Other Tools 285
          6.7    Visualizations    288
             6.7.1    Utilization Heat Map       288
             6.7.2    Subsecond-Offset Heat Map         289
             6.7.3    Flame Graphs        289
             6.7.4    FlameScope 292
          6.8    Experimentation        293
             6.8.1 Ad Hoc 293
             6.8.2 SysBench         294
          6.9    Tuning     294
             6.9.1 Compiler Options 295
             6.9.2    Scheduling Priority and Class     295
             6.9.3 Scheduler Options 295
             6.9.4    Scaling Governors         297
             6.9.5    Power States 297
             6.9.6    CPU Binding        297
             6.9.7    Exclusive CPU Sets        298
             6.9.8    Resource Controls         298
             6.9.9    Security Boot Options       298
             6.9.10 Processor Options (BIOS Tuning) 299
          6.10 Exercises 299
          6.11    References       300
                                                             Contents   xvii



7 Memory 303
  7.1   Terminology      304
  7.2   Concepts    305
    7.2.1 Virtual Memory 305
    7.2.2    Paging      306
    7.2.3    Demand Paging           307
    7.2.4 Overcommit           308
    7.2.5    Process Swapping         308
    7.2.6    File System Cache Usage             309
    7.2.7    Utilization and Saturation 309
    7.2.8    Allocators    309
    7.2.9 Shared Memory 310
    7.2.10    Working Set Size        310
    7.2.11    Word Size        310
  7.3   Architecture     311
    7.3.1    Hardware      311
    7.3.2    Software     315
    7.3.3    Process Virtual Address Space             319
  7.4 Methodology 323
    7.4.1 Tools Method          323
    7.4.2 USE Method           324
    7.4.3    Characterizing Usage          325
    7.4.4 Cycle Analysis 326
    7.4.5    Performance Monitoring          326
    7.4.6    Leak Detection      326
    7.4.7    Static Performance Tuning           327
    7.4.8    Resource Controls         328
    7.4.9 Micro-Benchmarking               328
    7.4.10 Memory Shrinking 328
  7.5 Observability Tools 328
    7.5.1 vmstat         329
    7.5.2 PSI 330
    7.5.3    swapon 331
    7.5.4 sar 331
    7.5.5    slabtop     333
    7.5.6 numastat         334
    7.5.7 ps       335
    7.5.8 top 336
xviii   Contents


               7.5.9 pmap 337
               7.5.10    perf     338
               7.5.11 drsnoop 342
               7.5.12       wss 342
               7.5.13       bpftrace    343
               7.5.14    Other Tools 347
            7.6    Tuning     350
               7.6.1    Tunable Parameters 350
               7.6.2 Multiple Page Sizes 352
               7.6.3 Allocators 353
               7.6.4    NUMA Binding          353
               7.6.5 Resource Controls 353
            7.7    Exercises     354
            7.8    References       355

         8 File Systems 359
            8.1    Terminology         360
            8.2 Models 361
               8.2.1    File System Interfaces 361
               8.2.2 File System Cache 361
               8.2.3    Second-Level Cache           362
            8.3    Concepts      362
               8.3.1    File System Latency          362
               8.3.2    Caching        363
               8.3.3    Random vs. Sequential I/O              363
               8.3.4    Prefetch       364
               8.3.5    Read-Ahead           365
               8.3.6    Write-Back Caching          365
               8.3.7    Synchronous Writes           366
               8.3.8    Raw and Direct I/O          366
               8.3.9    Non-Blocking I/O           366
               8.3.10       Memory-Mapped Files           367
               8.3.11       Metadata      367
               8.3.12       Logical vs. Physical I/O       368
               8.3.13       Operations Are Not Equal           370
               8.3.14       Special File Systems         371
               8.3.15       Access Timestamps            371
               8.3.16 Capacity          371
                                                          Contents   xix



8.4   Architecture    372
  8.4.1 File System I/O Stack 372
  8.4.2 VFS 373
  8.4.3 File System Caches 373
  8.4.4 File System Features            375
  8.4.5 File System Types 377
  8.4.6    Volumes and Pools        382
8.5   Methodology      383
  8.5.1    Disk Analysis     384
  8.5.2    Latency Analysis       384
  8.5.3 Workload Characterization             386
  8.5.4    Performance Monitoring         388
  8.5.5    Static Performance Tuning          389
  8.5.6 Cache Tuning 389
  8.5.7 Workload Separation 389
  8.5.8    Micro-Benchmarking       390
8.6 Observability Tools 391
  8.6.1 mount 392
  8.6.2 free     392
  8.6.3    top   393
  8.6.4 vmstat 393
  8.6.5 sar 393
  8.6.6    slabtop     394
  8.6.7 strace        395
  8.6.8 fatrace 395
  8.6.9    LatencyTOP 396
  8.6.10    opensnoop 397
  8.6.11    filetop    398
  8.6.12    cachestat 399
  8.6.13    ext4dist (xfs, zfs, btrfs, nfs)     399
  8.6.14    ext4slower (xfs, zfs, btrfs, nfs)       401
  8.6.15    bpftrace 402
  8.6.17 Other Tools 409
  8.6.18    Visualizations    410
8.7   Experimentation       411
  8.7.1    Ad Hoc     411
  8.7.2    Micro-Benchmark Tools         412
  8.7.3    Cache Flushing     414
