# network-algorithmics-4-13-incrementally-reading-a-large-database (chunk 000002)

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
