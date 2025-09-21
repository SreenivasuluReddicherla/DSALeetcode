\# LeetCode 35: Search Insert Position



\## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if inserted in order.



\## Approach

\- Use \*\*binary search\*\*.

\- If `target == nums\[mid]`, return `mid`.

\- If `target < nums\[mid]`, search left.

\- If `target > nums\[mid]`, search right.

\- If not found, `left` will be the insertion index.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(log n)  

\- \*\*Space:\*\* O(1)



\## Example

Input: nums = \[1,3,5,6], target = 5  

Output: 2  



Input: nums = \[1,3,5,6], target = 2  

Output: 1  



\## Solutions

\- ✅ Java: `SearchInsert.java`

\- ✅ Python: `search\_insert.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/search-insert-position/)



