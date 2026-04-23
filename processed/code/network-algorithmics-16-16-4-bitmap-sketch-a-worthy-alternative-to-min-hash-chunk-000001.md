# network-algorithmics-16-16-4-bitmap-sketch-a-worthy-alternative-to-min-hash (chunk 000001)

# Network Algorithmics — 16.16.4 Bitmap sketch: a worthy alternative to min-hash (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 507
- Slice: from `16.16.4 Bitmap sketch: a worthy alternative to min-hash` up to next detected section heading

---

16.16.4 Bitmap sketch: a worthy alternative to min-hash
Another technique for counting F0 is the bitmap sketch, invented in Whang et al. (1990) for database
applications. It requires more space than the min-hash sketch but has a much lower update time for

16.16 Counting the number of distinct flows                 481

Table 16.3 The Walmart customer-transaction table after
                      transformation.
                      Transaction ID    Milk     Cereal    Banana    Apple       ···
                           α1            α1       α1                  α1         ···
                           α2                                α2       α2         ···
                           α3            α3        α3        α3       α3         ···
                           α4            α4                  α4       α4         ···
                            ..            ..        ..        ..       ..        .. .. ..
                             .             .         .         .        .         ...
