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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode temp = dummy;
        int carry =0;
        while(l1 != null || l2  != null || carry != 0){
            int sm =0;
            if(l1 != null){
                sm += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                sm += l2.val;
                l2 = l2.next;
            }
            sm += carry;
            carry = sm / 10;
            ListNode temporary = new ListNode(sm%10);
            temp.next = temporary;
            temp = temp.next;
        }
        return dummy.next;
    }
}