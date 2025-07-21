\# LeetCode #139: Word Break



\## Problem

Given a string and a dictionary, determine if the string can be segmented into a space-separated sequence of dictionary words.



\## Approach

\- Use Dynamic Programming

\- dp\[i] = true if s\[0...i-1] can be broken using dictionary

\- Use nested loop to check all substrings ending at i



\## Time and Space

\- Time: O(n²)

\- Space: O(n)



\## Java

\[WordBreak.java](./WordBreak.java)



\## Python

\[word\_break.py](./word\_break.py)



\## Link

\[LeetCode Problem](https://leetcode.com/problems/word-break/)



