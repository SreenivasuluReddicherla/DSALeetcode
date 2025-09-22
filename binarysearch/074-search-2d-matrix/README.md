\# LeetCode 74: Search a 2D Matrix



\## Problem

You are given an `m x n` matrix where:

\- Each row is sorted in ascending order.

\- The first integer of each row is greater than the last integer of the previous row.  



Given a target integer, return `true` if it exists in the matrix, otherwise return `false`.



\## Approach

\- Treat the 2D matrix as a \*\*flattened sorted array\*\* of length `m \* n`.  

\- Perform \*\*binary search\*\* on this virtual array.  

\- Convert mid index to 2D:  

&nbsp; - Row = `mid // n`  

&nbsp; - Column = `mid % n`



\## Time \& Space Complexity

\- \*\*Time:\*\* O(log(m \* n))  

\- \*\*Space:\*\* O(1)



\## Example

Input:  



