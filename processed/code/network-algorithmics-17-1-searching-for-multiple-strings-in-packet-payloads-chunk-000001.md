# network-algorithmics-17-1-searching-for-multiple-strings-in-packet-payloads (chunk 000001)

# Network Algorithmics — 17.1 Searching for multiple strings in packet payloads (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 518
- Slice: from `17.1 Searching for multiple strings in packet payloads` up to next detected section heading

---

17.1 Searching for multiple strings in packet payloads
The first few sections tackle a problem of detecting an attack by searching for suspicious strings in
payloads. A large number of attacks can be detected by their use of such strings. For example, packets
that attempt to execute the Perl interpreter have perl.exe in their payload. For example, the arachNIDS
database (Max Vision, 2001) of vulnerabilities contains the following description.
   An attempt was made to execute perl.exe. If the Perl interpreter is available to Web clients, it can
   be used to execute arbitrary commands on the Web server. This can be used to break into the server,
   obtain sensitive information, and potentially compromise the availability of the Web server and the
   machine it runs on. Many Web server administrators inadvertently place copies of the Perl interpreter
   into their Web server script directories. If perl is executable from the cgi directory, then an attacker
   can execute arbitrary commands on the Web server.
    This observation has led to a commonly used technique to detect attacks in so-called signature-based
intrusion detection systems such as Snort. The idea is that a router or monitor has a set of rules, much
like the classifiers in Chapter 12. However, the Snort rules go beyond classifiers by allowing a 5-tuple
rule specifying the type of packet (e.g., port number equal to Web traffic) plus an arbitrary string that
can appear anywhere in the packet payload.

492       Chapter 17 Network security

FIGURE 17.1
The Aho–Corasick algorithm builds an alphabetical trie on the set of strings to be searched for. A search for the
string “barney” can be found by following the “b” pointer at the root, the “a” pointer at the next node, etc. More in-
terestingly, the trie is augmented with failure pointers that prevent restarting at the top of the trie when failure occurs
and a new attempt is made to match, shifting one position to the right.

Thus the Snort rule for the attempt to execute perl.exe will specify the protocol (TCP) and destina-
tion port (80 for Web) as well as the string “perl.exe” occurring anywhere in the payload. If a packet
matches this rule, an alert is generated. Snort has 300 such augmented rules, with 300 possible strings
to search for.
    Early versions of Snort do string search by matching each packet against each Snort rule in turn.
For each rule that matches in the classifier part, Snort runs a Boyer–Moore search on the correspond-
ing string, potentially doing several string searches per packet. Since each scan through a packet is
expensive, a natural question is: can one search for all possible strings in one pass through packet?
    There are two algorithms that can be used for this purpose: the Aho–Corasick algorithm (Aho and
Corasick, 1975) and a modified algorithm due to Commentz-Walter (1979), which we describe next.
