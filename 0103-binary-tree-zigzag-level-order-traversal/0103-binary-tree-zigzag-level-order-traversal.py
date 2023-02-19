# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        cur_level = [root]
        direction = 1
        
        while cur_level:
            res.append([n.val for n in cur_level][::direction])
            direction = -direction
            cur_level = [
                n 
                for node in cur_level
                for n in [node.left, node.right]
                if n is not None
            ]
        return res
        