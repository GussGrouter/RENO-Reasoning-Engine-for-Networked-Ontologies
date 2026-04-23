# Systems Performance — universal scalability law (2.6.4) (universal-scalability-law-2-6-4) (PDF pages 98–114)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-modeling-scout-p98-106.md + processed/code/systems-performance-modeling-scout-p104-114.md

---

2.6.4 Universal Scalability Law
The Universal Scalability Law (USL), previously called the super-serial model [Gunther 97], was
developed by Dr. Neil Gunther to include a parameter for coherency delay. This was pictured
earlier as the coherence scalability profile, which includes the effects of contention.

USL can be defined as:

    C(N) = N/(1 + α(N – 1) + βN(N – 1))

C(N), N, and α are as with Amdahl’s Law of Scalability. β is the coherence parameter. When
β == 0, this becomes Amdahl’s Law of Scalability.

Examples of both USL and Amdahl’s Law of Scalability analysis are graphed in Figure 2.17.
66   Chapter 2 Methodologies




     Figure 2.17 Scalability models

     The input dataset has a high degree of variance, making it difficult to visually determine the
     scalability profile. The first ten data points, drawn as circles, were provided to the models. An
     additional ten data points are also plotted, drawn as crosses, which check the model prediction
     against reality.

     For more on USL analysis, see [Gunther 97] and [Gunther 07].
