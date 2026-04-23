# Network Algorithmics — 6.4 Scalable I/O Notification (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 186
- Slice: from `6.4 Scalable I/O Notification` up to next detected section heading

---

6.4 Scalable I/O Notification
To motivate the problem, Section 6.4.1 presents a mysterious performance problem found in the lit-
erature. Section 6.4.2 then describes the usage and implementation of the select() call in UNIX.
Section 6.4.3 describes an analysis of the overheads and applies the implementation principles to sug-
gest ideas for improvement. Based on the analysis, Section 6.4.4 describes an improvement, assuming
that the API cannot change. Finally, Section 6.4.5 proposes an even better solution that involves a more
dramatic change to the API that is reflected in the Linux epoll() system call that is commonly used.
