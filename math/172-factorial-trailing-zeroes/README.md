\# LeetCode #172: Factorial Trailing Zeroes



\## Problem

Return the number of trailing zeroes in n!.



\## Approach

\- A trailing zero is produced by 10 = 2 × 5

\- Count the number of 5s in the prime factors of n!

\- Formula: n//5 + n//25 + n//125 + ...



\## Time and Space

\- Time: O(log n)

\- Space: O(1)



\## Java

\[FactorialTrailingZeroes.java](./FactorialTrailingZeroes.java)



\## Python

\[factorial\_trailing\_zeroes.py](./factorial\_trailing\_zeroes.py)



\## Link

\[LeetCode Problem](https://leetcode.com/problems/factorial-trailing-zeroes/)



