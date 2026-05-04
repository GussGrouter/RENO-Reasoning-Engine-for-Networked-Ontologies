# network-algorithmics-5-3-1-avoiding-copying-in-a-cluster (chunk 000002)

Finally, it is somewhat cavalier to allow any packet carrying a buffer ID from the network to be
written directly into memory. This could be a security hole. To mitigate against this, the buffer IDs
contain a random string that is hard to guess. More importantly, VAX Clusters are used only between
trusted hosts in a cluster. It is more difficult to imagine scaling this approach to Internet data transfers.
