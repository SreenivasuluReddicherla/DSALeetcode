\# LeetCode 98: Validate Binary Search Tree



\## Problem

Given the root of a binary tree, determine if it is a valid binary search tree (BST).



\## Approach

\- Use recursion with \*\*min and max bounds\*\* for each node.

\- A valid BST must satisfy:

&nbsp; - Left subtree values < node value

&nbsp; - Right subtree values > node value

\- Update bounds while traversing down.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n) (visit every node once)

\- \*\*Space:\*\* O(h) recursion stack (h = tree height)



\## Solutions

\- ✅ Java: `ValidateBST.java`

\- ✅ Python: `validate\_bst.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/validate-binary-search-tree/)



