\# LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal



\## Problem

Reconstruct a binary tree from inorder and postorder traversal arrays.



\## Approach

\- Postorder gives root (last element).

\- Inorder splits left and right subtrees.

\- Use recursion + hashmap for fast lookups.

\- Build right subtree before left (postorder rule).



\## Time \& Space Complexity

\- Time: O(n) (each node processed once)

\- Space: O(n) (hashmap + recursion stack)



\## Solutions

\- ✅ Java: BuildTreePost.java

\- ✅ Python: build\_tree\_post.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)



