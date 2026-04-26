# Systems Performance — Ch.9 §9.4 Architecture — HDD basics + throughput bound

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **695–782** (PDF ~435–436).

## Summary

- **Architecture-first:** capacity planning and **later incident triage** should consider **wrong topology / geometry** vs only “current load.”
- **HDD:** mechanical **seek + rotation** dominate **random** latency; **sequential** avoids head travel between requests.
- **Mitigations:** **caching**, **FS placement / COW effects**, **workload isolation** across spindles/systems, **elevator** class scheduling on device, **higher RPM**, **partitioning/short-stroking** strategies.
- **Theoretical max throughput:**  
  `max throughput ≈ max sectors/track × sector size × (rpm/60)` — **legacy** when firmware exposed real geometry; **modern drives virtualize** geometry—OS sees **synthetic** sector/track attributes (**measurement-validity**: **scope/semantics** of published geometry).

## Notes

- Footnote on **Netflix OCA** random I/O motivating flash—**workload shape** drives media choice.
