\# LeetCode 49: Group Anagrams



\## Problem

Group strings that are anagrams of each other. Two strings are anagrams if they contain the same characters with the same frequencies.



\## Approach

\- Sort each string and use the sorted string as a key in a hashmap.

\- Group original strings under this key.

\- Return all grouped values.



\## Time \& Space Complexity

\- Time: O(n × k log k), where k = max length of a string

\- Space: O(n × k)



\## Solutions

\- ✅ Java: GroupAnagrams.java

\- ✅ Python: group\_anagrams.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/group-anagrams/)



