      4. Develop the following procedures for your operating system:
         ■   A USE method checklist for disk resources (disks and controllers). Include how to fetch
             each metric (e.g., which command to execute) and how to interpret the result. Try to use
             existing OS observability tools before installing or using additional software products.
         ■   A workload characterization checklist for disk resources. Include how to fetch each metric,
             and try to use existing OS observability tools first.

      5. Describe disk behavior visible in this Linux iostat(1) output alone:

         $ iostat -x 1
         [...]
         avg-cpu:    %user      %nice %system %iowait     %steal     %idle
                       3.23      0.00     45.16   31.18     0.00     20.43


         Device:            rrqm/s   wrqm/s         r/s      w/s      rkB/s     wkB/s avgrq-sz
         avgqu-sz      await r_await w_await      svctm   %util
         vda                   39.78 13156.99 800.00 151.61         3466.67 41200.00     93.88
         11.99      7.49       0.57   44.01   0.49 46.56
         vdb                    0.00       0.00      0.00    0.00      0.00      0.00     0.00
         0.00      0.00       0.00      0.00    0.00    0.00

      6. (optional, advanced) Develop a tool to trace all disk commands except for reads and writes.
         This may require tracing at the SCSI level.


