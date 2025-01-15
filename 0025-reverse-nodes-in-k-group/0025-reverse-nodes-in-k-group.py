# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, cnt):
        """
        Reverse `cnt` nodes starting from `head` and return the new head and tail of the reversed segment.
        """
        curr = head
        prev = None
        while cnt > 0:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
            cnt -= 1
        # `prev` is the new head, `curr` is the first node after the reversed segment
        return prev, curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes in k-group and return the modified list.
        """
        # Calculate the total number of nodes in the list
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        
        # Determine the number of complete groups
        grp_cnt = cnt // k

        # Use a dummy node to simplify edge case handling
        dummy = prev_group_end = ListNode(0)
        dummy.next = head
        curr = head

        for _ in range(grp_cnt):
            # Reverse the current group of k nodes
            new_head, next_group_start = self.reverse(curr, k)

            # Update connections for the reversed group
            prev_group_end.next = new_head
            prev_group_end = curr

            # Move to the next group
            curr = next_group_start

        # Remaining nodes (less than k) are already connected
        prev_group_end.next = curr
        return dummy.next
