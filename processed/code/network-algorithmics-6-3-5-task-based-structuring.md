# Network Algorithmics — 6.3.5 Task-based structuring (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 185
- Slice: from `6.3.5 Task-based structuring` up to next detected section heading

---

6.3.5 Task-based structuring
The top of Fig. 6.6 depicts the event-driven approach augmented with helper processes. Notice the
similarity to the simple event-handler approach shown at the bottom of Fig. 6.5, except for the addition
of helper processes.
    There are some problems with the event-driven architecture with helper processes.

                                                              6.4 Scalable I/O Notification          159



• Complexity: The application designer must manage the state machine for juggling client requests
  without help.
• Modularity: The code for the server is written as one piece. While Web servers are popular, there are
  many other Web services that may use some similar pieces of code (e.g., for accepting connections).
  A more modular approach could allow code reuse.
• Overload control: Production Web servers have to deal with wide variations of load from huge
  client populations. Thus it is crucial to continue to make some progress during overload (without
  thrashing) and to be as fair as possible across clients.
    The main idea in the staged event-driven architecture (Welsh et al., 2001) is to exploit another degree
of freedom (P13) in decomposing code. Instead of decomposing into threads horizontally by client, as
in a multithreaded architecture, the server system is decomposed vertically by tasks within each client
request cycle, as shown on the bottom of Fig. 6.5. Each stage can be handled by one or more threads.
Thus the staged model can be considered a refinement of the simple event-driven model. This is because
it assigns a main thread and a potential thread to each stage of server processing. Once that is done, the
stages communicate via queues, and more refined overload control can be done at each stage.
    As far as we can determine, event based web servers still rule the roost in most major web servers.
Despite the potential advantages of the SEDA model, it has influenced server implementations without
being directly used. Part of the reason is that the technology has changed since SEDA was proposed, as
threading has become cheaper and multicore machines are standard. A retrospective on SEDA (2010)
written ten years after the paper suggests that one advantage of SEDA compared to more standard
approaches today is that task queues makes bottlenecks explicit. This allows more surgical and fairer
handling of requests during overload conditions.
