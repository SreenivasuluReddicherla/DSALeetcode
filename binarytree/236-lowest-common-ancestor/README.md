\# LeetCode 236: Lowest Common Ancestor of a Binary Tree



\## Problem

Find the lowest common ancestor (LCA) of two given nodes in a binary tree.



\## Approach

\- Use recursive DFS (post-order).

\- If current node is `p` or `q`, return it.

\- Otherwise, recurse on left and right:

&nbsp; - If both sides return non-null → current node is LCA.

&nbsp; - Else, return the non-null side.



\## Time \& Space Complexity

\- Time: O(n) (visit all nodes once)

\- Space: O(h) (recursion stack, h = height of tree)



\## Solutions

\- ✅ Java: LowestCommonAncestor.java

\- ✅ Python: lowest\_common\_ancestor.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)



