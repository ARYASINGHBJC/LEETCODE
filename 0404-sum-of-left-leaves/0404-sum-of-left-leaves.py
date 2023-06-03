# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s, ans = deque([(root, False)]), 0
        while s:
            cur, isLeft = s.pop()
            if not cur.left and not cur.right and isLeft:
                ans = ans + cur.val
            if cur.right: 
                s.append((cur.right, False))
            if cur.left: 
                s.append((cur.left, True))
        return ans
        