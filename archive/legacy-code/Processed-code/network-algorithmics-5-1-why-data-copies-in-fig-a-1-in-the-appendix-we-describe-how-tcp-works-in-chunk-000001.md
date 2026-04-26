# network-algorithmics-5-1-why-data-copies-in-fig-a-1-in-the-appendix-we-describe-how-tcp-works-in (chunk 000001)

# Network Algorithmics — 5.1 Why data copies In Fig. A.1 in the Appendix we describe how TCP works in the context of a Web server. Fig. A.1 only (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 140
- Slice: from `5.1 Why data copies In Fig. A.1 in the Appendix we describe how TCP works in the context of a Web server. Fig. A.1 only` up to next detected section heading

---

5.1 Why data copies
In Fig. A.1 in the Appendix we describe how TCP works in the context of a Web server. Fig. A.1 only
shows the sending of the GET request for a file, followed by the file data itself in two TCP segments.
What Fig. A.1 does not show is how the Web server processes the GET request. In this chapter we
ignore the control transfer required to transfer the request to some application server process. Instead,
Fig. 5.1 shows the sequence of data transfers involved in reading file data from the disk (in the worst
case) to the sending of the corresponding segments via the network adaptor.
    The main hardware players in Fig. 5.1 are the CPU, the memory bus, the I/O bus, the disk, and the
network adaptor. The main software players are the Web server application and the kernel. There are
two main kernel subsystems involved, the file system and the networking system. For simplicity, the
picture shows only one CPU in the server (many servers are multiprocessors and particularly multicore
machines) and focuses only on requests for static content (many requests are for dynamic content that
is served by a Common Gateway Interface (CGI) process).1
    Intuitively, the story is simple. The file is read from disk into the application buffer via, say, a read()
system call. The combination of the HTTP response and the application buffer is then sent to the

1 The picture makes it appear that the code for the file system and the TCP/IP code is on the processor. In reality the code is also
stored in memory and is fetched by the processor. However, the portion of the code that fits into the processor instruction cache
indeed can be considered to be in the processor.

114      Chapter 5 Copying data
