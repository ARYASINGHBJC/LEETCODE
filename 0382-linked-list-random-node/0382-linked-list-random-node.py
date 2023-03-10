# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.value = []
        while head:
            self.value.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        pick = int(random.random() * len(self.value))
        return self.value[pick]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()