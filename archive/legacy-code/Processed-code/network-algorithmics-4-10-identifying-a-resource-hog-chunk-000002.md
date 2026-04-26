# network-algorithmics-4-10-identifying-a-resource-hog (chunk 000002)

Thus to find the resource hog, the algorithm simply looks for the bit position i corresponding to the
rightmost bit set in the bitmap. The algorithm then returns the user at the head of the bucket list cor-
responding to position i. Thus in Fig. 4.19 the algorithm would return S4 instead of the more accurate
S3.

Exercises

• How is this data structure maintained? What happens if the resources in a user (e.g., S3) are reduced
  from 30 to 16? What kind of lists is needed for efficient maintenance?
• How large is each bitmap? How can finding the rightmost bit set be done efficiently?
