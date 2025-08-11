\# LeetCode 71: Simplify Path



\## Problem

Given an absolute Unix-style file path, simplify it to its canonical form.



\## Approach

\- Split the path by '/' and iterate over each part.

\- Use a \*\*stack\*\* to simulate directory navigation:

&nbsp; - Ignore `""` and `"."` (current directory).

&nbsp; - Pop for `".."` (parent directory).

&nbsp; - Push valid folder names.

\- Join stack contents with `/`.



\## Time \& Space Complexity

\- Time: O(n)

\- Space: O(n)



\## Solutions

\- ✅ Java: SimplifyPath.java

\- ✅ Python: simplify\_path.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/simplify-path/)



