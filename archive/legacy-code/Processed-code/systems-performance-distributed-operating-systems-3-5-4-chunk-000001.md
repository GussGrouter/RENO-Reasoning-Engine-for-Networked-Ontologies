3.5.4 Distributed Operating Systems
A distributed operating system runs a single operating system instance across a set of separate
computer nodes, networked together. A microkernel is commonly used on each of the nodes.
Examples of distributed operating systems include Plan 9 from Bell Labs, and the Inferno operating system.
While an innovative design, this model has not seen widespread use. Rob Pike, co-creator of
Plan 9 and Inferno, has described various reasons for this, including [Pike 00]:
“There was a claim in the late 1970s and early 1980s that Unix had killed operating
systems research because no one would try anything else. At the time, I didn’t believe
it. Today, I grudgingly accept that the claim may be true (Microsoft notwithstanding).”

123

124

Chapter 3 Operating Systems

On the cloud, today’s common model for scaling compute nodes is to load-balance across a
group of identical OS instances, which may scale in response to load (see Chapter 11, Cloud
Computing, Section 11.1.3, Capacity Planning).

