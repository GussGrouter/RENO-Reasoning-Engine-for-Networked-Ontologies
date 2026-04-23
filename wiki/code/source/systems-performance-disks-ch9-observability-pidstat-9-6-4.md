# Systems Performance — Ch.9 §9.6.4 pidstat (disk)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.4**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-pidstat-9-6-4.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Rates vs delay:** **`kB_*`** shows **applied load**; **`iodelay`** shows **blocked time**—together separate **who is pushing** vs **who is hurt** ([[resource-analysis-vs-workload-analysis]]).
- **Flush attribution:** writer process may show **little delay** until **`kworker` flush** pays the bill—avoid **single-column blame** ([[measurement-validity]] **representation**).

## Application hook

If **`iostat` says disks busy** but **no obvious tenant**: **`pidstat -d`** is the bridge to **ownership**.

## Concepts reused / refined / created

- Reused: [[resource-analysis-vs-workload-analysis]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[resource-analysis-vs-workload-analysis]], [[measurement-validity]], [[systems-performance]]
