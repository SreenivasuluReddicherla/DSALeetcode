# LeetCode #121: Best Time to Buy and Sell Stock

## Problem
Given an array where each element represents the stock price on that day, find the max profit you can achieve by choosing a day to buy and a different day to sell.

## Approach
- Track the minimum price so far (`min_price`)
- For each price, calculate profit: `price - min_price`
- Keep updating the max profit

## Time and Space
- Time Complexity: O(n)
- Space Complexity: O(1)

## Java
[BestTimeToBuyAndSellStock.java](./BestTimeToBuyAndSellStock.java)

## Python
[best-time-to-buy-and-sell-stock.py](./best-time-to-buy-and-sell-stock.py)

## Link
[LeetCode Problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
