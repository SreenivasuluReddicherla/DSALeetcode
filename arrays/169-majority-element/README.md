# LeetCode #169: Majority Element

## Problem
Given an array `nums`, return the majority element — the element that appears more than ⌊n / 2⌋ times.

## Approach
- ✅ Use the **Boyer-Moore Voting Algorithm**
- ✅ Track a `candidate` and a `count`, resetting candidate when count is zero
- ✅ Guaranteed majority element per constraints

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1)

## Java
[MajorityElement.java](./MajorityElement.java)

## Python
[majority-element.py](./majority-element.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/majority-element/)
