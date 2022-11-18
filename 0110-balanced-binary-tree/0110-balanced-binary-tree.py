# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def check(root):
            if not root:
                return 0
            left, right = check(root.left), check(root.right)
            if abs(right - left) > 1:
                self.bal = False
            return 1 + max(left, right)
        check(root)
        return self.bal