"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dummy = Node(0)
        prev = dummy
        current = root

        while current:
            if current.left:
                prev.next = current.left
                prev = prev.next
            if current.right:
                prev.next = current.right
                prev = prev.next
            current = current.next
            if not current:
                current = dummy.next
                dummy.next = None
                prev = dummy
        return root
