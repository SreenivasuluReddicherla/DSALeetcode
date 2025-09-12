\# LeetCode 222: Count Complete Tree Nodes



\## Problem

Count the number of nodes in a complete binary tree.



\## Approach

\- Compute left and right subtree heights.

\- If equal → left subtree is a perfect binary tree.

\- Otherwise → right subtree is perfect.

\- Recurse on the incomplete side.



\## Time \& Space Complexity

\- Time: O(log² n) (height \* recursion)

\- Space: O(log n) (recursion stack)



\## Solutions

\- ✅ Java: CountCompleteTreeNodes.java

\- ✅ Python: count\_complete\_tree\_nodes.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/count-complete-tree-nodes/)



