"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size):
            if self.is_uniform(grid, r, c, size):
                return Node(grid[r][c] == 1, True)

            new_size = size // 2
            return Node(
                True,
                False,
                build(r, c, new_size),
                build(r, c + new_size, new_size),
                build(r + new_size, c, new_size),
                build(r + new_size, c + new_size, new_size)
            )

        return build(0, 0, len(grid))

    def is_uniform(self, grid, r, c, size):
        val = grid[r][c]
        for i in range(r, r + size):
            for j in range(c, c + size):
                if grid[i][j] != val:
                    return False
        return True