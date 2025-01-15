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
    static class Pair {
        ListNode newHead;
        ListNode nextGroupStart;

        Pair(ListNode newHead, ListNode nextGroupStart) {
            this.newHead = newHead;
            this.nextGroupStart = nextGroupStart;
        }
    }
    public ListNode reverseKGroup(ListNode head, int k) {
        int cnt= 0;
        ListNode temp = head;
        while(temp != null){
            cnt += 1;
            temp = temp.next;
        }
        int grp = cnt / k;
        ListNode dummy = new ListNode(0);
        ListNode prev_grp_end = dummy;
        dummy.next = head;
        ListNode curr = head;

        for(int i= 0; i < grp; i++){
            Pair reversed = reverse(curr, k);
            ListNode newHead = reversed.newHead;   // New head after reversal
            ListNode newGrpStart = reversed.nextGroupStart; // The node after the reversed group
            prev_grp_end.next = newHead;
            prev_grp_end = curr;
            curr = newGrpStart;
        }
        prev_grp_end.next = curr;
        return dummy.next;
    }
    public Pair reverse(ListNode head, int k){
        ListNode curr = head;
        ListNode prev = null;
        while(k > 0){
            ListNode front = curr.next;
            curr.next = prev;
            prev = curr;
            curr = front;
            k = k - 1;
        }
        return new Pair(prev, curr);
    }
}