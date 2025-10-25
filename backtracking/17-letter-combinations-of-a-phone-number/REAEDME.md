\# LeetCode 17: Letter Combinations of a Phone Number



\## 🧩 Problem

Given a string containing digits from 2–9, return all possible letter combinations that the number could represent.



---



\## 🧠 Example

\*\*Input\*\*

digits = "23"



\*\*Output\*\*





\["ad","ae","af","bd","be","bf","cd","ce","cf"]





---



\## 💡 Approach

Use \*\*backtracking\*\*:

1\. Maintain a map of digits → letters.

2\. For each digit, iterate over its letters.

3\. Use recursion to build all valid letter paths.

4\. Add completed strings to the result list.



---



\## 🕒 Complexity

| Operation | Time | Space |

|------------|------|-------|

| Backtracking | O(3ⁿ × 4ᵐ) | O(n) |



Where `n` = digits with 3 options and `m` = digits with 4 options.



---



\## 💻 Implementations

\- ✅ Java — `LetterCombinations.java`

\- ✅ Python — `letter\_combinations.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)



---



\## 📢 LinkedIn Summary

> ☎️ LeetCode #17 – Letter Combinations of a Phone Number  

> Solved using elegant \*\*backtracking\*\* to explore all digit-letter combinations efficiently.  

>  

> 🧠 Pattern: Backtracking  

> ⏱️ Time: O(3ⁿ × 4ᵐ) | 📦 Space: O(n)  

>  

> ✅ Implemented in Java \& Python  

> 📁 GitHub-ready folder with README.md  

>  

> #LeetCode #Backtracking #Java #Python #Recursion #100DaysOfCode

