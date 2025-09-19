\# LeetCode 230: Kth Smallest Element in a BST



\## Problem

Given the root of a BST and an integer `k`, return the k-th smallest value (1-indexed) of all the values of the nodes in the tree.



\## Approach

\- Use \*\*in-order traversal\*\* (left → root → right) since BST in-order is sorted.

\- Maintain a counter to track visited nodes.

\- Stop when the k-th element is found.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(h + k) ≈ O(n) worst-case

\- \*\*Space:\*\* O(h) recursion stack (h = tree height)



\## Solutions

\- ✅ Java: `KthSmallestBST.java`

\- ✅ Python: `kth\_smallest\_bst.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)



