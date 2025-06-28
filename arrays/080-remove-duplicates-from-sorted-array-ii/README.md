# LeetCode #80: Remove Duplicates from Sorted Array II

## Problem
Given a sorted array, remove duplicates in-place such that each element appears at most twice and return the new length.

## Approach
- Use a pointer `i` to track the next valid position
- Only place the element if it's not the same as the element at `i-2`
- Time Complexity: O(n)
- Space Complexity: O(1)

## Java
[RemoveDuplicatesSortedArrayII.java](./RemoveDuplicatesSortedArrayII.java)

## Python
[remove-duplicates-sorted-array-ii.py](./remove-duplicates-sorted-array-ii.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
