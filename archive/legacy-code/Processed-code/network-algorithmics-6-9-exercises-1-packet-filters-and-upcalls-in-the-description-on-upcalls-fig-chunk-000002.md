# network-algorithmics-6-9-exercises-1-packet-filters-and-upcalls-in-the-description-on-upcalls-fig (chunk 000002)

6. Comparing the APIC Approach to the ADC Approach: In the text we described the ADC ap-
   proach to application-level networking, thereby bypassing the kernel and avoiding system calls. We
   want to compare this approach to an approach used in the APIC chip. First use a search engine to
   locate and print out a paper called “The APIC Approach to High-Performance Network Interface
   Design: Protected DMA and Other Techniques” (Dittia et al., 1997). Read the paper carefully, and
   then answer the following questions about its particular twists to the ADC design for a practical
   system.
   • There are two types of memory the ADC approach protects: The device registers on the adaptor,
     and the buffer memory containing the data. The first is protected by overloading the virtual
     memory scheme; the second is protected by having the kernel hand the adaptor a list of pages
     that an application can read/write from. Contrast this to the APIC approach to protecting the
     device registers. Why is an access mask helpful? Why is each connection register mapped both
     into the application and kernel memory?
   • In the APIC, the buffer memory is protected by having the APIC read (from memory) a ker-
     nel descriptor that contains validation information about the buffer. In the ADC approach, the
     validating information is already in the adaptor. Why add this extra complexity?
   • In the APIC, there is a third kind of memory that needs to be protected: Buffer descriptors contain
     links to other descriptors, and this link memory needs to be validated. Why is this not needed in
     the ADC approach?
   • A different way to do link notarization is to have the kernel create an array of pointers to real
     buffers, one for each application. Only the kernel can read or write this array. The applications
     queue buffer descriptors as offsets into this array. This is a standard approach in systems called
     using one level of indirection. Compare this approach to the APIC link notarization approach.
   • A disadvantage of the APIC approach is that the adaptor has to do a number of Reads to main
     memory to do all its checks. How many such Reads are required in the worst case for a received
     packet? Why might this be insignificant?
   • The paper describes splitting a packet into two pieces. Why is this needed? What assumption
     does this method make about protocols (that an approach based on packet filters does not need)?

This page intentionally left blank

CHAPTER

Maintaining timers
                                                                                                                           7
                                                                           That was, is, and shall be: Time’s wheel runs back or stops.
                                                                                                                   —Robert Browning
