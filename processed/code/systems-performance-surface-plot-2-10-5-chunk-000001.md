# systems-performance-surface-plot-2-10-5 (chunk 000001)

# Systems Performance — surface plot (2.10.5) (surface-plot-2-10-5) (PDF pages 118–140)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch2-tail-scout-p118-140.md

---

2.10.5      Surface Plot
     This is a representation of three dimensions, rendered as a three-dimensional surface. It works
     best when the third-dimension value does not frequently change dramatically from one point
     to the next, producing a surface resembling rolling hills. A surface plot is often rendered as a
     wireframe model.

     Figure 2.33 shows a wireframe surface plot of per-CPU utilization. It contains 60 seconds of
     per-second values from many servers (this is cropped from an image that spanned a data center
     of over 300 physical servers and 5,312 CPUs) [Gregg 11b].

     Each server is represented by plotting its 16 CPUs as rows on the surface, the 60 per-second uti-
     lization measurements as columns, and then setting the height of the surface to the utilization
     value. Color is also set to reflect the utilization value. Both hue and saturation could be used, if
     desired, to add fourth and fifth dimensions of data to the visualization. (With sufficient resolu-
     tion, a pattern could be used to indicate a sixth dimension.)

     These 16 × 60 server rectangles are then mapped across the surface as a checkerboard. Even
     without markings, some server rectangles can be clearly seen in the image. One that appears as
     an elevated plateau on the right shows that its CPUs are almost always at 100%.

     The use of grid lines highlights subtle changes in elevation. Some faint lines are visible, which
     indicate a single CPU constantly running at low utilization (a few percent).
                                                                                2.11   Exercises   85




Figure 2.33 Wireframe surface plot: data center CPU utilization
