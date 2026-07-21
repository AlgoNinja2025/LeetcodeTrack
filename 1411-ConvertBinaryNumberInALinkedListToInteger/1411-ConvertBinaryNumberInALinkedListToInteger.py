# Last updated: 7/21/2026, 7:08:53 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
         
        if head == 0:
            return 0
        else:
            decimal_value = 0
            current = head
            while current:
                decimal_value = (decimal_value * 2) + current.val
                current = current.next

        return decimal_value