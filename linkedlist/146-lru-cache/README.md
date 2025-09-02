\# LeetCode 146: LRU Cache



\## Problem

Design a data structure that follows the \*\*Least Recently Used (LRU) cache\*\* policy.



\- `get(key)`: Return value if key exists, else -1.

\- `put(key, value)`: Insert/update key-value. If capacity exceeded, evict least recently used.



\## Approach

\- Use \*\*HashMap\*\* for O(1) key-node lookup.

\- Use \*\*Doubly Linked List\*\* for maintaining usage order.

&nbsp; - Head = most recently used

&nbsp; - Tail = least recently used

\- On `get`/`put`, move accessed/updated node to head.

\- If capacity exceeded, remove tail node.



\## Time \& Space Complexity

\- Time: O(1) for both `get` and `put`

\- Space: O(capacity)



\## Solutions

\- ✅ Java: LRUCache.java

\- ✅ Python: lru\_cache.py



\## LeetCode

\[Link to Problem](https://leetcode.com/problems/lru-cache/)



