# Network Algorithmics — 14.9.1 A simple example It helps to explain the GPS scheduler and the related concepts using the following simple example. We (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 428
- Slice: from `14.9.1 A simple example It helps to explain the GPS scheduler and the related concepts using the following simple example. We` up to next detected section heading

---

14.9.1 A simple example
It helps to explain the GPS scheduler and the related concepts using the following simple example. We
consider a packet scheduling instance in which there are three flows, namely F 1, F 2, and F 3, with
equal weight 1. Assume they share a link with service rate of 1-bit per second. The j th packet of flow i
is denoted pi,j . Its arrival time and length (in bits) are denoted as ai,j and li,j , respectively. Let a1,1 =
a2,1 = a3,1 = 0, a1,2 = a2,2 = a3,2 = 3, and a3,3 = 4. Let l1,1 = 7, l1,2 = 1, l2,1 = 5, l2,2 = 4, l3,1 = 3,
l3,2 = 1, and l3,3 = 6.
    The service schedule of this instance, represented as a GPS graph, is shown in Fig. 14.16. Each
rectangle corresponds to a packet, and each row (of rectangles) corresponds to a flow. The height of
each row corresponds to the weight of the corresponding flow. All rows have the same height since all
flows have weight 1. The length of each packet is equal to the area and equivalently the length in this
case (since all rectangles have the same height) of the corresponding rectangle. For example, as shown
in Fig. 14.16, row 3 contains three rectangles of lengths 3, 1, and 6, respectively. They correspond to
the three packets p3,1 , p3,2 , and p3,3 in F 3.

402       Chapter 14 Scheduling packets




FIGURE 14.16
GPS graph of a simple packet arrival instance.


    Under GPS all three flows start receiving service, each at rate 1/3 bits per second, at time 0, since
the first packets of all three flows arrive at the same time 0. The x-axis of the GPS graph corresponds
to the virtual time, defined as the number of bits of service rendered by GPS to backlogged flows. For
example, in Fig. 14.16, at virtual time 7 (bits), 7 bits of service have been rendered to all three flows.
Clearly, the real time corresponding to virtual time 7 (bits) is 21 (seconds), since a total of 21 (bits) of
service is rendered to the three flows during the virtual time interval [0, 7] (bits) at the assumed link
rate of r = 1 bit per second.
