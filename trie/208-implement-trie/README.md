\# LeetCode 208: Implement Trie (Prefix Tree)



\## 🧩 Problem

Implement a Trie (Prefix Tree) supporting the following operations:

\- `insert(word)`

\- `search(word)`

\- `startsWith(prefix)`



---



\## 🧠 Example

\*\*Input\*\*

\["Trie", "insert", "search", "search", "startsWith", "insert", "search"]

\[\[], \["apple"], \["apple"], \["app"], \["app"], \["app"], \["app"]]





\*\*Output\*\*





\[null, null, true, false, true, null, true]





---



\## 💡 Approach

\- Each node maintains:

&nbsp; - `children`: an array of 26 TrieNodes (for 'a'–'z')

&nbsp; - `isEnd`: marks if a word ends here

\- Traverse characters sequentially for each operation.



---



\## 🕒 Complexity

| Operation | Time | Space |

|------------|------|-------|

| Insert     | O(L) | O(L) |

| Search     | O(L) | O(1) |

| StartsWith | O(L) | O(1) |



Where `L` = length of the word/prefix.



---



\## 💻 Implementations

\- ✅ Java — `ImplementTrie.java`

\- ✅ Python — `implement\_trie.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/implement-trie-prefix-tree/)



---





