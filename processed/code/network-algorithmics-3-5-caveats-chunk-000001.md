# network-algorithmics-3-5-caveats (chunk 000001)

# Network Algorithmics — caveats (3.5) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 90 -l 105 -layout
- Slice: from `3.5 Caveats` up to (excluding) `3.6 Summary`

---

3.5 Caveats            67

FIGURE 3.9
Retrieval of a Web page with images typically requires one request to get the page that specifies the needed images
and more requests to retrieve each specified image. Why not have the Web server download the images directly?

implementation principles (e.g., “use hints” and “optimize the expected case”). This book, by contrast,
assumes that much of the network design is already given, and so we focus on principles for efficient
protocol implementation. This book also adds several principles for efficient implementation not found
in Keshav (1991) or Lampson (1989).
    On the other hand, Bentley’s book on “efficient program design” (Bentley, 1982) is more about
optimizing small code segments than the large systems that are our focus; thus many of Bentley’s
principles (e.g., fuse loops, unroll loops, reorder tests) are meant to speed up critical loops rather than
speed up systems as a whole.

3.5 Caveats
                                  Performance problems cannot be solved only through the use of Zen meditation.
                                                —Paraphrased from Jeff Mogul, a computer scientist at HP Labs

The best of principles must be balanced with wisdom to understand the important metrics, with profiling
to determine bottlenecks, and with experimental measurements to confirm that the changes are really
improvements. We start with two case studies to illustrate the need for caution.

Case study 1: Reducing page download times
      Fig. 3.9 shows that in order for a Web client to retrieve a Web page containing images, it must
  typically send a GET request for the page. If the page specifies inline images, then the client must
  send separate requests to retrieve the images before it can display the page. A natural application
  of principle P1 is to ask why separate requests are needed. Why can’t the Web server automatically
  download the images when the page is requested instead of waiting for a separate request? This
  should reduce page download latency by at least half a round trip delay.

---

## PDF page 95

68     Chapter 3 Fifteen implementation principles

To test our hypothesis, we modified the server software to do so and measured the resulting
 performance. To our surprise, we found only minimal latency improvement.
    Using a network analyzer based on tcpdump, we found two reasons why this seeming im-
 provement was a bad idea.
 • Interaction with TCP: Web transfer is orchestrated by TCP as described in Chapter 2. To
   avoid network congestion, TCP increases its rate slowly, starting with one packet per round-
   trip, then to two packets per round trip delay, increasing its rate when it gets acks. Since TCP
   had to wait for acks anyway to increase its rate, waiting for additional requests for images did
   not add latency.
 • Interaction with Client Caching: Many clients already cache common images, such as .gif
   files. It is a waste of bandwidth to have the Web server unilaterally download images that
   the client already has in its cache. Note that having the client request the images avoids this
   problem because the client will only request images it does not already have.
 A useful lesson from this case study is the difficulty of improving part of a system (e.g., image
 downloading) because of interactions with other parts of the system (e.g., TCP congestion control).
