# network-algorithmics-5-2-3-fbufs-optimizing-page-remapping (chunk 000005)

can briefly toggle the write-enable bit when an fbuf is transferred from the application to the kernel; the
bit is set again when the fbuf is given back. If the application does a Write when it does not have write
permission, an exception is generated and the application crashes, leaving other processes unaffected.
    Since the toggling of the write-enable bits requires some of the overhead that fbufs worked hard to
avoid, the fbuf facility also allows another form of fbufs, called volatile. Observe that if the writer is a
trusted entity (such as the kernel), then there is no point enforcing write protection. If the kernel has a
bug that causes it to make unexpected writes, the whole system will crash anyway.
    Changing the API in this way sounds dramatic. Does this mean that the huge amount of existing
UNIX application software (which uses the networking stack) must be rewritten? Since this is infea-
sible, there are several ways out. First, the existing API can be augmented with new system calls. For
example, the Solaris extensions in Thadani and Khalidi (1995) add a uf_write() call in addition to the
standard write() call. Applications interested in performance can be rewritten using these new calls.
    Second, the extensions can be used in implementing common I/O substrates (such as the UNIX
stdio library) that are a part of several applications. Applications that are linked to this library do not
need to be changed and yet can potentially benefit in performance.
    Eventually, the pragmatic consideration is not whether the API changes but how hard it is to modify
applications to benefit from the API changes. The experiences described in Thadani and Khalidi (1995)
and Pai et al. (1999b) for a number of applications indicate that the changes required in an application
to migrate to an fbuf-like API are small and localized.
