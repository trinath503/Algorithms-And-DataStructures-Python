# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        
            Find the k-th node from the front.
            Find the k-th last element using two poiners method.
            Swap their values.
            Return the head of the Linked List

        """
        
        slow = fast = head
        
        for _ in range(k-1):
            fast = fast.next
            
        first = fast 
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        second = slow 
        
        second.val , first.val = first.val , second.val 
        
        
        return head 
        