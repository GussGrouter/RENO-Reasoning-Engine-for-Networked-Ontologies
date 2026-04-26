# Systems Performance — Ch.8 §8.8.2 ext4 (`/sys/fs/ext4`, docs, e2fsck)

Source: `systems-performance-ch8-scout-p398-460.txt`, lines ~4888–4960 (print ~pp. 417–418).

## Summary

- **Live tunables / introspection:** under **`/sys/fs/ext4/<device>`** (example path in book: **`/sys/fs/ext4/nvme0n1p1`**), many **knobs and read-only counters** appear as small files—**not all are writable tunables**.
- Example shown: **`inode_readahead_blks`** = **32** → bounds **inode table read-ahead** in **blocks** (interpretation: read-ahead depth for inode metadata scans).
- **Authoritative reference:** Linux **admin-guide/ext4** documentation (`ext4.rst` / current kernel docs URL in book)—lists **mount options** and explains **sysfs** entries.
- **`e2fsck -D -f device`:** optional maintenance to **reindex directories**; may help some **large-directory** performance paths. Other **`e2fsck`** modes are **integrity/repair**, not routine tuning.

## Notes

- Example **`ls`** / **`cat`** listings truncated in processed text; see PDF for full directory dumps.
