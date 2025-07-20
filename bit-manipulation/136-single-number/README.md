\# LeetCode #136: Single Number



\## Problem

Given a non-empty array of integers where every element appears twice except for one, find that single one.



\## Approach

\- Use XOR:

&nbsp; - a ^ a = 0

&nbsp; - a ^ 0 = a

\- XOR all numbers → duplicates cancel → single number remains



\## Time and Space

\- Time: O(n)

\- Space: O(1)



\## Java

\[SingleNumber.java](./SingleNumber.java)



\## Python

\[single\_number.py](./single\_number.py)



\## Link

\[LeetCode Problem](https://leetcode.com/problems/single-number/)



