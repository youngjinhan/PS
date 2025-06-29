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
    public ListNode mergeNodes(ListNode head) {
        ListNode answer = null;
        ListNode ans = answer;
        ListNode cur = head;
        int s = 0;
        while (cur.next != null) {
            cur = cur.next;
            if (cur.val == 0) {
                if (ans == null) {
                    answer = new ListNode(s);
                    ans = answer;
                } else {
                    ans.next = new ListNode(s);
                    ans = ans.next;
                }
                s = 0;
                continue;
            }
            s += cur.val;
        }

        return answer;
    }
}