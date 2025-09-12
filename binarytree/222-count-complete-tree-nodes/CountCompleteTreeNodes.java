# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        leftheight = height(root.left)
        rightheight = height(root.right)
        if leftheight == rightheight:
            return (1 << leftheight)+self.countNodes(root.right)
        else:
            return (1 << rightheight)+self.countNodes(root.left)