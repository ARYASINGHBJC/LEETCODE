/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        int cnt= 0;
        ListNode temp = head;
        while(temp != null){
            cnt += 1;
            temp = temp.next;
        }
        if(k <= 1 || cnt < k){
            return head;
        }
        ListNode prev = new ListNode(0);
        ListNode curr = head;
        for(int i= 0; i< k; i++){
            ListNode front = curr.next;
            curr.next = prev;
            prev = curr;
            curr = front;
        }
        head.next = reverseKGroup(curr, k);
        return prev;
    }
}