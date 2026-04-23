Some applications force this behavior by binding themselves to CPUs. This can significantly
improve performance for some systems. It can also reduce performance when the bindings conflict with other CPU bindings, such as device interrupt mappings to CPUs.
Be especially careful about the risks of CPU binding when there are other tenants or applications
running on the same system. This is a problem I’ve encountered in OS virtualization (container)
environments, where an application can see all the CPUs and then bind to some, on the assumption that it is the only application on the server. When a server is shared by other tenant applications
that are also binding, multiple tenants may unknowingly bind to the same CPUs, causing CPU
contention and scheduler latency even though other CPUs are idle.
Over the lifespan of an application the host system may also change, and bindings that are not
updated may hurt instead of help performance, for example when they needlessly bind to CPUs
across multiple sockets.

5.2.8 Performance Mantras
For more techniques for improving application performance, see the Performance Mantras
methodology from Chapter 2. In summary:
1. Don’t do it.
2. Do it, but don’t do it again.
3. Do it less.
4. Do it later.
5. Do it when they’re not looking.
6. Do it concurrently.
7. Do it cheaper.
The first item, “Don’t do it,” is eliminating unnecessary work. For more detail on this methodology see Chapter 2, Methodologies, Section 2.5.20, Performance Mantras.

