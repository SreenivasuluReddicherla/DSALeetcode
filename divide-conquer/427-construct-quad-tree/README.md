\# LeetCode 427: Construct Quad Tree



\## Problem

Given a `n x n` binary grid of `0`s and `1`s, construct its \*\*quad tree\*\* representation.



A quad tree divides a 2D space into four quadrants recursively until all values in a quadrant are the same.



\## Approach

\- Use \*\*Divide and Conquer\*\*:

&nbsp; - Check if the current region is uniform (all 0 or all 1).

&nbsp; - If uniform → return leaf node.

&nbsp; - Else → divide into four quadrants and recursively build nodes.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n²) — every cell is visited once.

\- \*\*Space:\*\* O(log n) recursion depth.



\## Solutions

\- ✅ Java: `ConstructQuadTree.java`

\- ✅ Python: `construct\_quad\_tree.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/construct-quad-tree/)



