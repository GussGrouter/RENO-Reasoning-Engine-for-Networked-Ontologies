# Systems Performance — Ch.8 §8.8.2 ext4 (four levers + mount man excerpt)

Source: `systems-performance-ch8-scout-p398-460.txt`, lines ~4701–4797 (print ~pp. 416–417).

## Summary

- **Four tuning surfaces** for ext2/3/4: **mount options**, **`tune2fs(8)`**, **`/sys/fs/ext4/...` property files**, **`e2fsck(8)`** (maintenance/repair side).
- **Mount options** come from **`mount(8)`**, **`/etc/fstab`**, or installer/boot config; **`mount(8)`** documents generic options; **ext4-specific** options are in **`ext4(5)`** on Linux.
- **Excerpt (generic mount):** documents **`atime`**, **`noatime`**, **`relatime`** semantics at a high level—**access time updates** interact with **read paths** and can add **metadata write traffic** when not strictly needed.

## Notes

- Long **`man mount`** / **`man ext4`** transcripts omitted; use local man pages + kernel **ext4** admin guide for authoritative option lists.
