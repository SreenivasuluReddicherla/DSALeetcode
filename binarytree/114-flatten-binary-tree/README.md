\# LeetCode 114: Flatten Binary Tree to Linked List



\## Problem

Flatten a binary tree into a linked list in-place.  

The flattened tree should follow preorder traversal (root → left → right).



\## Approach

\- \*\*Iterative\*\*: Use a Morris Traversal-like approach to rewire nodes.

\- \*\*Recursive\*\*: Flatten left \& right subtrees, then attach accordingly.



\## Time \& Space Complexity

\- Time: O(n) (every node visited once)

\- Space: O(1) iterative, O(h) recursive (h = height)



\## Solutions

\- ✅ Java: FlattenBinaryTree.java

\- ✅ Python: flatten\_binary\_tree.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)



