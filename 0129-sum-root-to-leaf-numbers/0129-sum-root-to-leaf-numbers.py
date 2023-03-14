# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        tot_sum, cur, depth = 0, 0, 0
        while root:
            if root.left:
                pre, depth = root.left, 1
                while pre.right and pre.right != root:
                    pre, depth = pre.right, depth + 1
                if not pre.right:
                    pre.right = root
                    cur = cur * 10 + root.val
                    root = root.left
                else:
                    pre.right = None
                    if not pre.left: tot_sum += cur
                    cur //= 10**depth
                    root = root.right
            else:
                cur = cur * 10 + root.val
                if not root.right: tot_sum += cur
                root = root.right
        return tot_sum