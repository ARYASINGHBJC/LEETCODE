# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # while sys.getrefcount(head) < 5:
        #     head = head.next
        # return bool(head)
        # try:
        #     slow = head
        #     fast = head.next
        #     while slow is not fast:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return True
        # except:
        #     return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False