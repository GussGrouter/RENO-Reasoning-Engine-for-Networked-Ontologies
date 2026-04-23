# Chunk 000002

- Source: raw/code/pdf/a-philosophy-of-software-design.pdf
- Slice: PDF pages 38–42
- From: processed/code/philosophy-ousterhout-deep-modules-p38-42.md

---
actually shrinks its overall interface, since it eliminates the interface for freeing
objects. The implementation of a garbage collector is quite complex, but that
complexity is hidden from programmers.
    Deep modules such as Unix I/O and garbage collectors provide powerful
abstractions because they are easy to use, yet they hide significant
implementation complexity.
