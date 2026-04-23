# Network Algorithmics — 3.3 Fifteen implementation principles—categorization and description (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 84
- Slice: from `3.3 Fifteen implementation principles—categorization and description` up to next detected section heading

---

3.3 Fifteen implementation principles—categorization and description
The two earlier examples and the warm-up exercise in Chapter 1 motivate the following 15 principles,
which are used in the rest of the book. They are summarized inside the front cover. To add more
structure, they are categorized as follows:
• Systems Principles: Principles 1–5 take advantage of the fact that a system is constructed from
  subsystems. By taking a systemwide rather than a black-box approach, one can often improve per-
  formance.
• Improving Efficiency While Retaining Modularity: Principles 6–10 suggest methods for improv-
  ing performance while allowing complex systems to be built modularly.
• Speeding It Up: Principles 11–15 suggest techniques for speeding up a key routine considered by
  itself.

58       Chapter 3 Fifteen implementation principles



    Amazingly, many of these principles have been used for years by Chef Charlie at his Greasy Spoon
restaurant. This chapter sometimes uses illustrations drawn from Chef Charlie’s experience, in addition
to computer systems examples. One networking example is also described for each principle, though
details are deferred to later chapters.
