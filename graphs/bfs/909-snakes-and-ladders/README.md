\# 909. Snakes and Ladders



\## 🧩 Problem

Given an `n x n` board, find the \*\*minimum number of moves\*\* to reach the last square (n²) in the \*\*Snakes and Ladders\*\* game.



Each square may contain a ladder (go up) or snake (slide down).



---



\## 💡 Approach — BFS (Shortest Path)

\- Model the board as a graph where each cell is a node.

\- Use BFS to find the minimum dice rolls needed to reach `n²`.

\- Convert between 1D cell numbers and 2D board coordinates using a helper function.



---



\## 🕒 Complexity

\- \*\*Time:\*\* O(n²)

\- \*\*Space:\*\* O(n²)



---



\## 💻 Solutions

\- ✅ Java: `SnakesAndLadders.java`

\- ✅ Python: `snakes\_and\_ladders.py`



---



\## 🧠 Example

\*\*Input\*\*

\[\[-1,-1,-1,-1,-1,-1],

\[-1,-1,-1,-1,-1,-1],

\[-1,-1,-1,-1,-1,-1],

\[-1,35,-1,-1,13,-1],

\[-1,-1,-1,-1,-1,-1],

\[-1,15,-1,-1,-1,-1]]



\*\*Output\*\*





4





---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/snakes-and-ladders/)



---



\## 📢 LinkedIn Summary

> 🎯 LeetCode #909 — Snakes and Ladders  

> Solved using \*\*BFS (Shortest Path in Graph)\*\* approach 🧠  

> Simulated dice rolls and ladder/snake jumps efficiently with 1D–2D coordinate mapping.  

>  

> 🕒 Time: O(n²) | 📦 Space: O(n²)  

> Implemented in both \*\*Java\*\* and \*\*Python\*\*.  

>  

> #LeetCode #Graph #BFS #DSA #Java #Python #100DaysOfCode

