# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        cnt = 1
        temp = head
        while temp.next:
            cnt += 1
            temp = temp.next
        temp.next = head
        k = k % cnt
        end = cnt - k  # to get end of the list
        while end:
            temp = temp.next
            end -= 1
        # breaking last node link and pointing to NULL
        head = temp.next
        temp.next = None
        return head
       