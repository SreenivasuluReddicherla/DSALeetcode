# LeetCode #135: Candy

## Problem
There are `n` children with ratings. Give each child at least 1 candy. Children with a higher rating than their neighbors must get more candies.

Return the minimum candies required.

## Approach
- Greedy two-pass:
  1. Left to right → ensure increasing ratings get more candy
  2. Right to left → fix any remaining inequality

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(n)

## Java
[Candy.java](./Candy.java)

## Python
[candy.py](./candy.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/candy/)
