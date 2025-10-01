\# LeetCode 373: Find K Pairs with Smallest Sums



\## Problem

Given two sorted arrays `nums1` and `nums2`, return the `k` pairs `(u, v)` such that the sum `u + v` is the smallest.



\### Example

Input:  

nums1 = \[1,7,11], nums2 = \[2,4,6], k = 3  

Output: \[\[1,2],\[1,4],\[1,6]]  



\## Approach

\- Use a \*\*min-heap\*\* to store candidate pairs `(sum, i, j)`.  

\- Start with all pairs `(nums1\[i], nums2\[0])`.  

\- Pop the smallest sum, push the next candidate `(nums1\[i], nums2\[j+1])`.  

\- Repeat until we collect `k` pairs.  



\## Time \& Space Complexity

\- \*\*Time:\*\* O(k log k)  

\- \*\*Space:\*\* O(k)  



\## Solutions

\- ✅ Java: `FindKPairs.java`  

\- ✅ Python: `find\_k\_pairs.py`  



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)



