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
    def construct(self, grid):
        def construct(row, col, size):
            if size == 1:
                return Node(grid[row][col], True)

            size //= 2
            n = Node(1, False,         
                construct(row, col, size),
                construct(row, col + size, size),
                construct(row + size, col, size),
                construct(row + size, col + size, size))
            
            return Node(grid[row][col], True) if four_leaves(n) and four_equal_val(n) else n
        
        four_leaves = lambda n: n.topLeft.isLeaf and n.topRight.isLeaf and n.bottomLeft.isLeaf and n.bottomRight.isLeaf
        four_equal_val = lambda n: n.topLeft.val == n.topRight.val == n.bottomLeft.val == n.bottomRight.val
        
        return construct(0, 0, len(grid))
        