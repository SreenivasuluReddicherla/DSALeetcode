\# 🧩 133. Clone Graph



\### 📂 Folder

`graph/133-clone-graph`



---



\### 🧠 Problem Statement

You are given a \*\*reference to a node\*\* in a connected undirected graph.  

Each node has a `val` (integer) and a list of `neighbors`.



Return a \*\*deep copy\*\* (clone) of the graph.



---



\### 💡 Approach: BFS with HashMap

We perform a \*\*Breadth-First Search (BFS)\*\* traversal to visit each node once,  

while maintaining a \*\*mapping\*\* from the original node to its clone.



For each node:

1\. Clone it if not already cloned.

2\. Add clones of its neighbors to the current clone’s neighbor list.

3\. Push unvisited neighbors to the queue.



---



\### ✅ Steps

1\. Use a \*\*HashMap / Dictionary\*\* to store mapping `{original\_node → cloned\_node}`.

2\. Start BFS from the given node.

3\. Clone each neighbor and connect appropriately.

4\. Return the clone of the original input node.



---



\### 🕒 Time Complexity

\*\*O(V + E)\*\* — where V = number of vertices, E = number of edges.



\### 🧠 Space Complexity

\*\*O(V)\*\* — for storing cloned nodes and queue.



---



\### 🧩 Example

\*\*Input:\*\*



