# network-algorithmics-14-7-1-the-parochial-parcel-service (chunk 000004)

the packet of size 750 and the packet of size 20. Assume that no more packets arrive to F 1’s queue than
are shown in Fig. 14.12. Thus since the F 1 queue is empty, the algorithm skips to F 2.
    Curiously, when skipping to F 2, the algorithm does not leave behind the deficit of 800 − 750 −
20 = 30 in F 1’s queue. Instead, it zeroes out F 1’s deficit counter. Thus the deficit counter is a somewhat
curious bank account that is zeroed unless the account holder can prove a “need” in terms of a nonempty
queue. Perhaps this is analogous to a welfare account.
