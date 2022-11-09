# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # if root.left and not root.right:
        #     return 1 + self.minDepth(root.left)
        # if root.right and not root.left:
        #     return 1 + self.minDepth(root.right)
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        # --------------bfs---------------
        if not root: return 0
        q = deque([root])
        level = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right: return level
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level +=1
        return level