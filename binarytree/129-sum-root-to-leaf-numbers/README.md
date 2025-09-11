\# LeetCode 129: Sum Root to Leaf Numbers



\## Problem

Given a binary tree with digits `0-9`, each root-to-leaf path forms a number.  

Return the sum of all such numbers.



\## Approach

\- \*\*Recursive DFS\*\*: Carry current number down the tree, add at leaf.

\- \*\*Iterative DFS\*\*: Use stack `(node, num)` to track paths.



\## Time \& Space Complexity

\- Time: O(n), every node visited once

\- Space: O(h), recursion/stack depth (h = height)



\## Solutions

\- ✅ Java: SumRootToLeaf.java

\- ✅ Python: sum\_root\_to\_leaf.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/sum-root-to-leaf-numbers/)



