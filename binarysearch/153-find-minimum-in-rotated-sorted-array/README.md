\# LeetCode 153: Find Minimum in Rotated Sorted Array



\## Problem

Given a rotated sorted array with unique elements, find the minimum element.



\## Approach

\- Use \*\*binary search\*\*:

&nbsp; - Compare `nums\[mid]` with `nums\[right]`.

&nbsp; - If `nums\[mid] > nums\[right]`, the minimum is in the right half.

&nbsp; - Otherwise, it’s in the left half (including `mid`).

\- Stop when `left == right`.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(log n)

\- \*\*Space:\*\* O(1)



\## Example

Input: `nums = \[3,4,5,1,2]`  

Output: `1`



Input: `nums = \[4,5,6,7,0,1,2]`  

Output: `0`



\## Solutions

\- ✅ Java: `FindMinimumRotatedArray.java`

\- ✅ Python: `find\_minimum\_rotated\_array.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)



