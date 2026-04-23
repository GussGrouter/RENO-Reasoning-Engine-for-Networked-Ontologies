# Systems Performance — Section 4.3.4 netlink (netlink-observability-4-3-4)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch4-scout-p171-220.txt
- PDF pages (approx): 171–220

---

4.3.4 netlink
netlink is a special socket address family (AF_NETLINK) for fetching kernel information. Use of
netlink involves opening a networking socket with the AF_NETLINK address family and then
using a series of send(2) and recv(2) calls to pass requests and receiving information in binary
structs. While this is a more complicated interface to use than /proc, it is more efficient, and also
supports notifications. The libnetlink library helps with usage.

145

146

Chapter 4 Observability Tools

As with earlier tools, strace(1) can be used to show where the kernel information is coming from.
Inspecting the socket statistics tool ss(8):
# strace ss
[...]
socket(AF_NETLINK, SOCK_RAW|SOCK_CLOEXEC, NETLINK_SOCK_DIAG) = 3
[...]

This is opening an AF_NETLINK socket for the group NETLINK_SOCK_DIAG, which returns
information about sockets. It is documented in the sock_diag(7) man page. netlink groups
include:
■

NETLINK_ROUTE: Route information (there is also /proc/net/route)

■

NETLINK_SOCK_DIAG: Socket information

■

NETLINK_SELINUX: SELinux event notifications

■

NETLINK_AUDIT: Auditing (security)

■

NETLINK_SCSITRANSPORT: SCSI transports

■

NETLINK_CRYPTO: Kernel crypto information

Commands that use netlink include ip(8), ss(8), routel(8), and the older ifconfig(8) and
netstat(8).

