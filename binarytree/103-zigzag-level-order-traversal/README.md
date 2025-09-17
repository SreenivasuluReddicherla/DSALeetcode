\# LeetCode 103: Binary Tree Zigzag Level Order Traversal



\## Problem

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.  

(i.e., left-to-right, then right-to-left for the next level and alternate between).



\## Approach

\- Use \*\*BFS traversal\*\* with a queue.  

\- Use a flag `leftToRight` to alternate between left-to-right and right-to-left.  

\- Use `Deque` (double-ended queue) for efficient insertions at both ends.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n) – visit each node once.

\- \*\*Space:\*\* O(n) – queue holds up to one level of nodes.



\## Solutions

\- ✅ Java: `ZigzagLevelOrder.java`

\- ✅ Python: `zigzag\_level\_order.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)



