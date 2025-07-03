# LeetCode #380: Insert Delete GetRandom O(1)

## Problem
Design a data structure that supports `insert(val)`, `remove(val)`, and `getRandom()` in average O(1) time.

## Approach
- Use a HashMap to store value-to-index mappings
- Use an ArrayList to allow O(1) getRandom
- Swap-with-last technique used for efficient deletions

## Time and Space
- Time Complexity: O(1) average for all operations
- Space Complexity: O(n)

## Java
[RandomizedSet.java](./RandomizedSet.java)

## Python
[insert-delete-getrandom.py](./insert-delete-getrandom.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/insert-delete-getrandom-o1/)
