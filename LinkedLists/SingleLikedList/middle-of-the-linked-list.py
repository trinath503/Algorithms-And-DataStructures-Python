# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast =head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        
        slow = fast =head
        prev_node = None
        while fast and fast.next:
            prev_node = slow
            slow = slow.next
            fast = fast.next.next
            
        if prev_node:
            prev_node.next = slow.next
            
        return head
        