# Network Algorithmics — 18.1.1 Endnode algorithmics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 541
- Slice: from `18.1.1 Endnode algorithmics` up to next detected section heading

---

18.1.1 Endnode algorithmics
Chapters 5–9 of this book concentrate on endnode algorithmics, especially for servers. Many of the
problems tackled under endnode algorithmics involve getting around complexities due to software and
structure, in other words, complexities of our own making as opposed to necessarily fundamental com-
plexities. These complexities arise because of the following characteristics of endnodes.
• Computation Versus Communication: Endnodes are about general-purpose computing and must
  handle possible unknown and varied computational demands, from database queries to weather pre-
  diction. By contrast, routers are devoted to communication.
• Vertical Versus Horizontal Integration: Endnodes are typically horizontally integrated, with one
  institution building boards, another writing kernel software, and another writing applications. In
  particular, kernels have to be designed to tolerate unknown and potentially buggy applications to
  run on top of them. Today, routers are typically vertically integrated, where the hardware and all
  software are assembled by a single company.
• Complexity of Computation: Endnode protocol functions are more complex (application, transport)
  as compared to the corresponding functions in routers (routing, data link).
   As a consequence, endnode software has three important artifacts that seem hard to avoid, each of
which contributes to inefficiencies that must be worked around or minimized.
1. Structure: Because of the complexity and vastness of endnode software, code is structured and mod-
   ular to ease software development. In particular, unknown applications are allowed using a standard
   application programming interface (API) between the core operating system and the unknown ap-
   plication.
2. Protection: Because of the need to accommodate unknown applications, there is a need to protect
   applications from each other and to protect the operating system from applications.
3. Generality: Core routines such as buffer allocators and the scheduler are written with the most
   general use (and the widest variety of applications) in mind and thus are unlikely to be as efficient
   as special-purpose routines.
    In addition, since most endnodes were initially designed in an environment where the endnode
communicated with only a few nodes at a time, there is little surprise that when these nodes were
retrofitted as servers, a fourth artifact was discovered.
4. Scalability: By scalability, we often mean in terms of the number of concurrent connections. A
   number of operating systems use simple data structures that work well for a few concurrent con-

                                                        18.1 What this book has been about                    515




FIGURE 18.1
Endnode bottlenecks covered in this book. Associated with each bottleneck is the chapter in which the material is
reviewed, the underlying cause, and one or more sample solutions.



   nections but become major bottlenecks in a server environment, where there is a large number of
   connections.
    With this list of four endnode artifacts in mind, Fig. 18.1 reviews the main endnode bottlenecks
covered in this book, together with causes and workarounds. This picture is a more detailed version of
the corresponding figure in Chapter 1.
