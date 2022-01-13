"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # Time Complexity : O(l1+l2)
        # Space Complexity : O(max(l1 or l2))
        head = dummy = ListNode(0)
        
        carry =0
        while l1 or l2 or carry:
            l1_val , l2_val = 0, 0
            
            if l1:
                l1_val = l1.val
                l1 = l1.next
                
            if l2:
                l2_val = l2.val
                l2 = l2.next
                
            # devmod -> returns tuples (x//y, x%y)
            carry, cur_num = divmod(l1_val + l2_val + carry, 10)
            dummy.next =  ListNode(cur_num)
            
            dummy = dummy.next
        
        return head.next