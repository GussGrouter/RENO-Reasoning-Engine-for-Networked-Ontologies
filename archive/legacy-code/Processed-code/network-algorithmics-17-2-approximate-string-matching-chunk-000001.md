# network-algorithmics-17-2-approximate-string-matching (chunk 000001)

# Network Algorithmics — 17.2 Approximate string matching (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 522
- Slice: from `17.2 Approximate string matching` up to next detected section heading

---

17.2 Approximate string matching
This section briefly considers an even harder problem, that of approximately detecting strings in pay-
loads. Thus instead of settling for an exact match or a prefix match, the specification now allows a few
errors in the match. For example, with one insertion, “p-erl.exe” should match “perl.exe,” where the
intruder may have added a character.
    While the security implications of using the mechanisms described next need much more thought,
the mechanisms themselves are powerful and should be part of the arsenal of designers of detection
mechanisms.
    The first simple idea can handle substitution errors. A substitution error is a replacement of one or
more characters with others. For example, “parl.exe” can be obtained from “perl.exe” by substituting
“a” for “e.” One way to handle this is to search not for the complete string but for one or more random
projections of the original string.
    For example, in Fig. 17.3 instead of searching for “babar” one could search for the first, third, and
fourth characters in “babar.” Thus the misspelled string “babad” will still be found. Of course, this
particular projection will not find a misspelled string such as “rabad.” To make it hard for an adversary,
the scheme in general can use a small set of such random projections. This simple idea is generalized
greatly in a set of papers on locality-sensitive hashing (e.g., Indyk et al., 1997).
    Interestingly, the use of random projections may make it hard to efficiently shift one character to the
right. One alternative is to replace the random projections with deterministic projections. For example,
if one replaces every string by its two halves and places each half in an Aho–Corasick trie, then any
one substitution error will be caught without slowing down the Aho–Corasick processing. However,
the final efficiency will depend on the number of false alarms.
    The simplest random projection idea, described earlier, does not work with insertions or deletions
that can displace every character one or more steps to the left or right. One simple and powerful way of

496      Chapter 17 Network security
