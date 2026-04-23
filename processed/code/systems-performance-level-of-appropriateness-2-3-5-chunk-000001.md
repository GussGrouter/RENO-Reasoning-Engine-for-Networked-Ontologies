# systems-performance-level-of-appropriateness-2-3-5 (chunk 000001)

# Systems Performance — 2.3.5 Level of Appropriateness (PDF pages 66–70)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-concepts-2-3-3-to-2-3-6-p64-71.md
- Slice: 2.3.5 Level of Appropriateness

---

2.3.5 Level of Appropriateness
     Different organizations and environments have different requirements for performance. You
     may have joined an organization where it is the norm to analyze much deeper than you’ve seen
     before, or even knew was possible. Or you may find that, in your new workplace, what you
     consider basic analysis is considered advanced and has never before been performed (good news:
     low-hanging fruit!).

     This doesn’t necessarily mean that some organizations are doing it right and some wrong. It
     depends on the return on investment (ROI) for performance expertise. Organizations with
     large data centers or large cloud environments may employ a team of performance engineers
     who analyze everything, including kernel internals and CPU performance counters, and make
     frequent use of a variety of tracing tools. They may also formally model performance and
     develop accurate predictions for future growth. For environments spending millions per year
     on computing, it can be easy to justify hiring such a performance team, as the wins they find
     are the ROI. Small startups with modest computing spend may only perform superficial checks,
     trusting third-party monitoring solutions to check their performance and provide alerts.

     However, as introduced in Chapter 1, systems performance is not just about cost: it is also about
     the end-user experience. A startup may find it necessary to invest in performance engineering
     to improve website or application latency. The ROI here is not necessarily a reduction in cost, but
     happier customers instead of ex-customers.

     The most extreme environments include stock exchanges and high-frequency traders, where
     performance and latency are critical and can justify intense effort and expense. As an example
     of this, a transatlantic cable between the New York and London exchanges was planned with a
     cost of $300 million, to reduce transmission latency by 6 ms [Williams 11].


     2
      Examples of environments that change rapidly include the Netflix cloud and Shopify, which push multiple changes
     per day.
                                                                                   2.3   Concepts     29


When doing performance analysis, the level of appropriateness also comes in to play in deciding
when to stop analysis.
