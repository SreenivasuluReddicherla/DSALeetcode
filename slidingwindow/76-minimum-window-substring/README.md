\# LeetCode 76: Minimum Window Substring



\## Problem

Find the minimum window substring of `s` that contains all characters of `t`.  

If none exists, return an empty string.



\## Approach

\- Use sliding window with two hash maps (or counters).  

\- Expand the right pointer until all characters of `t` are satisfied.  

\- Contract the left pointer to minimize window size while keeping validity.  



\## Time \& Space Complexity

\- Time: O(m + n)  

\- Space: O(m + n)  



\## Solutions

\- ✅ Java: MinimumWindowSubstring.java  

\- ✅ Python: minimum\_window\_substring.py  



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/minimum-window-substring/)



