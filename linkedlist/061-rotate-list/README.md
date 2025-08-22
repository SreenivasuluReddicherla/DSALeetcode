\# LeetCode 61: Rotate List



\## Problem

Rotate the linked list to the right by \*k\* positions.



\## Approach

\- Find the length of the list.

\- Connect tail to head to make it circular.

\- New head is at position `(length - k % length)`.

\- Break the cycle.



\## Time \& Space Complexity

\- Time: O(n)

\- Space: O(1)



\## Solutions

\- ✅ Java: RotateList.java

\- ✅ Python: rotate\_list.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/rotate-list/)



