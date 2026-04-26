      9.7.3 Latency Heat Maps
      A heat map can be used to visualize latency, placing the passage of time on the x-axis, the I/O
      latency on the y-axis, and the number of I/O in a particular time and latency range on the z-axis,
      shown by color (darker means more). Heat maps were introduced in Chapter 2, Methodologies,
      Section 2.10.3, Heat Maps. An interesting disk example is shown in Figure 9.12.

      The workload visualized was experimental: I was applying sequential reads to multiple disks one
      by one to explore bus and controller limits. The resulting heat map was unexpected (it has been
      described as a pterodactyl) and shows the information that would be missed when only consid-
      ering averages. There are technical reasons for each of the details seen: e.g., the “beak” ends at
      eight disks, equal to the number of SAS ports connected (two x4 ports) and the “head” begins at
      nine disks once those ports begin suffering contention.

      I invented latency heat maps to visualize latency over time, inspired by taztool, described in the next
      section. Figure 9.12 is from Analytics in the Sun Microsystems ZFS Storage appliance [Gregg 10a]:
      I collected this and other interesting latency heat maps to share publicly and promote their use.
                                                                              9.7   Visualizations   489




Figure 9.12 Disk latency pterodactyl

The x- and y-axis are the same as a latency scatter plot. The main advantage of heat maps is that
they can scale to millions of events, whereas the scatter plot becomes “paint.” This problem was
discussed in Sections 2.10.2, Scatter Plots, and 2.10.3, Heat Maps.

