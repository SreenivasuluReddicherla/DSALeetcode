\# 210. Course Schedule II



\### 🧩 Problem

You are given `numCourses` and a list of `prerequisites` where each pair `\[a, b]` means you must take course `b` before course `a`.  

Return \*\*any valid order\*\* in which you can finish all the courses.  

If it’s impossible to complete all, return an \*\*empty array\*\*.



---



\### 💡 Approach

We use \*\*Topological Sorting (Kahn’s Algorithm)\*\* to determine the correct course order.



\#### Steps:

1\. Build a graph (adjacency list) and indegree array.

2\. Push all courses with indegree 0 into a queue.

3\. Pop from the queue, add to result, and reduce indegrees of dependent courses.

4\. If all courses are processed → return order; else → return empty array.



---



\### 🧠 Example

\*\*Input\*\*

numCourses = 4

prerequisites = \[\[1,0],\[2,0],\[3,1],\[3,2]]



\*\*Output\*\*





\[0,2,1,3]





---



\### 🕒 Complexity

\- \*\*Time:\*\* O(V + E)

\- \*\*Space:\*\* O(V + E)



---



\### 💻 Languages

\- \*\*Java:\*\* `CourseScheduleII.java`

\- \*\*Python:\*\* `course\_schedule\_ii.py`



---



\### 🔗 LinkedIn Post Caption

> 🚀 LeetCode #210 – Course Schedule II  

> Implemented \*\*Topological Sorting\*\* using Kahn’s Algorithm to generate a valid course order.  

> Solved in both Java and Python. 🧠  

>  

> #LeetCode #GraphAlgorithms #TopologicalSort #CycleDetection #Java #Python #DSA

