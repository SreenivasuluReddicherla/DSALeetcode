\# LeetCode 25: Reverse Nodes in k-Group



\## Problem

Given a linked list, reverse nodes in groups of size k and return the modified list.

If the number of nodes is not a multiple of k, the remaining nodes should stay as is.



\## Approach

\- Check if there are at least k nodes to reverse.

\- Reverse the first k nodes, then recursively process the rest.

\- Connect reversed blocks together.



\## Time \& Space Complexity

\- Time: O(n) – each node visited once

\- Space: O(n/k) recursion stack (O(1) if iterative)



\## Solutions

\- ✅ Java: ReverseKGroup.java

\- ✅ Python: reverse\_k\_group.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/reverse-nodes-in-k-group/)



