# Systems Performance — Ch.10 §10.4.3 Software (TCP buffering)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- TCP throughput uses send/receive socket buffers.
- Larger buffers improve throughput but consume more memory per connection; asymmetric sizing can match send-heavy vs receive-heavy roles.
- Linux can auto-tune buffer sizes within configured min/default/max.

