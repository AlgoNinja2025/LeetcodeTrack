// Last updated: 7/21/2026, 7:09:36 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
         ListNode *a = headA, *b = headB;
        while (a != b) {
            a = !a ? headB : a->next;
            b = !b ? headA : b->next;
        }
        return a;
    }
};