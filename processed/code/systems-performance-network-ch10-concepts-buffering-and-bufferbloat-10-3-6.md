# Systems Performance — Ch.10 §10.3.6 Buffering (throughput vs queueing delay)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1207–1228** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Buffering at endpoints sustains throughput across RTT by sending before blocking on ACKs (TCP windowing; socket/app buffers).
- Buffering inside switches/routers can increase their throughput, but large buffers can cause **bufferbloat**: long queues → higher latency.
- Large intermediate queues can trigger congestion avoidance and throttle performance.
- End-to-end arguments suggest buffering is often best placed at endpoints, not intermediate nodes.

