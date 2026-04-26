# Network Algorithmics — 18.4.2 New connecting disciplines (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 553
- Slice: from `18.4.2 New connecting disciplines` up to next detected section heading

---

18.4.2 New connecting disciplines
Earlier we said that a key aspect of network algorithmics is its interdisciplinary nature. Solutions
require a knowledge of operating systems, computer architecture, hardware design, networking, and
algorithms. We believe the following disciplines will also impinge on network algorithmics very soon.
• Optics: Optics has been abstracted away as a link layer technology in this book. Currently, optics
  provides a way to add extra channels to existing fiber using dense wavelength-division multiplexing.
  However, optical research has made amazing strides. There are undoubtedly exciting possibilities to
  rethink router design using some combination of electronics and optics.2
• Network processor architecture: While this field is still in its infancy as compared to computer archi-
  tecture, there are surely more imaginative approaches than current approaches that assign packets to


2 Electronics still appears to be required today because of the lack of optical buffers and the difficulty of optical header process-
ing.

                                        18.4 Network algorithmics: back to the future             527



  one of several processors. One such approach, described many years ago in Sherwood et al. (2003),
  uses a wide word state machine as a fundamental building block. A more modern approach that uses
  a pipeline of stages is embodied in the Reconfigurable Match Table architecture (Bosshart et al.,
  2013) as embodied for instance in Intel’s Tofino-3 chip (Intel Corporation, 2022).
• Learning theory: The fields of security and measurement are crying out for techniques to pick out
  interesting patterns from massive traffic data sets. Learning theory and data mining have been used
  for these purposes in other fields. Rather than simply reusing, say, standard clustering algorithms
  or standard techniques such as hidden Markov models, the real breakthroughs may belong to those
  who can find variations of these techniques that can be implemented at high speeds with some loss
  of accuracy. Similarly, online analytical processing (OLAP) tools may be useful for networking,
  with twists to fit the networking milieu. An example of a tool that has an OLAP flavor in a unique
  network setting can be found in Estan et al. (2003). Machine learning is increasingly intersecting
  with network algorithmics. A modern paper that uses machine learning ideas for packet classification
  is (Liang et al., 2019).
• Databases: The field of databases has a great deal to teach networking in terms of systematic tech-
  niques for querying for information. Recently, an even more relevant trend has been the subarea of
  continuous queries. Techniques developed in databases can be of great utility to algorithmics. The
  second edition of this book has a new section on streaming algorithms for networks in Chapter 16.
  Streaming algorithms originated in the database and theory communities. In Section 16.16, we have
  shown how the networking problem of counting the number of distinct flows is intricately connected
  to association rule mining, a classical problem in databases and data mining.
• Statistics: The field of statistics will be of even more importance in dealing with large data sets.
  Already, NetFlow and other tools have to resort to sampling. What inferences can safely be made
  from sampled data? As we have seen in Chapter 16, statistical methods are already used by ISPs to
  solve the traffic matrix problem from limited SNMP data.
