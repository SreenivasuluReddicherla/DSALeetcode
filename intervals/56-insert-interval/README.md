\# LeetCode 57: Insert Interval



\## Problem

You are given a list of non-overlapping intervals sorted by their start times and a new interval.  

Insert the new interval into the list such that the list remains sorted and merged if necessary.



\## Approach

\- Add all intervals ending before `newInterval` starts.

\- Merge all overlapping intervals into `newInterval`.

\- Append the remaining intervals.



\## Time \& Space Complexity

\- Time: O(n)

\- Space: O(n)



\## Solutions

\- ✅ Java: InsertInterval.java

\- ✅ Python: insert\_interval.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/insert-interval/)



