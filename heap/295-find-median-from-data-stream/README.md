\# LeetCode 295: Find Median from Data Stream



\## Problem

Design a data structure that supports:

\- `addNum(num)`: Add a number from the stream.

\- `findMedian()`: Return the median of all numbers added so far.



\## Approach

We use two heaps:

\- \*\*Max-Heap\*\*: Stores the smaller half of the numbers.

\- \*\*Min-Heap\*\*: Stores the larger half.



Balance heaps so that:

\- Either both heaps have equal size, or

\- Max-Heap has one extra element.



Median:

\- If sizes are equal → average of tops.

\- Else → top of Max-Heap.



\## Time \& Space Complexity

\- \*\*Time:\*\* `O(log n)` per insertion  

\- \*\*Space:\*\* `O(n)`  



\## Solutions

\- ✅ Java: `MedianFinder.java`

\- ✅ Python: `median\_finder.py`



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/find-median-from-data-stream/)



