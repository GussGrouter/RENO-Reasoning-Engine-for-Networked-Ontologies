# systems-performance-point-in-time-recommendations-2-3-7 (chunk 000001)

# Systems Performance — 2.3.7 Point-in-Time Recommendations (PDF pages 68–72)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-concepts-2-3-6-to-2-3-8-p68-72.md
- Slice: 2.3.7 Point-in-Time Recommendations

---

2.3.7 Point-in-Time Recommendations
The performance characteristics of environments change over time, due to the addition of more
users, newer hardware, and updated software or firmware. An environment currently limited by
a 10 Gbit/s network infrastructure may start to experience a bottleneck in disk or CPU perfor-
mance after an upgrade to 100 Gbits/s.

Performance recommendations, especially the values of tunable parameters, are valid only at a
specific point in time. What may have been the best advice from a performance expert one week
may become invalid a week later after a software or hardware upgrade, or after adding more users.
30   Chapter 2 Methodologies


     Tunable parameter values found by searching on the Internet can provide quick wins—in some
     cases. They can also cripple performance if they are not appropriate for your system or workload,
     were appropriate once but are not now, or are appropriate only as a temporary workaround for a
     software bug that is fixed properly in a later software upgrade. It is akin to raiding someone else’s
     medicine cabinet and taking drugs that may not be appropriate for you, may have expired, or
     were supposed to be taken only for a short duration.

     It can be useful to browse such recommendations just to see which tunable parameters exist and
     have needed changing in the past. Your task then becomes to see whether and how these should
     be tuned for your system and workload. But you may still miss an important parameter if others
     have not needed to tune that one before, or have tuned it but haven’t shared their experience
     anywhere.

     When changing tunable parameters, it can be helpful to store them in a version control system
     with a detailed history. (You may already do something similar when using configuration man-
     agement tools such as Puppet, Salt, Chef, etc.) That way the times and reasons that tunables were
     changed can be examined later on.
