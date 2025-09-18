\# LeetCode 530: Minimum Absolute Difference in BST



\## Problem

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes.



\## Approach

\- Use \*\*in-order traversal\*\* of BST (sorted order).

\- Track the \*\*previous node value\*\* and compute differences with the current node.

\- Maintain the \*\*minimum difference\*\* found so far.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n) – each node visited once.

\- \*\*Space:\*\* O(h) – recursion stack, where h is tree height.



\## Solutions

\- ✅ Java: `MinAbsDiffBST.java`

\- ✅ Python: `min\_abs\_diff\_bst.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)



