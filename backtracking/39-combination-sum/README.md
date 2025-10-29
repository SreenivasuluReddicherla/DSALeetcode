\# LeetCode 39: Combination Sum



\## 🧩 Problem

Given distinct `candidates\[]` and a target integer `target`, find all unique combinations of `candidates` that sum to `target`.  

You can reuse each number any number of times.



---



\## 🧠 Example

\*\*Input\*\*

candidates = \[2,3,6,7], target = 7



\*\*Output\*\*





\[\[2,2,3],\[7]]





---



\## 💡 Approach

\- Use \*\*backtracking\*\* to explore every possible combination.  

\- At each recursive step:

&nbsp; - Include the current number and recurse with the reduced target.  

&nbsp; - Exclude it and move to the next number.  

\- Stop when `target == 0` (valid combination) or `target < 0`.



---



\## 🕒 Complexity

| Operation | Time | Space |

|------------|------|-------|

| Backtracking | O(2ⁿ) | O(target/min(candidates)) |



---



\## 💻 Implementations

\- ✅ Java — `CombinationSum.java`  

\- ✅ Python — `combination\_sum.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/combination-sum/)



---



\## 📢 LinkedIn Summary

> 💫 LeetCode #39 – Combination Sum  

> Solved using \*\*backtracking + pruning\*\* to find all unique combinations that sum to target.  

>  

> 🧠 Pattern: Backtracking  

> ⏱️ Time: O(2ⁿ) | 📦 Space: O(target/min(candidates))  

>  

> ✅ Java \& Python solutions  

> 📁 GitHub-ready with README.md  

>  

> #LeetCode #Backtracking #Recursion #CombinationSum #Java #Python #100DaysOfCode

