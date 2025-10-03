\# LeetCode 108: Convert Sorted Array to Binary Search Tree



\## Problem

Given an integer array `nums` where the elements are sorted in ascending order,  

convert it into a \*\*height-balanced\*\* Binary Search Tree (BST).



A height-balanced BST is defined as:

\- A binary tree in which the left and right subtrees of every node differ in height by no more than 1.



\## Approach

\- Use \*\*Divide and Conquer\*\*:

&nbsp; - Pick the middle element as the root (to keep balance).

&nbsp; - Recursively construct the left subtree using the left half of the array.

&nbsp; - Recursively construct the right subtree using the right half.



\## Time \& Space Complexity

\- \*\*Time:\*\* `O(n)` (each element is visited once)

\- \*\*Space:\*\* `O(log n)` (recursion stack in balanced tree)



\## Solutions

\- ✅ Java: `SortedArrayToBST.java`

\- ✅ Python: `sorted\_array\_to\_bst.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)



