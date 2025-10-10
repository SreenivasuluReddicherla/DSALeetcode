\# 🏰 130. Surrounded Regions



\### 📂 Folder

`graph/130-surrounded-regions`



---



\### 🧠 Problem Statement

You are given an `m x n` matrix `board` containing `'X'` and `'O'`.



Capture all regions surrounded by `'X'` by flipping all `'O'`s in that region to `'X'`.



\*\*A region is captured if it is surrounded by `'X'` on all sides (not touching the border).\*\*



---



\### 💡 Approach: Depth-First Search (DFS)

The idea is to:

1\. \*\*Mark all border-connected `'O'`s\*\* as safe (temporary `'S'`).

2\. \*\*Convert all remaining `'O'`s\*\* to `'X'` (since they are surrounded).

3\. \*\*Restore `'S'` → `'O'`\*\* to keep the border-connected regions.



---



\### ✅ Steps

1\. Traverse the \*\*borders\*\* and start DFS from every `'O'` found.  

2\. During DFS, mark all connected `'O'`s as `'S'` (safe).  

3\. After DFS:

&nbsp;  - Convert remaining `'O'` → `'X'`

&nbsp;  - Convert `'S'` → `'O'`



---



\### 🕒 Time Complexity

\*\*O(m × n)\*\* — each cell is visited once.



\### 🧠 Space Complexity

\*\*O(m × n)\*\* — recursion stack in worst case (DFS).



---



\### 🧩 Example

\*\*Input:\*\*



