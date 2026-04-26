# network-algorithmics-5-2-4-transparently-emulating-copy-semantics (chunk 000003)

To do so without a physical copy, the kernel’s data buffer must start at the same offset within the
page as the application’s receive buffer. For a large buffer, the first and last pages (which can be partially
filled) are probably most efficiently handled by a physical copy; however, the intermediate pages that
are full can simply be swapped from the kernel to the application by the right page table mappings.
There is a cute optimization called reverse copyout that is explored in the exercises.
     Given the complexity that underlies page table remapping, it is unclear how page remapping is done
efficiently in Genie. One possibility is that Genie uses the same fbuf idea of caching VM mappings on
a path basis6 to avoid the overhead of TLB flushing, dealing with multiple page tables, and so on.
     When all is said and done, can the TCOW idea benefit legacy applications? There is no experimental
confirmation of this in Brustoloni and Steenkiste (1996) and Brustoloni (1999) because the experiments
use a simple copy benchmark and not an existing application such as a Web server. Fundamentally, it
seems hard for an existing legacy application to benefit from the new kernel implementation of the
existing API.
     Consider an application running over TCP that supplies a buffer to TCP. Since there is no feedback
to the application (unlike fbufs), the application does not know when it can safely reuse the buffer. If
the application overwrites the buffer too early while TCP is holding the buffer for retransmission, then
safety is not compromised, but performance is compromised because of the physical copy involved in
COW. It appears improbable that an unmodified application could choose the times to modify buffers
in accordance with TCP sending times and would have aligned its buffers well enough to allow page
swapping to work well.
     Thus applications do need to be modified to take full advantage of the Genie system. Even if they do,
there is still the hard problem of knowing when to reuse a buffer because of the lack of feedback. The
application could monitor TCOW faults and accordingly modify its reuse pattern. But if applications
need to be modified in subtle ways to take full advantage of the new kernel, it is unclear what benefit
was gained from preserving the API. Nevertheless, the ideas in Genie are fun to study, and they fall
nicely within the general area of network algorithmics.
