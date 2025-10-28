\# LeetCode 46: Permutations



\## 🧩 Problem

Given an array `nums` of distinct integers, return \*\*all possible permutations\*\*.  

Return the result in any order.



---



\## 🧠 Example

\*\*Input\*\*

nums = \[1,2,3]



\*\*Output\*\*





\[\[1,2,3],\[1,3,2],\[2,1,3],\[2,3,1],\[3,1,2],\[3,2,1]]





---



\## 💡 Approach

\- Use \*\*backtracking\*\* to build all permutations.

\- Maintain a list for the current permutation and mark used elements.

\- Once all elements are used, add the combination to results.

\- Backtrack by removing the last element and unmarking it.



---



\## 🕒 Complexity

| Operation | Time | Space |

|------------|------|-------|

| Backtracking | O(n × n!) | O(n) |



---



\## 💻 Implementations

\- ✅ Java — `Permutations.java`

\- ✅ Python — `permutations.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/permutations/)



---



\## 📢 LinkedIn Summary

> 🔄 \*\*LeetCode #46 – Permutations\*\*  

> Implemented using \*\*backtracking\*\* to generate all unique orderings of a list.  

>  

> 🧠 Pattern: Backtracking  

> ⏱️ Time: O(n × n!) | 📦 Space: O(n)  

>  

> ✅ Java \& Python solutions  

> 📁 GitHub-ready with README.md  

>  

> #LeetCode #Backtracking #Java #Python #Permutations #100DaysOfCode

