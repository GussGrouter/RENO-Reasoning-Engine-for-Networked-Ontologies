<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (combined extract; Chapter 5 Applications §5.2.5–5.2.7) -->
updated copy [Linux 20e].
Investigating performance issues involving locks can be time-consuming and often requires
familiarity with the application source code. This is usually an activity for the developer.

179

180

Chapter 5 Applications

Hash Tables
A hash table of locks can be used to employ the optimum number of locks for a large number of
data structures. While hash tables are summarized here, this is an advanced topic that assumes a
programming background.
Picture the following two approaches:
■
