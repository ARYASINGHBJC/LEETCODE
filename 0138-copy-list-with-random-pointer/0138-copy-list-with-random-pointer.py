"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        copiedRef = {}
        curr = head
        while curr:
            copiedRef[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            getNode = copiedRef[curr]
            getNode.next = copiedRef.get(curr.next)
            getNode.random = copiedRef.get(curr.random)
            curr = curr.next
        return copiedRef[head]