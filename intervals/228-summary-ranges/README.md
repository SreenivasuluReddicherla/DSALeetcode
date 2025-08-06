\# LeetCode 228: Summary Ranges



\## Problem

You are given a sorted unique integer array. Return the smallest sorted list of ranges that cover all the numbers in the array exactly.



\## Approach

\- Use a while loop to traverse the array.

\- Track the start of each range.

\- If a range continues (i.e., consecutive numbers), extend it.

\- Otherwise, record the single number or range.



\## Time \& Space Complexity

\- Time: O(n)

\- Space: O(1) – aside from output



\## Solutions

\- ✅ Java: SummaryRanges.java

\- ✅ Python: summary\_ranges.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/summary-ranges/)



