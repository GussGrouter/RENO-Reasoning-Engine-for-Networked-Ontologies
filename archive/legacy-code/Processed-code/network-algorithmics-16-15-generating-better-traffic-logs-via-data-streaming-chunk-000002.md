# network-algorithmics-16-15-generating-better-traffic-logs-via-data-streaming (chunk 000002)

when processing OC-768 traffic), the streaming algorithm does not have enough processing time to “put
the data into the exact place.” Second, the streaming algorithm does not have enough space to store all
the relevant data. Due to the loss, the streaming result is typically far away from the information we
would like to estimate. Bayesian statistics is therefore used to recover information from the streaming
result as much as possible.
    Data-streaming and sketching algorithms were first proposed as memory-efficient approximate
query processing solutions in databases (Alon et al., 1999b). In general, a success is declared if the
solution has a small memory footprint that is sublinear with respect to the number of data points in the
database. However, data-streaming algorithms for network applications have to possess an additional
property: the time complexity of updating the corresponding sketch has to be very low since every
packet arrival triggers one or more such updates and the network link rate can be extremely high.
