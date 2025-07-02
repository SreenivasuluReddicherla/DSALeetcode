# LeetCode #55: Jump Game

## Problem
Given an array `nums` where each element represents your maximum jump length from that position, determine if you can reach the last index.

## Approach
- Use a greedy strategy to keep track of the furthest reachable index
- If you ever find that `i > reachable`, you're stuck → return False
- Else, if the loop finishes → return True

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1)

## Java
[JumpGame.java](./JumpGame.java)

## Python
[jump-game.py](./jump-game.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/jump-game/)
