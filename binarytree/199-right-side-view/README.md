\# LeetCode 199: Binary Tree Right Side View



\## Problem

Given the root of a binary tree, return the values of the nodes visible when the tree is viewed from the right side.



\## Approach

\- Perform \*\*level-order traversal (BFS)\*\*.

\- At each level, record the \*\*last node\*\* (rightmost) in that level.

\- Add these values to the result.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n) – each node is visited once.

\- \*\*Space:\*\* O(n) – queue can hold up to one level of nodes.



\## Solutions

\- ✅ Java: `RightSideView.java`

\- ✅ Python: `right\_side\_view.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/binary-tree-right-side-view/)



