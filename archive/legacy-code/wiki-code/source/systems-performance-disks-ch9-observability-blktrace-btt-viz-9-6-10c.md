# Systems Performance — Ch.9 §9.6.10 blktrace (btt + visualization)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.10** (part **c** of **c**—**btt**, visualization)

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-blktrace-btt-viz-9-6-10c.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **`btt` stage splits** map **where time disappears**—**queue vs device** vs **merge window**—before blaming vendors ([[measurement-validity]] **scope/semantics**, [[latency-analysis]], [[metric-visualization]] for offline viewers).

## Application hook

When **`await` is painful** but **`%util` is modest**: **`btt`** can show whether you are paying in **queue stages** vs **media**, guiding **scheduler/array** tuning vs **spindles/flash**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[latency-analysis]], [[metric-visualization]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[latency-analysis]], [[metric-visualization]], [[systems-performance]]
