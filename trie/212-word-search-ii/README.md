\# LeetCode 212: Word Search II



\## 🧩 Problem

Find all words from a given list that exist in a 2D character board.  

A word can be constructed from adjacent cells (up, down, left, right) without reusing a cell.



---



\## 🧠 Example

\*\*Input\*\*

board = \[

\["o","a","a","n"],

\["e","t","a","e"],

\["i","h","k","r"],

\["i","f","l","v"]

]

words = \["oath","pea","eat","rain"]





\*\*Output\*\*





\["eat","oath"]





---



\## 💡 Approach

\- Build a \*\*Trie\*\* to store all words.

\- Start DFS from each cell in the board.

\- Explore all valid paths using \*\*backtracking\*\*.

\- Use `#` to mark visited cells temporarily.

\- When a full word is found, add to the result and mark it as used.



---



\## 🕒 Complexity

| Step | Time | Space |

|------|------|-------|

| Build Trie | O(N·L) | O(N·L) |

| DFS Search | O(M×N×4^L) worst, pruned by Trie | O(L) |



---



\## 💻 Implementations

\- ✅ Java — `WordSearchII.java`

\- ✅ Python — `word\_search\_ii.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/word-search-ii/)



---



\## 📢 LinkedIn Summary

> 🔍 LeetCode #212 – Word Search II  

> Solved using \*\*Trie + DFS backtracking\*\* for optimal prefix pruning.  

>  

> 🧠 Pattern: Trie + Backtracking  

> ⏱️ Time: O(M×N×4^L) worst | 📦 Space: O(N·L)  

>  

> ✅ Implemented in Java \& Python  

> 📁 GitHub-ready folder with README.md  

>  

> #LeetCode #Trie #DFS #Backtracking #Java #Python #100DaysOfCode

