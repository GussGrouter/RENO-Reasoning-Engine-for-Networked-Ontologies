# network-algorithmics-13-8-input-queued-switching-as-a-bipartite-matching-problem (chunk 000002)

1973), yet using maximum matchings as crossbar schedules generally cannot provably guarantee 100%
throughput under all traffic patterns. The family of maximal matchings has long been recognized as a
special cost-effective family for crossbar scheduling. On the one hand, efficient distributed algorithms
exist for computing maximal matchings. We will describe two such algorithms, namely parallel iter-
ative matching (PIM) (Anderson et al., 1993) and iSLIP, in the next two sections. On the other hand,
using maximal matchings as crossbar schedules can provably result in at least 50% throughput (Dai and
Prabhakar, 2000) under all traffic patterns, and maximal matching algorithms such as PIM and iSLIP
typically can deliver much better empirical throughput performances. All said, it is well known that
neither PIM nor iSLIP can attain 100% throughput except under certain benign traffic patterns such as
uniform traffic (McKeown, 1999).
