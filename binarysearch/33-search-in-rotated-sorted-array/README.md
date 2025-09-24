\# LeetCode 33: Search in Rotated Sorted Array



\## Problem

Given a rotated sorted array `nums` and a target value, return the index of the target if found, otherwise return `-1`.  

The array is rotated at some pivot but has no duplicates.



\## Approach

\- Use \*\*binary search\*\* with a twist:

&nbsp; - Identify which half (left or right) is \*\*sorted\*\*.

&nbsp; - Decide if the `target` lies in that half.

&nbsp; - Narrow the search accordingly.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(log n)

\- \*\*Space:\*\* O(1)



\## Example

Input: `nums = \[4,5,6,7,0,1,2], target = 0`  

Output: `4`



Input: `nums = \[4,5,6,7,0,1,2], target = 3`  

Output: `-1`



\## Solutions

\- ✅ Java: `SearchInRotatedSortedArray.java`

\- ✅ Python: `search\_in\_rotated\_sorted\_array.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)



