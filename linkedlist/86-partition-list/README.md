\# LeetCode 86: Partition List



\## Problem

Given the head of a linked list and a value x, partition it such that:

\- All nodes less than x appear before nodes greater than or equal to x.

\- Relative order of nodes is preserved.



\## Approach

\- Use two dummy lists: `before` for nodes < x, and `after` for nodes >= x.

\- Traverse the list once and partition nodes accordingly.

\- Connect the two lists at the end.



\## Time \& Space Complexity

\- Time: O(n)  

\- Space: O(1) (only extra pointers used)



\## Solutions

\- ✅ Java: PartitionList.java

\- ✅ Python: partition\_list.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/partition-list/)



