\# 207. Course Schedule



\### 🧩 Problem

You are given `numCourses` and a list of `prerequisites`, where each pair `\[a, b]` indicates that you must take course `b` before course `a`.  

Return `true` if it is possible to finish all courses, otherwise `false`.



---



\### 💡 Approach

This is a \*\*cycle detection problem in a directed graph\*\*.  

We can solve it using \*\*Topological Sorting (Kahn’s Algorithm)\*\*:



1\. Build the graph and indegree array.

2\. Use a queue to process nodes with zero indegree.

3\. Reduce indegrees of dependent courses.

4\. If all nodes are processed → no cycle → return `True`.



---



\### 🧠 Example

\*\*Input\*\*





numCourses = 2

prerequisites = \[\[1, 0]]



\*\*Output\*\*





true





\*\*Input\*\*





numCourses = 2

prerequisites = \[\[1, 0], \[0, 1]]



\*\*Output\*\*





false









---



\### 🕒 Complexity

\- \*\*Time:\*\* `O(V + E)`

\- \*\*Space:\*\* `O(V + E)`



---



\### 💻 Languages

\- \*\*Java:\*\* `CourseSchedule.java`

\- \*\*Python:\*\* `course\_schedule.py`



---



\### 🔗 LinkedIn Post Caption

> 🚀 LeetCode #207 – Course Schedule  

> Mastered Topological Sorting (Kahn’s Algorithm) to detect cycles in directed graphs!  

> Implemented in both Java and Python 🧠  

>  

> #LeetCode #GraphAlgorithms #TopologicalSort #CycleDetection #Java #Python #DSA



