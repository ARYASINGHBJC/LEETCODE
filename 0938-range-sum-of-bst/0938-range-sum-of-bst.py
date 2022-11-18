# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def dfs(root):
            if not root: return
            if low <= root.val <= high:
                self.res += root.val
            if root.val > low:
                dfs(root.left)
            if root.val < high:
                dfs(root.right)
        dfs(root)
        return self.res