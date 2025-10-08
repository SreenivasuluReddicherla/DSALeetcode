\# 🧮 23. Merge k Sorted Lists



\### 📂 Folder

`divide\_and\_conquer/23-merge-k-sorted-lists`



---



\### 🧠 Problem Statement

Given an array of `k` sorted linked lists, merge them into one sorted linked list and return it.



---



\### 💡 Approach 1: Divide and Conquer

\- Recursively divide the list of linked lists into halves.

\- Merge two lists at a time (like Merge Sort).

\- Time complexity: \*\*O(N log k)\*\*, where N is the total number of nodes.

\- Space complexity: \*\*O(log k)\*\* (recursion stack).



---



\### 💡 Approach 2: Min-Heap (Alternate)

\- Insert the head of each linked list into a min-heap.

\- Repeatedly extract the smallest element and push the next node from that list.

\- Time complexity: \*\*O(N log k)\*\*

\- Space complexity: \*\*O(k)\*\*



---



\### 🧩 Example

\*\*Input:\*\*



