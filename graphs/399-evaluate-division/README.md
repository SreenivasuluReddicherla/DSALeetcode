\# ⚖️ LeetCode 399: Evaluate Division



\### 📂 Folder

`graph/399-evaluate-division`



---



\### 🧠 Problem Statement

You are given equations like `a / b = 2.0` and queries like `a / c = ?`.



Find the result of each query using the given equations.  

If the answer cannot be determined, return `-1.0`.



---



\### 💡 Approach: Graph + DFS

Each equation forms \*\*bidirectional edges\*\* in a graph:

\- `a → b` with weight `k`

\- `b → a` with weight `1/k`



We then use \*\*Depth-First Search (DFS)\*\* to traverse from the numerator to the denominator, multiplying edge weights along the way.



---



\### ✅ Steps

1\. Build an adjacency list representing equations.

2\. For each query `(x, y)`:

&nbsp;  - If either `x` or `y` is missing → return `-1.0`

&nbsp;  - Else perform DFS from `x` to `y`

3\. Multiply edge weights during traversal.



---



\### 🧮 Example

\*\*Input:\*\*



