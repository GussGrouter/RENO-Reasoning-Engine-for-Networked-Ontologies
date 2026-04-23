# Chunk 000001

- Source: raw/code/pdf/a-philosophy-of-software-design.pdf
- Slice: PDF pages 35–39
- From: processed/code/philosophy-ousterhout-abstractions-p35-39.md

---
4.3 Abstractions
The term abstraction is closely related to the idea of modular design. An
abstraction is a simplified view of an entity, which omits unimportant
details. Abstractions are useful because they make it easier for us to think about
and manipulate complex things.
    In modular programming, each module provides an abstraction in the form of
its interface. The interface presents a simplified view of the module’s
functionality; the details of the implementation are unimportant from the
standpoint of the module’s abstraction, so they are omitted from the interface.
    In the definition of abstraction, the word “unimportant” is crucial. The more
unimportant details that are omitted from an abstraction, the better. However, a

detail can only be omitted from an abstraction if it really is unimportant. An
abstraction can go wrong in two ways. First, it can include details that are not
really important; when this happens, it makes the abstraction more complicated
than necessary, which increases the cognitive load on developers using the
abstraction. The second error is when an abstraction omits details that really are
important. This results in obscurity: developers looking only at the abstraction
will not have all the information they need to use the abstraction correctly. An
abstraction that omits important details is a false abstraction: it might appear
simple, but in reality it isn’t. The key to designing abstractions is to understand
what is important, and to look for designs that minimize the amount of
information that is important.
    As an example, consider a file system. The abstraction provided by a file
system omits many details, such as the mechanism for choosing which blocks on
a storage device to use for the data in a given file. These details are unimportant
to users of the file system (as long as the system provides adequate performance).
However, some of the details of a file system’s implementation are important to
users. Most file systems cache data in main memory, and they may delay writing
new data to the storage device in order to improve performance. Some
applications, such as databases, need to know exactly when data is written
through to storage, so they can ensure that data will be preserved after system
crashes. Thus, the rules for flushing data to secondary storage must be visible in
the file system’s interface.
    We depend on abstractions to manage complexity not just in programming,
but pervasively in our everyday lives. A microwave oven contains complex
electronics to convert alternating current into microwave radiation and distribute
that radiation throughout the cooking cavity. Fortunately, users see a much
simpler abstraction, consisting of a few buttons to control the timing and
intensity of the microwaves. Cars provide a simple abstraction that allows us to
drive them without understanding the mechanisms for electrical motors, battery
power management, anti-lock brakes, cruise control, and so on.

Figure 4.1: Deep and shallow modules. The best modules are deep: they allow a lot of functionality to be
accessed through a simple interface. A shallow module is one with a relatively complex interface, but not
much functionality: it doesn’t hide much complexity.
