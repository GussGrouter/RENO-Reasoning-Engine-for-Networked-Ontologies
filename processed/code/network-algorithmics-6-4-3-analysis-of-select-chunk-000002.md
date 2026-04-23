# network-algorithmics-6-4-3-analysis-of-select (chunk 000002)

Strategies and principles to fix select()
Given the sources of waste just listed, some simple strategies can be applied using our algorithmic
principles.
• Recreate interest on each call: Consider changing the API (P9) to use separate bitmaps for input
  and output. Alternatively, preserve the API and use incremental computation (P12a).
• Recheck state after resume: Pass information between protocol modules that know when a descriptor
  is ready and the select module (P9).
• Have kernel recheck readiness for descriptors known not to be ready: Kernel keeps state across calls
  so that it does not recheck readiness for descriptors known not to be ready (P12a, use incremental
  computation).
• Use bitmaps linear with ready size, not descriptor size: Change the API in a fundamental way to
  avoid the need for state-based queries about all descriptors represented by bitmaps (P9).
