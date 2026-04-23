# Systems Performance — Ch.9 §9.4.3 — Storage arrays + NAS

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1276–1291** (PDF ~446).

## Summary

- **Arrays:** large **controller + cache** pools; **BBU loss → write-through** can **suddenly** expose **RMW/backdisk latency**.
- **Attachment link:** **HBA + cable/fabric** caps **IOPS/BW** independent of **array spindle count**.
- **Dual-path:** availability + sometimes **aggregate path** considerations.
- **NAS (NFS/SMB/iSCSI):** **remote system**—client sees **protocol + network + array** stack; **network congestion** and **multi-hop RTT** enter the **latency budget** (**cross-component-interactions**).

## Application validation

Latency SLO breach on “**disk-bound**” app using **NAS:** split **client FS stats** vs **network** vs **array-side** metrics—fixing **local disk** knobs alone **mis-scopes** the problem.
