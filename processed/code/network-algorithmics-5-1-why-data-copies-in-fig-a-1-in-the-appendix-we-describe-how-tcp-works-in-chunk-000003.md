# network-algorithmics-5-1-why-data-copies-in-fig-a-1-in-the-appendix-we-describe-how-tcp-works-in (chunk 000003)

5.2 Reducing copying via local restructuring              115

In summary redundant copies hurt performance in two fundamental and orthogonal ways. First,
by using more bus and memory bandwidth than strictly necessary, the Web server runs slower than
bus speeds, even when serving documents that are in memory. Second, by using more memory than it
should, the Web server will have to read an unduly large fraction of files from disk instead of from the
file cache.
    Note also that we have only described the scenario in which static content is served. In reality the
SPECweb benchmarks assume that 30% of the requests are for dynamic content. Dynamic content
is often served by a separate CGI process (other than the server application) that communicates this
content to the server via some interprocess communication mechanism, such as a UNIX pipe, which
often involves another copy.
    Ideally, all these pesky extra bus traversals should be removed. Clearly, Copy 1 is not required if
the data is in cache and so we can ignore it. If it’s not in cache, the server runs at disk speed, which
is too slow anyway (though the use of fast non-volatile memory changes this equation). Copy 2 seems
unnecessary. Why can’t the data be sent directly from the file cache memory location to the network?
Similarly, Copy 3 seems unnecessary. Copy 4 is unavoidable.
