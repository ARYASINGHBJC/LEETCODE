# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        count = 0
        while temp:
            count += 1
            temp = temp.next
        temp = head
        mid = count//2 + 1
        while temp:
            mid -= 1
            if mid == 0:
                break
            temp = temp.next
        return temp