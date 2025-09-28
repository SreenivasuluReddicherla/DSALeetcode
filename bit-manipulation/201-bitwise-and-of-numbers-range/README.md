\# LeetCode 201: Bitwise AND of Numbers Range



\## Problem

Given two integers `left` and `right`, return the bitwise \*\*AND\*\* of all numbers in the inclusive range `\[left, right]`.



\## Approach

\- The common prefix of the binary representation of `left` and `right` is the result.

\- Keep right-shifting both numbers until they become equal.

\- Count how many shifts were made and left-shift back.



\### Example

Input: `left = 5, right = 7`  

Binary:



