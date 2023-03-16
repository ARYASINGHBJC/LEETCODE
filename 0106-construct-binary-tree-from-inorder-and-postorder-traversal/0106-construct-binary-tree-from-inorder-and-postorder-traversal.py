# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val) # Line A

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder) # Line B
        root.left = self.buildTree(inorder[:inorderIndex], postorder) # Line C

        return root