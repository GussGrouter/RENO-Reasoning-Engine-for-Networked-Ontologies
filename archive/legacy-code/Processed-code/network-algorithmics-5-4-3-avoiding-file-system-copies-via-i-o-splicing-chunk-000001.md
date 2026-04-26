# network-algorithmics-5-4-3-avoiding-file-system-copies-via-i-o-splicing (chunk 000001)

# Network Algorithmics — 5.4.3 Avoiding file system copies via I/O splicing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 161
- Slice: from `5.4.3 Avoiding file system copies via I/O splicing` up to next detected section heading

---

5.4.3 Avoiding file system copies via I/O splicing
In the commercial world Web servers are measured by commercial tests such as the SPECweb tests
(SPEC consortium, 1999) for Web servers and the Web polygraph tests (Web Polygraph Associa-
tion, 2001) for Web proxies. In the proxy space there is an annual cache-off, in which all devices
are measured together to calculate the highest cache hit rate, normalized to the price of the device. The
SPECweb benchmarks use a different system, in which manufacturers submit their own experimental
results to the benchmark system, though these results are audited. In the Web polygraph tests at the
time of writing, a Web server technology based on I/O-Lite ideas was among the leaders.
    However, in the SPECweb benchmarks, a number of other Web servers also show impressive per-
formance. Part of the reason for this is just faster (and more expensive) hardware. However, there are
two simple ideas that can avoid the need for complete model shifts as is the case in IO-Lite.
    The first idea is to push the Web server application completely into the kernel. Thus in Fig. 5.1 all
copies can be eliminated because the application and the kernel are part of the same entity. The major
problem with this approach is that such in-kernel Web servers have to deal with the idiosyncrasies
of operating system implementation changes. For example, for a popular high-performance server that
runs over Linux, every internal change to Linux can invalidate assumptions made by the server software
and cause a crash. Note that a conventional user-space server does not have this problem because all
changes to the UNIX implementation still preserve the API.
    The second idea keeps the server application in user space but relies on a simple idea called I/O
splicing to eliminate all the copying in Fig. 5.1. I/O splicing, shown in Fig. 5.10, was first introduced in
Fall and Pasquale (1993). The idea is to introduce a new system call that combines the old call to read a
file with the old call (P6, efficient specialized routines) to send a message to the network. By allowing
the kernel to splice together these two hitherto-separate system calls, we can avoid all redundant copies.
Many systems have system calls such as sendfile(), which are now used by several commercial vendors.
    Despite the success of this mechanism, mechanisms based on sendfile do not generalize well to
communication with say CGI processes.. Thus there is still a need for reducing copy overhead for data
that is computed on the fly and not stored in a file as we saw earlier (A reworked TCP zero-copy receive
API, 2018).
