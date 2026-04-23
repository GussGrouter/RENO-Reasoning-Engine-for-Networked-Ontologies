# network-algorithmics-14-9-4-tracking-the-gps-clock (chunk 000003)

14.10 Weighted fair queueing              407

complexity in practice remains O(n) per packet, just as in the case of precomputing all GPS real finish
times.
    This inconsistency between theory and practice was first elaborated in details in Zhao and Xu
(2004). Shortly afterward, this inconsistency was resolved by the aforementioned GPS clock track-
ing work (Valente, 2004), in which a data structure and algorithm was proposed that strikes a nice
tradeoff between theory and the practice. With this new solution, each cleanup operation has a higher
time complexity of O(log n) (than O(1)), but the worst-case time complexity of computing V (·) in
the event of a “rude awakening” is also capped at O(log n). As a result, this new solution allows the
worst-case time complexity of both WFQ and WF2 Q algorithms to be capped at O(log n) per packet.
