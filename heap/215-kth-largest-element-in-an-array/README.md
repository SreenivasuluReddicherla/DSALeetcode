\# LeetCode 215: Kth Largest Element in an Array



\## Problem

Find the \*\*kth largest element\*\* in an unsorted array.  

Note: The array is not necessarily sorted.



\### Example

Input: `nums = \[3,2,1,5,6,4], k = 2`  

Output: `5`



\## Approach

\- Use a \*\*min-heap\*\* of size `k`.

\- Keep pushing elements into the heap.

\- If the heap size exceeds `k`, pop the smallest.

\- At the end, the root of the heap is the `k`th largest element.



\## Time \& Space Complexity

\- \*\*Time:\*\* O(n log k)  

\- \*\*Space:\*\* O(k)



\## Solutions

\- ✅ Java: `KthLargestElement.java`

\- ✅ Python: `kth\_largest.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/kth-largest-element-in-an-array/)



