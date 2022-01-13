# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        """
        If two linked lists have intersection, we can find two observations:

            They must have same nodes after the intersection point.
            L1+L2 must have same tail from the intersection point as L2 + L1. For example,

        L1 = 1,2,3
        L2 = 6,5,2,3

        L1+L2 = 1,2,3,6,5,2,3
        L2+L1 = 6,5,2,3,1,2,3
        
        """
        
        if headA == None or headB== None:
            return None
        
        if headA == headB:
            return headA
        
        first_list = headA
        second_list = headB
        
        while first_list is not second_list:
            # print('A ->', first_list)
            # print('B->', second_list)
            # print('\n')
            first_list = first_list.next if first_list else headB
            second_list = second_list.next if second_list else headA
            
        
        return first_list
            
            
        