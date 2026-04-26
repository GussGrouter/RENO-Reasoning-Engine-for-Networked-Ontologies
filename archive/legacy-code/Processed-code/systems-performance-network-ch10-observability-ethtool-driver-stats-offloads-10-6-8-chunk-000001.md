# Systems Performance — Ch.10 §10.6.8 ethtool (driver stats + offloads)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3122–3185** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `ethtool -S` pulls **NIC/driver-specific counters** from the kernel ethtool framework (names vary by driver).
- `ethtool -i` summarizes **driver identity/version**, supporting static-configuration audits alongside vendor release notes.
- `ethtool -k` lists **hardware/protocol offload toggles** (checksumming, GSO/GRO/LRO, VLAN offload, hashing, segment offload, etc.); `-K` changes writable knobs.
- Example shows a cloud NIC where **TCP segmentation offload is off** (`[fixed]` on several TCP offload lines)—meaning CPU may pay more segmentation work unless changed elsewhere—pair with throughput/CPU evidence before flipping knobs.
