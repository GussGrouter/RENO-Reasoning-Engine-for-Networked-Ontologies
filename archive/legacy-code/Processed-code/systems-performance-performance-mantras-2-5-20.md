# Systems Performance — performance mantras (2.5.20) (performance-mantras-2-5-20) (PDF pages 98–106)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-cache-microbench-mantras-scout-p98-106.md

---

2.5.20       Performance Mantras
This is a tuning methodology that shows how best to improve performance, listing actionable
items in order from most to least effective. It is:

   1. Don’t do it.

  2. Do it, but don’t do it again.

  3. Do it less.

  4. Do it later.

  5. Do it when they’re not looking.
  6. Do it concurrently.

   7. Do it more cheaply.

Here are some examples for each of these:

   1. Don’t do it: Eliminate unnecessary work.

  2. Do it, but don’t do it again: Caching.

  3. Do it less: Tune refreshes, polling, or updates to be less frequent.

  4. Do it later: Write-back caching.

  5. Do it when they’re not looking: Schedule work to run during off-peak hours.

  6. Do it concurrently: Switch from single-threaded to multi-threaded.

   7. Do it more cheaply: Buy faster hardware.

This is one of my favorite methodologies, which I learned from Scott Emmons at Netflix. He
attributes it to Craig Hanson and Pat Crain (though I’ve yet to find a published reference).
62   Chapter 2 Methodologies
