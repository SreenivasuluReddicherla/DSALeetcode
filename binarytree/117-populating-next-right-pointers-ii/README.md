\# LeetCode 117: Populating Next Right Pointers in Each Node II



\## Problem

Connect each node’s `next` pointer to its right neighbor at the same level.

Unlike #116, the tree is not necessarily perfect.



\## Approach

\- Use a dummy node to connect nodes at each level in O(1) space.

\- BFS with queue also works but uses extra memory.



\## Time \& Space Complexity

\- Time: O(n) (every node visited once)

\- Space: O(1) with dummy pointer, O(n) with BFS



\## Solutions

\- ✅ Java: ConnectNextPointersII.java

\- ✅ Python: connect\_next\_pointers\_ii.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)



