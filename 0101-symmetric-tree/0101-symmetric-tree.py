# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # --------------bfs queue-----------------
        if not root: return True
        q = deque([(root.left, root.right)])
        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            q.append((left.left, right.right))
            q.append((left.right, right.left))
        return True
        
        # --------------dfs stack---------------
        # if not root: return True
        # stack = [[root.left, root.right]]
        # while stack:
        #     left, right = stack.pop()
        #     if not left and not right:
        #         continue
        #     if left and not right or not left and right:
        #         return False
        #     if left.val != right.val:
        #         return False
        #     if left.val == right.val:
        #         stack.append([left.left, right.right])
        #         stack.append([left.right, right.left])
        # return True
        
        # ------------------dfs recursion---------------
        # if not root: return True
        # def symmetric(node1, node2):
        #     if not node1 and not node2: return True
        #     if (not node1 and node2) or (node1 and not node2):
        #         return False
        #     if node1.val == node2.val:
        #         return symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)
            
        # return symmetric(root.left, root.right)