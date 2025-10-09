\# 🌊 200. Number of Islands



\### 📂 Folder

`graph/200-number-of-islands`



---



\### 🧠 Problem Statement

Given an `m x n` 2D binary grid representing a map of `'1'`s (land) and `'0'`s (water),  

return the number of \*\*islands\*\*.



An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.



---



\### 💡 Approach: Depth-First Search (DFS)

\- Traverse each cell in the grid.

\- When `'1'` (land) is found, perform DFS to mark all connected lands as visited.

\- Increment island count each time a new unvisited land is found.



\#### ✅ Steps

1\. Iterate through the entire grid.  

2\. If a cell is `'1'`, trigger a DFS from that cell.  

3\. DFS marks all connected `'1'`s as `'0'`.  

4\. Count the number of DFS calls made → number of islands.



---



\### 🕒 Time Complexity

\*\*O(m × n)\*\* — each cell is visited once.  

\### 🧠 Space Complexity

\*\*O(m × n)\*\* — recursion stack for DFS (in worst case, all land).



---



\### 🧩 Example

\*\*Input:\*\*



