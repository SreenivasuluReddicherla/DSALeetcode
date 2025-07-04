# LeetCode #134: Gas Station

## Problem
There are `n` gas stations arranged in a circle. Each has gas[i] and cost[i]. Return the index of the gas station to start from and complete a full circle, or -1 if not possible.

## Approach
- Track total gas vs total cost (to determine feasibility)
- Greedy local `tank` check: reset start point when tank drops below 0

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1)

## Java
[GasStation.java](./GasStation.java)

## Python
[gas-station.py](./gas-station.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/gas-station/)
