# Systems Performance — Ch.9 §9.8.4 Random read example

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2313–2338** (printed ~492).

## Summary

- **Concurrency sweep:** **1→5** parallel random **8KB** readers on a device; **`iostat`** shows **rising `aqu-sz`** and **`r_await`** as load steps—illustrates **queue growth under overload**.

## Links

- Connects micro-experiment design to **USE** / **queueing** intuition without needing formal models.
