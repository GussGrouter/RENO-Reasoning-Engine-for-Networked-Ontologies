# network-algorithmics-5-4-2-io-lite-a-unified-view-of-buffering (chunk 000002)

7 Because of the overhead of copying data between a CGI process generating dynamic content and the server process, some
vendors have proposed merging the CGI code within the server process. However, that makes the system more brittle because
faulty third-party content-generation software can crash the server. Better solutions, such as Windows ASP, propose incorporating
safe languages into Web pages such that the server executes the code and puts the result in the page it serves. Thus, despite the
references to CGI processes in this chapter, CGI may well be obsolete.

5.4 Broadening to file systems               133

FIGURE 5.9
IO-Lite removes all the redundant copying in Fig. 5.1 by effectively passing around pointers (via VM mappings) to
a single IO-Lite buffer. Assuming the file, the TCP checksum, and the HTTP response are all cached, the Web server
only has to transmit these cached values in a single copy to the network interface.

application makes a call to read the file, no physical copy is made, but a buffer aggregate is created with
a pointer to the IO-Lite buffer. Next, when the application sends the file to TCP for transmission, the
network system gets a pointer to the same IO-Lite pages. To prevent errors, the IO-Lite system keeps a
reference count for each buffer and reallocates a buffer only when all users are done.
    Fig. 5.9 also shows two more optimizations. The application keeps a cache of HTTP responses for
common files and can often simply append the standard response with minimal modifications. Second,
every buffer is given a unique number (P12, add redundant state) by IO-Lite, and the TCP module
keeps a cache of checksums indexed by buffer number. Thus when a file is transmitted multiple times,
the TCP module can avoid calculating the checksum after the first time. Notice that these changes
eliminate all the redundancy in Fig. 5.1, which speeds up the processing of a response.
    IO-Lite can also be used to implement a modified pipe program that eliminates copying. When
this IPC mechanism is used between the CGI process and the server process, all copying is elimi-
nated without compromising the safety and fault isolation provided by implementing the two programs
as separate processes. IO-Lite can also allow applications to customize their buffer-caching strategy,
allowing fancier caching strategies for Web servers based on both size and access frequency.
    It is important to note that IO-Lite manages these performance feats without completely eliminating
the kernel and without closely tying the application with the kernel. The Cheetah Web server (Engler
et al., 1995) built over the Exokernel operating system takes a more extreme position, allowing each

134      Chapter 5 Copying data

application (including the Web server) to completely customize its network and file system. The Ex-
okernel mechanisms allow such extreme customization from each application without compromising
safety. By dint of these customizations, the Cheetah Web server can eliminate all the copies in Fig. 5.1
and also eliminate the TCP checksum calculation using a cache.
    While Cheetah does allow some further tricks (see the Exercises), the enormous software engineer-
ing challenge of designing and maintaining custom kernels for each application makes approaches such
as IO-Lite more attractive. IO-Lite comes close to the performance of customized kernels like Cheetah
with a much smaller set of software engineeringchallenges.
