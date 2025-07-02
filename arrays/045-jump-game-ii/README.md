# LeetCode #45: Jump Game II

## Problem
Return the minimum number of jumps to reach the last index from the first index. Each element in the array represents your maximum jump length at that position.

## Approach
- Track the `farthest` point reachable in the current jump window
- Track the current `end` of the window
- Each time `i == end`, make a jump and update the window

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1)

## Java
[JumpGameII.java](./JumpGameII.java)

## Python
[jump-game-ii.py](./jump-game-ii.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/jump-game-ii/)
