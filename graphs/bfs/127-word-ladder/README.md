\# LeetCode 127: Word Ladder



\## 🧩 Problem

Given two words (`beginWord` and `endWord`) and a word list, find the \*\*length of the shortest transformation sequence\*\* from `beginWord` to `endWord`.



Each transformation must:

1\. Change only one letter.

2\. Produce a valid word from the word list.



If no sequence exists, return 0.



---



\## 💡 Approach — BFS (Shortest Path)

\- Each word is a node.

\- A one-letter change creates an edge.

\- Use \*\*Breadth-First Search (BFS)\*\* to find the shortest transformation path.



---



\## 🧠 Example

\*\*Input\*\*

beginWord = "hit"

endWord = "cog"

wordList = \["hot","dot","dog","lot","log","cog"]



\*\*Output\*\*





5



\*\*Explanation\*\*

`hit → hot → dot → dog → cog`



---



\## 🕒 Complexity

\- \*\*Time:\*\* O(N \* L²)

\- \*\*Space:\*\* O(N \* L)



---



\## 💻 Solutions

\- ✅ Java: `WordLadder.java`

\- ✅ Python: `word\_ladder.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/word-ladder/)



---



\## 📢 LinkedIn Summary

> 🪜 LeetCode #127 – Word Ladder  

> Solved using \*\*BFS\*\* to find the shortest transformation path between words.  

> Each valid one-character change represents a graph edge.  

>  

> 🧠 Pattern: Graph + BFS  

> ⏱️ Time: O(N \* L²) | 📦 Space: O(N \* L)  

>  

> ✅ Implemented in Java \& Python  

> 📁 GitHub-ready with clean README.md  

>  

> #LeetCode #Graph #BFS #Java #Python #WordLadder #100DaysOfCode

