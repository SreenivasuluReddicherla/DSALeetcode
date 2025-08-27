\# LeetCode 30: Substring with Concatenation of All Words



\## Problem

Find all starting indices in string `s` where substring is a concatenation of each word in `words` exactly once.



\## Approach

\- Use sliding window with step size equal to word length.

\- Maintain hash maps for word frequency.

\- Shift left pointer when extra words appear.



\## Time \& Space Complexity

\- Time: O(n \* word\_len)

\- Space: O(m) (number of words)



\## Solutions

\- ✅ Java: SubstringConcat.java

\- ✅ Python: substring\_concat.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)



