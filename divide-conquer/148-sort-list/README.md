\# LeetCode 148: Sort List



\## Problem

Sort a linked list in \*\*O(n log n)\*\* time and \*\*O(1)\*\* space (constant space complexity).



\## Approach

\- Use \*\*Merge Sort\*\* algorithm for linked lists.

\- Steps:

&nbsp; 1. \*\*Split\*\* the list into two halves using the slow and fast pointer approach.

&nbsp; 2. \*\*Recursively sort\*\* each half.

&nbsp; 3. \*\*Merge\*\* the two sorted halves.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n log n)

\- \*\*Space:\*\* O(log n) (recursion stack)



\## Solutions

\- ✅ Java: `SortList.java`

\- ✅ Python: `sort\_list.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/sort-list/)



