# network-algorithmics-16-21-exercises-1-using-dram-backed-up-counters-this-chapter-described-only-th (chunk 000002)

From denial-of-service to Smurf attacks, hackers that perpetrate exploits have captured both the imag-
ination of the public and the ire of victims. There is some reason for indignation and ire. A survey by
the Computer Security Institute placed the cost of computer intrusions at an average of $970,000 per
company in 2000.
     Thus there is a growing market for intrusion detection, a field that consists of detecting and reacting
to attacks. A 2020 report says that the Intrusion detection market is was USD 4.57 billion in 2020 and is
forecasted to reach USD 9.04 billion by 2028 (Fior Markets, 2020). Further, the report says that roughly
half this market is for network intrusion detection, the topic of this chapter.
     Yet the capabilities of current intrusion detection systems are widely accepted as inadequate, partic-
ularly in the context of growing threats and capabilities. The first problem with some current systems
are that they are slow; but the bigger problem is that they have a high false-positive rate. As a result of
these deficiencies, intrusion detection serves primarily a monitoring and audit function rather than as a
real-time component of a protection architecture on par with firewalls and encryption.
     However, many vendors have introduced real-time intrusion detection systems. If intrusion detection
systems can work in real time with only a small fraction of false positives, they can actually be used to
respond to attacks by either deflecting the attack or tracing the perpetrators.
     Intrusion detection systems (IDSs) have been studied in many forms since Denning’s classic sta-
tistical analysis of host intrusions (Denning, 1987). Today, IDS techniques are usually classified as
either signature detection or anomaly detection. Signature detection is based on matching events to the
signatures of known attacks.
     In contrast, anomaly detection, based on statistical or learning theory techniques, identifies aberrant
events, whether known to be malicious or not. As a result, anomaly detection can potentially detect
new types of attacks that signature-based systems will miss. Unfortunately, anomaly detection systems
are prone to falsely identifying events as malicious. Thus this chapter does not address anomaly-based
methods.
     Meanwhile, signature-based systems are highly popular due to their relatively simple implemen-
tation and their ability to detect commonly used attack tools. The lightweight detection system Snort
(Roesch, 1999) is one of the more popular examples because of its free availability and efficiency.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00025-7
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                489

490      Chapter 17 Network security
