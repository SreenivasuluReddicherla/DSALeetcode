\# LeetCode 173: Binary Search Tree Iterator



\## Problem

Design an iterator over a binary search tree (BST).  

\- `next()` → return the next smallest number.  

\- `hasNext()` → check if more numbers exist.  



\## Approach

\- Use a \*\*stack\*\* for controlled in-order traversal.

\- Push all left children from root.

\- `next()` → pop top node, process its right child.

\- `hasNext()` → check if stack is non-empty.



\## Time \& Space Complexity

\- Time: O(1) average per operation (amortized)

\- Space: O(h) where h = height of the tree (stack storage)



\## Solutions

\- ✅ Java: BSTIterator.java

\- ✅ Python: bst\_iterator.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/binary-search-tree-iterator/)



