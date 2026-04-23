# network-algorithmics-4-1-buffer-validation (chunk 000001)

# Network Algorithmics — buffer validation of application device channels (4.1) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 104 -l 113 -layout
- Slice: from `4.1 Buffer validation of application device channels` up to (excluding) `4.2`

---

4.1 Buffer validation of application device channels                         77

validation process be sped up? Try thinking through the solution before reading the hint and solutions
that follow.

Hint: A good approach to reduce the complexity of validation is to use a better data structure than
a list (P15). Which data structure would you choose? However, one can improve worst-case behavior
even further and get smaller constant factors by using system thinking and by passing hints in
interfaces (P9).
    An algorithmic thinker will immediately consider implementing the set of valid pages as a hash
table instead of a list. This provides an O(1) average search time. Hashing has two disadvan-
tages: (1) good hash functions that have small collision probabilities are expensive computationally;
(2) hashing does not provide a good worst-case bound. Binary search does provide logarithmic worst-
case search times, but this is expensive (it also requires keeping the set sorted) if the set of pages
is large and packet transmission rates are higher. Instead, we replace the hash table lookup by an
indexed array lookup, as follows (try using P9 before you read on).

Solution
The adaptor stores the set of valid pages for each application in an array, as shown in Fig. 4.2. This array
is updated only when the kernel updates the set of valid pages for the application. When the application
does a Receive into page A, it also passes to the adaptor a handle (P9). The handle is the index of the
array position where A is stored. The adaptor can use this to quickly confirm whether the page in the
Receive request matches the page stored in the handle. The cost of validation is a bounds check (to see
if the handle is a valid index), one array lookup, and one compare.

Exercises

• Is the handle a hint or a tip? Let’s invoke principle P1: If this is a handle, why pass the page number
  (e.g., A) in the interface? Why does removing the page number speed up the confirmation task
  slightly?

FIGURE 4.2
Finessing the need for a hash table lookup by passing a handle across the interface between the application and
adaptor.

---

## PDF page 105

78        Chapter 4 Principles in action

• To find the array corresponding to application P normally requires a hash table search using P as
  the key. This weakens the argument for getting rid of the hash table search to check if the page is
  valid—unless, of course, the hash search of P can be finessed as well. How can this be done?
