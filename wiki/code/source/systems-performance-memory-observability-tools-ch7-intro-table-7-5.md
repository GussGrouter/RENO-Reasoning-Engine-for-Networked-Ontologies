# Systems Performance — Memory observability tools: intro (§7.5) (PDF scout extracts 320–380 + 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5** — **Observability Tools** (Table 7.4 **omitted** in processed extract; see book for the tool index)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt` (and `…-p381-400.txt` for tail of §7.5)
- Converted slice: `processed/code/systems-performance-memory-observability-tools-ch7-intro-table-7-5.md`
- Chunks: `processed/code/systems-performance-memory-observability-tools-ch7-intro-table-7-5-chunk-000001.md`

## Extracted ideas (with classification)

- (heuristic) **Tool survey follows §7.4 method order** (system → pressure → per-process → events): treat the section as a **ladder of resolution**, not a menu to run at random ([[drill-down-analysis]], [[use-method]]).
- (abstraction) **Documented tool set still has coverage gaps**—name the **known unknowns** you are *not* seeing on a given host image ([[known-unknowns-framework]]).
- (structure) **Table 7.4 is an index, not a model**; **validity** comes from matching each tool’s **semantics** to the question (free+cache, RSS overcount, swap I/O) ([[measurement-validity]]).

## Application validation

- **New memory alert on a minimal image:** before installing BCC, list which of **PSI, vmstat, /proc/pressure, swap/sar** you can already read so the **first** triage pass is not a **false negative** from missing columns.

## Decision clarity

- **Decision:** choose **filling visibility holes in the standard stack (PSI, vmstat, process RSS, optional tracers)** over **adopting a new one-off tool** when **the team already has a working path** from monitoring to **per-process maps** and the gap is **integration**, not technique.

## Concepts reused / refined / created

- Reused (heuristic): [[use-method]], [[drill-down-analysis]]
- Reused (abstraction): [[known-unknowns-framework]], [[measurement-validity]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[use-method]], [[drill-down-analysis]], [[known-unknowns-framework]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-memory-methodology-ch7-intro-and-order-7-4]], [[systems-performance-memory-observability-vmstat-7-5-1]]
