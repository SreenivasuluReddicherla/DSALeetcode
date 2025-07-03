# LeetCode #238: Product of Array Except Self

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. Do not use division.

## Approach
- Use two passes: prefix pass and suffix pass
- First fill left-to-right product
- Then multiply by right-to-left product

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1) (excluding result array)

## Java
[ProductOfArrayExceptSelf.java](./ProductOfArrayExceptSelf.java)

## Python
[product-of-array-except-self.py](./product-of-array-except-self.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/product-of-array-except-self/)
