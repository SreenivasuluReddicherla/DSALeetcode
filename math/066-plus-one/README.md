# LeetCode #66: Plus One

## Problem
Given a non-empty array of digits representing a non-negative integer, increment the integer by one.

## Approach
- Traverse from end to start
- If digit < 9, increment and return
- Else, set to 0 and carry over
- If all digits are 9, prepend 1

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1) (excluding output)

## Java
[PlusOne.java](./PlusOne.java)

## Python
[plus-one.py](./plus-one.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/plus-one/)
