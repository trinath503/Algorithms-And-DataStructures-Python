# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
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
            
            
        