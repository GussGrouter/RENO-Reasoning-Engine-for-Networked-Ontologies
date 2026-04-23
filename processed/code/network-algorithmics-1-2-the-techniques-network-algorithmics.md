# Network Algorithmics — 1.2 The techniques: network algorithmics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 34
- Slice: from `1.2 The techniques: network algorithmics` up to next detected section heading

---

1.2 The techniques: network algorithmics
Throughout this book, we will talk of many specific techniques: of interrupts, copies, and timing
wheels; of Pathfinder and Sting; of why some routers are very slow; and whether Web servers can
scale. But what underlies the assorted techniques in this book and makes it more than a recipe book
is the notion of network algorithmics. As said earlier, network algorithmics recognizes the primary
importance of taking a systems approach to streamlining network implementations.
    While everyone recognizes that the Internet is a system consisting of routers and links, it is perhaps
less obvious that every networking device, from the Cisco GSR to an Apache Web server, is also a sys-
tem. A system is built out of interconnected subsystems that are instantiated at various points in time.
For example, a core router consists of line cards with forwarding engines and packet memories con-
nected by a crossbar switch. The router behavior is affected by decisions at various time scales, which
range from manufacturing time (when default parameters are stored in NVRAM) to route computation
time (when routers conspire to compute routes) to packet-forwarding time (when packets are sent to
adjoining routers).
    Thus one key observation in the systems approach is that one can often design an efficient sub-
system by moving some of its functions in space (i.e., to other subsystems) or in time (i.e., to points
in time before or after the function is apparently required). In some sense, the practitioner of network
algorithmics is an unscrupulous opportunist willing to change the rules at any time to make the game
easier. The only constraint is that the functions provided by the overall system continue to satisfy users.
    In one of Mark Twain’s books, a Connecticut Yankee is transported back in time to King Arthur’s
court. The Yankee then uses a gun to fight against dueling knights accustomed to jousting with lances.
This is an example of changing system assumptions (replacing lances by guns) to solve a problem
(winning a duel).
    Considering the constraints faced by the network implementor at high speeds—increasingly com-
plex tasks, larger systems to support, small amounts of high-speed memory, and a small number of
memory accesses—it may require every trick, every gun in one’s arsenal, to keep pace with the increas-
ing speed and scale of the Internet. The designer can throw hardware at the problem, change the system
assumptions, design a new algorithm—whatever it takes to get the job done.
    This book is divided into four parts. The first part, of which this is the first chapter, lays a foundation
for applying network algorithmics to packet processing. The second chapter of the first part outlines
models, and the third chapter presents general principles used in the remainder of the book.

8         Chapter 1 Introducing network algorithmics




FIGURE 1.3
Getting wind of an evil packet by noticing the frequency of unprintable characters.


   One of the best ways to get a quick idea about what network algorithmics is about is to plunge right
away into a warm-up example. While the warm-up example that follows is in the context of a device
within the network where new hardware can be designed, note that Part 2 is about building efficient
servers using only software design techniques.
