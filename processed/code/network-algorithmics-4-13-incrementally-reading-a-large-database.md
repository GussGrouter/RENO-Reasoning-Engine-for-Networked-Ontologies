# Network Algorithmics — 4.13 Incrementally reading a large database (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 128
- Slice: from `4.13 Incrementally reading a large database` up to next detected section heading

---

4.13 Incrementally reading a large database
Suppose a user continuously reads a large database stored on a Website. The Web page can change
and the reader only wants the incremental (P12a) updates since the last read of the database. Thus in
Fig. 4.24 there is a database of highly popular food items that is being read constantly by readers around
the world who wish to keep up with culinary fashion. Fortunately, food fashions change slowly.
    Thus a reader that last read at 2 p.m. and reads again at 6 p.m. only wants the differences: Coke
to Pepsi, and Wheaties to Cheerios. If, on the other hand, a different user reads at 3 p.m. and then at
6 p.m., she, too, only wants the difference: Wheaties to Cheerios. This leads to the following problem.

Problem
Find a way for the database to efficiently perform such incremental queries. One solution is to have the
database remember what each user has previously read. However, it is unreasonable for the database
to remember what each user has previously read, since there may be millions of users. Find another
solution that is less burdensome for the database program.

102       Chapter 4 Principles in action




FIGURE 4.24
A slowly changing database of food items shown at three different times: 2 p.m., 3 p.m., and 6 p.m. Notice that only
the soft drink has changed from 2 to 3 p.m. and that only the cereal has changed from 3 to 6 p.m. Thus a reader who
is constantly monitoring the database wishes to find only the differences from the last time the database was read.




FIGURE 4.25
Solving the incremental-update problem using an update history list.



Hint: If the database does not store any information about the last Read performed by a user, then
it follows that user Read requests must pass some information (P10) about the last Read request
made by the same user. Passing the entire details of the last Read would be overkill and inefficient.
What simple piece of information can succinctly characterize the user’s last request? Now consider
adding redundant state (P12) at the database that can easily be indexed using the information
passed by the user to facilitate efficient incremental query processing.

Solution
As said earlier, user Read requests must pass some information (P10) about the last Read request made
by the same user. The most succinct and relevant piece of information about the last user request is the
time at which it was made. If user requests pass the time of the last Read, then the database needs to be
organized to efficiently compute all updates after any given time. This can be done by storing copies of
the database at all possible earlier times. This is clearly inefficient and can be avoided by storing only
the incremental changes (P12a). This leads to the following algorithm.

                                                            4.14 Binary search of long identifiers                    103



   Add an update history list to the database, with most recent updates closer to the head of the list.
Read requests carry the time T of the last Read, so a Read request can be processed by scanning the
update list from the head to find all updates after T .
   For example, in Fig. 4.25 the head of the update history list has the latest change (compare with
Fig. 4.24) at 6 p.m. from Wheaties to Cheerios and the next earliest change at 3 p.m. from Coke to
Pepsi. Consider a Read request that has a last Read time of 5 p.m. In this case, when scanning the list
from the head, the request processing will find the 6 p.m. update and stop when it reaches the 3 p.m.
update because 3 < 5. Thus the Read request will return only the first update.

Exercises

• If a single entry changes multiple times, a single entry change can be stored redundantly in the
  list, which costs space and time. What principle can you use to avoid this redundancy? Assume the
  database is just a collection of records and that you want each record to appear at most once in the
  incremental list.
• If the number of records is large or the foregoing trick is not adopted, the incremental list size will
  grow very big. Suggest a sensible policy for periodically reducing the size of the incremental list.
