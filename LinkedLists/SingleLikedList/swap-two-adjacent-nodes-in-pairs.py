# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # case empty 
        # case: even
        # case: odd
        
        if not head or not head.next:
            return head

        result =  ListNode(0)
        result.next = head
        previous_node = result
        
        while previous_node.next and previous_node.next.next:
            
            first = previous_node.next
            second = previous_node.next.next 
            
            previous_node.next = second
            first.next = second.next 
            second.next = first 
            
            previous_node = previous_node.next.next
            
        return result.next
    