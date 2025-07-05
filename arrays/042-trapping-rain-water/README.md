# LeetCode #42: Trapping Rain Water

## Problem
Given height[i] representing elevation, return the total amount of trapped rainwater.

## Approach
- Two-pointer technique
- Track `left_max` and `right_max` to calculate water at each index
- Greedy: always move smaller side inward

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1)

## Java
[TrappingRainWater.java](./TrappingRainWater.java)

## Python
[trapping-rain-water.py](./trapping-rain-water.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/trapping-rain-water/)
