# network-algorithmics-16-16-1-the-min-hash-algorithm (chunk 000002)

The manner in which this estimator is obtained, by replacing the first moment of V with a realization
of V is called the method of moments in statistics (Casella and Berger, 2001).
    Clearly, a single estimator N̂ is very noisy and can lead to large estimation errors. To improve on
that, we often use a number of, say 25, such estimators that are statistically independent. This can be
achieved using 25 different and statistically independent hash functions H1 , H2 , · · · , H25 as follows.
Instead of a single min-hash variable V we compute an array V [1..25] of 25 min-hash variables. This
array is called a min-hash sketch. Each variable V [i] is generated using the hash function Hi . Suppose
their corresponding values are v[1..25] after processing a data stream. Then what would be a good
estimator derived from these 25 values?
    A good guess is simply to use the average (i.e., the sample mean) of these 25 values in the place
of v in Formula (16.1). However, the resulting estimator is not robust since an outlier among them can
significantly distort the average. In statistics, the median of means or the mean of medians is often
used instead to both achieve low variance and guard against outliers. For example, a median of means
estimator in this case can be obtained by organizing these 25 values into a 5 × 5 matrix, calculating
the average of each row, and outputting the median of the 5 averages. In the following, we denote such
an estimator as MM(v[1..25]) so that we do not have to spell out whether MM stands for median of
means or mean of medians. With this notation, an MM estimator is
                                                  1
                                       N̂ =                − 1.                                    (16.2)
                                              MM(v[1..25])
Such an MM-based estimator is frequently used in synthesizing multiple independent observations,
such as in Alon et al. (1999b).
    Compared to maintaining a hash table, which requires O(N ) memory, this data-sketching algorithm
requires only 25 or so words of memory, or O(1) memory. It does sacrifice some estimation accuracy,
but this can be tolerated in many applications. Since its memory requirement is extremely low, these
memory words can be stored in SRAM or even registers to allow for accesses at line rates. Since each
V [i] is independent of others, they can be accessed and updated in parallel, at an extra cost.


