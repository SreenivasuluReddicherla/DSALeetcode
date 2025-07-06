# LeetCode #13: Roman to Integer

## Problem
Convert a Roman numeral string to an integer. Roman numerals involve special subtraction rules like IV=4, IX=9, etc.

## Approach
- Traverse from right to left
- If a smaller numeral precedes a larger one, subtract it
- Else, add it to total

## Time and Space
- Time: O(n)
- Space: O(1)

## Java
[RomanToInteger.java](./RomanToInteger.java)

## Python
[roman-to-integer.py](./roman-to-integer.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/roman-to-integer/)
