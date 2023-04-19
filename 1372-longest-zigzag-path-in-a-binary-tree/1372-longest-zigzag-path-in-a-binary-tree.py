# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(
            self.solve(root.left, 'left', 0),
            self.solve(root.right, 'right', 0)
        )
    
    def solve(self, root, dir_from, path_cnt):
        if not root:
            return path_cnt
        if dir_from == 'left':
            return max(
                self.solve(root.right, 'right', path_cnt + 1),
                self.solve(root.left, 'left', 0)
            )
        else:
            return max(
                self.solve(root.left, 'left', path_cnt + 1),
                self.solve(root.right, 'right', 0)
            )
# class Solution:

#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         self.pathLength = 0
        
#         def dfs(node, goLeft, steps):
#             if node:
#                 self.pathLength = max(self.pathLength, steps)
#                 if goLeft:
#                     dfs(node.left, False, steps + 1)
#                     dfs(node.right, True, 1)
#                 else:
#                     dfs(node.left, False, 1)
#                     dfs(node.right, True, steps + 1)
        
#         dfs(root, False, 0)
#         dfs(root, True, 0)
#         return self.pathLength
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        ans = 0
        nodes = [(root, False, 0), (root, True, 0)]
        while nodes:
            node, right, length = nodes.pop()
            if node:
                ans = max(ans, length)
                nodes.append((node.right if right else node.left, not right, length + 1))
                nodes.append((node.left if right else node.right, right, 1))
        return ans