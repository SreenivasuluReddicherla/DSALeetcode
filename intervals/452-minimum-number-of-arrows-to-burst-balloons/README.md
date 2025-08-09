\# LeetCode 452: Minimum Number of Arrows to Burst Balloons



\## Problem

Given a list of balloon intervals, find the minimum number of arrows required to burst all balloons.



\## Approach

\- Sort balloons by their end coordinate.

\- Use a greedy approach: shoot an arrow at the end of the current balloon range and cover as many overlapping balloons as possible.

\- If the next balloon starts after the current arrow position, shoot a new arrow.



\## Time \& Space Complexity

\- Time: O(n log n) (due to sorting)

\- Space: O(1)



\## Solutions

\- ✅ Java: MinimumArrows.java

\- ✅ Python: minimum\_arrows.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)



