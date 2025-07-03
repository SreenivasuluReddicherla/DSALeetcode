# LeetCode #274: H-Index

## Problem
Given an array `citations`, where `citations[i]` is the number of citations for the `i-th` paper, return the researcher's H-index.

## Approach
- Sort the array in ascending order
- For each index `i`, compute `h = n - i`
- Return the highest `h` such that `citations[i] >= h`

## Time and Space
- Time Complexity: O(n log n)
- Space Complexity: O(1)

## Java
[HIndex.java](./HIndex.java)

## Python
[h-index.py](./h-index.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/h-index/)
