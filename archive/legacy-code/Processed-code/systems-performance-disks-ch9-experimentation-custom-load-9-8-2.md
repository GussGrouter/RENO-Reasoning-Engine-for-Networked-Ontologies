# Systems Performance — Ch.9 §9.8.2 Custom load generators

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2286–2293** (printed ~491–492).

## Summary

- **Roll-your-own** generators can express **exact offsets/sizes/patterns** then validate with **`iostat`**.
- **Linux:** open block devices with **`O_DIRECT`** to reduce **unintended buffering**; higher-level languages need **discipline** to avoid **library buffers** masking the disk.

## Measurement-validity

- **Perturbation / representation:** user-space buffering can make results **about RAM**, not **spindles/flash**—align I/O path with the question.
