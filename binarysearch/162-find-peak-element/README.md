\# LeetCode 162: Find Peak Element



\## Problem

A peak element is one that is strictly greater than its neighbors.  

Given an integer array `nums`, return the index of \*\*any\*\* peak element.



You may assume that `nums\[-1] = nums\[n] = -∞`, so a peak always exists.



\## Approach

\- Use \*\*binary search\*\*:

&nbsp; - Compare `nums\[mid]` and `nums\[mid+1]`.

&nbsp; - If `nums\[mid] > nums\[mid+1]`, then the peak is on the \*\*left\*\* (including `mid`).

&nbsp; - Otherwise, the peak is on the \*\*right\*\*.

\- Continue until `left == right`, which is the peak index.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(log n)

\- \*\*Space:\*\* O(1)



\## Example

Input: `nums = \[1,2,3,1]`  

Output: `2` (element `3` is a peak)



Input: `nums = \[1,2,1,3,5,6,4]`  

Output: `1` or `5` (elements `2` and `6` are both peaks)



\## Solutions

\- ✅ Java: `FindPeakElement.java`

\- ✅ Python: `find\_peak\_element.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/find-peak-element/)



