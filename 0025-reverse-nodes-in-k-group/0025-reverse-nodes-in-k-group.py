# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l, temp = 0, head
        while temp:
            l += 1
            temp = temp.next
        if k <= 1 or l < k:
            return head
        prev, curr = None, head
        for i in range(k):
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        head.next = self.reverseKGroup(curr, k)
        return prev