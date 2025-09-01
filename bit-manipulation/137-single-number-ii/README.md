\# LeetCode 137: Single Number II



\## Problem

Find the element that appears only once in an array where every other element appears exactly three times.



\## Approach

\- Use bit manipulation with two variables (`ones` and `twos`) to simulate counting in base-3.

\- Bits appearing three times are cleared.

\- The remaining number in `ones` is the unique element.



\## Time \& Space Complexity

\- Time: O(n)

\- Space: O(1)



\## Solutions

\- ✅ Java: SingleNumberII.java

\- ✅ Python: single\_number\_ii.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/single-number-ii/)



