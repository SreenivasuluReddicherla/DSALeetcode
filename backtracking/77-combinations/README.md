\# LeetCode 77: Combinations



\## 🧩 Problem

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from `\[1, n]`.



---



\## 🧠 Example

\*\*Input\*\*

n = 4, k = 2



\*\*Output\*\*





\[\[1,2],\[1,3],\[1,4],\[2,3],\[2,4],\[3,4]]





---



\## 💡 Approach

\- Use \*\*backtracking\*\* to explore all valid subsets of size `k`.

\- At each step, choose one number and recursively explore further.

\- Use pruning: stop exploring when remaining numbers are insufficient.



---



\## 🕒 Complexity

| Operation | Time | Space |

|------------|------|-------|

| Backtracking | O(C(n, k)) | O(k) |



---



\## 💻 Implementations

\- ✅ Java — `Combinations.java`

\- ✅ Python — `combinations.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/combinations/)



---



\## 📢 LinkedIn Summary

> 🧮 LeetCode #77 – Combinations  

> Solved using \*\*backtracking\*\* with pruning optimization to generate all unique combinations efficiently.  

>  

> 🧠 Pattern: Backtracking  

> ⏱️ Time: O(C(n, k)) | 📦 Space: O(k)  

>  

> ✅ Implemented in Java \& Python  

> 📁 GitHub-ready folder with README.md  

>  

> #LeetCode #Backtracking #Combinations #Java #Python #100DaysOfCode

