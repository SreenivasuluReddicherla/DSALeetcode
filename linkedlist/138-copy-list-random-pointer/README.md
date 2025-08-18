\# LeetCode 138: Copy List with Random Pointer



\## Problem

Create a deep copy of a linked list where each node has:

\- A `next` pointer

\- A `random` pointer (may point to any node or null)



\## Approach

\- Use a HashMap to store mapping: original node → copied node

\- Two passes:

&nbsp; 1. Copy nodes (values only)

&nbsp; 2. Assign `next` and `random` pointers



\## Time \& Space Complexity

\- Time: O(n)

\- Space: O(n)



\## Solutions

\- ✅ Java: CopyListWithRandomPointer.java

\- ✅ Python: copy\_list\_random.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/copy-list-with-random-pointer/)



