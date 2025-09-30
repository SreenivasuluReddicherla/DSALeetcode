\# LeetCode 502: IPO



\## Problem

You are given `k` projects and initial capital `w`.  

Each project has a \*\*profit\*\* and a \*\*minimum capital requirement\*\*.  



Pick at most `k` projects to \*\*maximize final capital\*\*.  



\### Example

Input:  

k = 2, w = 0, profits = \[1,2,3], capital = \[0,1,1]  

Output: 4  



\## Approach

\- Use two heaps:

&nbsp; 1. \*\*Min-heap\*\* to track projects by required capital.

&nbsp; 2. \*\*Max-heap\*\* to pick the most profitable project available.

\- At each step:

&nbsp; - Add all affordable projects to the max-heap.

&nbsp; - Select the project with the highest profit.

&nbsp; - Increase available capital.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n log n + k log n)  

\- \*\*Space:\*\* O(n)



\## Solutions

\- ✅ Java: `IPO.java`

\- ✅ Python: `ipo.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/ipo/)



