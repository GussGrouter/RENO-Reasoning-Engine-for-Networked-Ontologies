8.6.14

ext4slower (xfs, zfs, btrfs, nfs)

ext4slower(8) traces common ext4 operations and prints per-event details for those that
were slower than a given threshold. The operations traced are reads, writes, opens, and fsync.

(Omitted in this processed extract: sample lines above/below threshold — see PDF.)

The columns show the time (TIME), process name (COMM), and pid (PID), type of operation (T: R is
reads, W is writes, O is opens, and S is syncs), offset in Kbytes (OFF_KB), latency of the operation in
milliseconds (LAT(ms)), and the filename (FILENAME).

Example interpretation in the book: multiple **sync (S)** operations exceeding the default **10 ms**
threshold.

The threshold can be provided as an argument; selecting **0** milliseconds shows all operations:

(Omitted in this processed extract: verbose `ext4slower 0` listing — see PDF.)

A pattern can be seen in the output: mysqld performs writes to files followed by a later sync
operation.
Tracing all operations can produce a large amount of output with associated overheads. I only do
this for short durations (e.g., ten seconds) to understand patterns of file system operations that
are not visible in other summaries (ext4dist(8)).
Options include **-p PID** to trace a single process only, and **-j** to produce parsable (CSV) output.
