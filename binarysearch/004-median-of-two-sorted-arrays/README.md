\# LeetCode 4: Median of Two Sorted Arrays



\## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, return the median of the two sorted arrays.



\## Approach

\- Use \*\*binary search\*\* on the smaller array.

\- Partition both arrays such that:

&nbsp; - Left half contains `(m+n+1)/2` elements.

&nbsp; - Ensure `max(left) <= min(right)` on both sides.

\- Return median:

&nbsp; - If total length is odd → max of left partition.

&nbsp; - If even → average of max(left) and min(right).



\## Time \& Space Complexity

\- \*\*Time:\*\* O(log(min(m, n)))

\- \*\*Space:\*\* O(1)



\## Example

Input: nums1 = \[1, 3], nums2 = \[2]  

Output: 2.0  



Input: nums1 = \[1, 2], nums2 = \[3, 4]  

Output: 2.5  



\## Solutions

\- ✅ Java: `MedianTwoSortedArrays.java`

\- ✅ Python: `median\_two\_sorted\_arrays.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/median-of-two-sorted-arrays/)



