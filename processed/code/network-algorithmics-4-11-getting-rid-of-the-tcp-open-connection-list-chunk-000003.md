# network-algorithmics-4-11-getting-rid-of-the-tcp-open-connection-list (chunk 000003)

• Write pseudocode for the addition of a new connection, the termination of a connection, and the
  timer-based traversal.
• How can we get away with singly linked lists for the lists of connections in each hash table list?
• Hugh Hopeful is always interested in clever tricks that he never thinks through completely. He
  suggests a way to avoid back pointers in any doubly linked list. Suppose a node X needs to be
  deleted. Normally, the deletion routine is passed a handle to retrieve X, which is typically a pointer
  to node X. Instead, Hugh suggests that the handle be a pointer to the node before X in the linked
  list (except when X is the head of the list when the handle is a null pointer). Hugh claims that this
  allows his implementation to efficiently locate both the node prior to X and the node after X using
  only forward pointers. Present a counter-example to stop Hugh before he writes some buggy code.
