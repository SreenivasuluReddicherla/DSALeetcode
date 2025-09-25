\# LeetCode 34: Find First and Last Position of Element in Sorted Array



\## Problem

Given a sorted array `nums` and a target value, return the starting and ending position of the target value.  

If the target is not found, return `\[-1, -1]`.



\## Approach

\- Use \*\*binary search\*\* twice:

&nbsp; - Once to find the \*\*first occurrence\*\*.

&nbsp; - Once to find the \*\*last occurrence\*\*.

\- Return both indices.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(log n) (binary search twice)

\- \*\*Space:\*\* O(1)



\## Example

Input: `nums = \[5,7,7,8,8,10], target = 8`  

Output: `\[3,4]`



Input: `nums = \[5,7,7,8,8,10], target = 6`  

Output: `\[-1,-1]`



\## Solutions

\- ✅ Java: `FindFirstAndLastPosition.java`

\- ✅ Python: `find\_first\_and\_last\_position.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)



