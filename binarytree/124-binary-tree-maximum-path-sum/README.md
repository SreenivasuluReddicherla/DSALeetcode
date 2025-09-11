\# LeetCode 124: Binary Tree Maximum Path Sum



\## Problem

Find the maximum path sum in a binary tree.  

A path can start and end at any node, but must contain at least one node.



\## Approach

\- Use \*\*DFS recursion\*\*.

\- For each node:

&nbsp; - Compute max gain from left and right subtrees (ignore negatives).

&nbsp; - Update global max with path sum through current node.

&nbsp; - Return max gain to parent (current node + max(left, right)).



\## Time \& Space Complexity

\- Time: O(n), every node visited once

\- Space: O(h), recursion depth (h = height of tree)



\## Solutions

\- ✅ Java: BinaryTreeMaxPathSum.java

\- ✅ Python: binary\_tree\_max\_path\_sum.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/)



