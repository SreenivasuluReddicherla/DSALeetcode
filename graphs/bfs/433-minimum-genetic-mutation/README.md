\# 433. Minimum Genetic Mutation



\## 🧩 Problem

You are given two gene strings (`start` and `end`) and a list of valid mutations (`bank`).  

Each mutation changes \*\*exactly one character\*\* in the gene.  



Return the \*\*minimum number of mutations\*\* required to transform `start` → `end`.  

If it’s not possible, return `-1`.



---



\## 💡 Approach — BFS (Shortest Path in Graph)

\- Each gene represents a \*\*node\*\*.

\- A valid one-character mutation forms an \*\*edge\*\*.

\- Use \*\*BFS\*\* to find the minimum number of mutations.



---



\## 🧠 Example

\*\*Input\*\*

start = "AACCGGTT"

end = "AAACGGTA"

bank = \["AACCGGTA","AACCGCTA","AAACGGTA"]



\*\*Output\*\*





2





---



\## 🕒 Complexity

\- \*\*Time:\*\* O(N \* L \* 4)

\- \*\*Space:\*\* O(N)

&nbsp; - N = size of bank  

&nbsp; - L = gene length (8)



---



\## 💻 Solutions

\- ✅ Java: `MinimumGeneticMutation.java`

\- ✅ Python: `minimum\_genetic\_mutation.py`



---



\## 🔗 LeetCode

\[LeetCode Problem Link](https://leetcode.com/problems/minimum-genetic-mutation/)



---



\## 📢 LinkedIn Summary

> 🧬 LeetCode #433 – Minimum Genetic Mutation  

> Solved using \*\*BFS\*\* to find the shortest path between gene sequences.  

> Each valid mutation (1-character change) is treated as a graph edge.  

>  

> 🧠 Pattern: Graph Traversal (BFS)  

> ⏱️ Time: O(N \* L \* 4) | 📦 Space: O(N)  

>  

> ✅ Java \& Python implementations  

> 📁 Ready for GitHub with README structure  

>  

> #LeetCode #Graph #BFS #Bioinformatics #Genetics #Java #Python #100DaysOfCode

