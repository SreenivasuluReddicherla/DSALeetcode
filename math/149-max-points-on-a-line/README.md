\# LeetCode #149: Max Points on a Line



\## Problem

Given n points in a 2D plane, return the maximum number of points that lie on the same straight line.



\## Approach

\- Fix one point.

\- Compute the slope to every other point.

\- Count identical slopes using a hashmap.

\- Handle duplicates and vertical lines carefully.

\- Normalize slope using GCD.



\## Time and Space

\- Time: O(n^2)

\- Space: O(n)



\## Java

\[MaxPointsOnALine.java](./MaxPointsOnALine.java)



\## Python

\[max\_points\_on\_line.py](./max\_points\_on\_line.py)



\## Link

\[LeetCode Problem](https://leetcode.com/problems/max-points-on-a-line/)



