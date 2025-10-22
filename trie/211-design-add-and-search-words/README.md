\# LeetCode 211: Design Add and Search Words Data Structure



\## 🧩 Problem

Design a data structure that supports adding words and searching for them.  

The search supports a wildcard character `.` which can match any letter.



---



\## 🧠 Example

\*\*Input\*\*

"WordDictionary","addWord","addWord","addWord","search","search","search","search"]

\[\[],\["bad"],\["dad"],\["mad"],\["pad"],\["bad"],\[".ad"],\["b.."]]



\*\*Output\*\*





\[null,null,null,null,false,true,true,true]





---



\## 💡 Approach

\- Use a \*\*Trie\*\* to store words.

\- Use \*\*DFS\*\* during search:

&nbsp; - If `.` is encountered, try all possible child nodes.

&nbsp; - Otherwise, follow the specific child for the character.



---



\## 🕒 Complexity

| Operation | Time | Space |

|------------|------|-------|

| addWord()  | O(L) | O(L) |

| search()   | O(26^d) worst, avg O(L) | O(L) |



---



\## 💻 Implementations

\- ✅ Java — `WordDictionary.java`

\- ✅ Python — `word\_dictionary.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/)



---



\## 📢 LinkedIn Summary

> 🧩 LeetCode #211 – Design Add and Search Words Data Structure  

> Implemented a \*\*Trie-based word dictionary\*\* supporting `.` wildcard searches using DFS.  

>  

> 🧠 Pattern: Trie + DFS Search  

> ⏱️ Time: O(L) for add | 📦 Space: O(L)  

>  

> ✅ Implemented in Java \& Python  

> 📁 GitHub-ready folder with README.md  

>  

> #LeetCode #Trie #DFS #Java #Python #DataStructures #100DaysOfCode

