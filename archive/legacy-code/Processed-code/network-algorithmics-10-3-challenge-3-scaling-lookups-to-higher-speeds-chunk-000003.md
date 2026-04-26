# network-algorithmics-10-3-challenge-3-scaling-lookups-to-higher-speeds (chunk 000003)

addresses. In such a case these entries are stored in a small hardware lookup database called a content
addressable memory or CAM (studied in more detail in Chapter 11).
    The CAM lookup occurs in parallel with the hash lookup. Finally, in the extremely rare case when
several dozen addresses are added to the CAM (say, when new station addresses are learned that cause
collisions), the central processor initiates a rehashing operation and distributes the new hash function
to the line cards. It is perhaps ironic that rehashing occurred so rarely in practice that one might worry
whether the rehashing code was adequately tested!
    The Gigaswitch became a successful product, allowing up to 22 FDDI networks to be bridged to-
gether with other link technologies, such as ATM. Barry Spinney was assigned US patent 5,920,900,
“Hash-based translation method and apparatus with multiple-level collision resolution.” While tech-
niques based on perfect hashing (Dietzfelbinger et al., 1988) have been around for a while in the
theoretical community, Spinney’s contribution was to use a pragmatic version of the perfect hashing
idea for high-speed forwarding.
