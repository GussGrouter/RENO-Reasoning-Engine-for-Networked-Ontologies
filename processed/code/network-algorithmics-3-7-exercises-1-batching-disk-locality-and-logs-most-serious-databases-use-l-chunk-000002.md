# network-algorithmics-3-7-exercises-1-batching-disk-locality-and-logs-most-serious-databases-use-l (chunk 000002)

• If the database represented by the log gets too far ahead of the database represented on disk,
     crash recovery can take too long. Describe a strategy to bound crash recovery times.
2. Relaxing Consistency Requirements in a Name Service: The Grapevine system (Birell et al.,
   1982) offers a combination of a name service (to translate user names to inboxes) and a mail service.
   To improve availability, Grapevine name servers are replicated. Thus any update to a registration
   record (e.g., Joe → MailSlot3) must be performed on all servers implementing replicas of that
   record. Standard database techniques for distributed databases require that each update be atomic;
   that is, the effect should be as if updates were done simultaneously on all replicas. Because atomic
   updates require that all servers be available, and registration information is not as important as,
   say, bank accounts, Grapevine provides only the following loose semantics (P3): All replicas will
   eventually agree if updates stop. Each update is timestamped and passed from one replica to the
   other in arbitrary order. The highest timestamped update wins.
   • Give an example of how a user could detect inconsistency in Joe’s registration during the con-
     vergence process.
   • If Joe’s record is deleted, it should eventually be purged from the database to save storage. Sup-
     pose a server purges Joe’s record immediately after receiving a Delete update. Why might Add
     updates possibly cause a problem? Suggest a solution.
   • The rule that the latest timestamp wins does not work well when two administrators try to create
     an entry with the same name. Because a later creation could be trapped in a crashed server,
     the administrator of the earlier creation can never know for sure that his creation has won. The
     Grapevine designers did not introduce mechanisms to solve this problem but relied on “some
     human-level centralization of name creation.” Explain their assumption clearly.
3. Replacing General-Purpose Routines with Special-Purpose Routines and Efficient Storage
   Allocators: Consider the design of a general storage allocator that is given control of a large contigu-
   ous piece of memory and may be asked by applications for smaller, variable-size chunks. A general
   allocator is quite complex: As time goes by, the available memory fragments and time must be spent
   finding a piece of the requested size and coalescing adjacent released pieces into larger free blocks.
   • Briefly sketch the design of a general-purpose allocator. Consult a textbook such as Horowitz
     and Sahni (1978) for examples of allocators.
   • Suppose a profile has shown that a large fraction of the applications ask for 64 bytes of storage.
     Describe a more efficient allocator that works for the special case (P6) of allocating just 64-byte
     quantities.
   • How would you optimize the expected case (P11) and yet handle requests for storage other than
     64 bytes?
4. Passing Information in Interfaces: Consider a file system that is reading or writing files from
   disk. Each random disk Read/Write involves positioning the disk over the correct track (seeking).
   If we have a sequence of, say, three Reads to Tracks 1, 15, and 7, it may pay to reorder the second
   and third Reads to reduce waste in terms of seek times. Clearly, as in P1, the larger the context of
   the optimization (e.g., the number of Reads or Writes considered for reordering), the greater the
   potential benefits of such seek optimization.

3.7 Exercises          73
