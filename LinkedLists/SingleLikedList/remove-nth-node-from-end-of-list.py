# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        
        """
            L = [1,2,3,4,5]
            N = 6 
            They will be equal when slow (start->K) == fast(k->N)
        """
        slow = fast = head 
        
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next 
            slow = slow.next
        
        
        slow.next = slow.next.next
        return head
        
        
# solution -2 
#         if not head.next:
#             return None
        
        
#         total_nodes = 0
        
#         list_node = head
#         find_node = head
#         while list_node:
#             list_node = list_node.next
#             total_nodes +=1
            
#         remove_node_index = total_nodes-n
#         prev_node = None
#         print(total_nodes, remove_node_index )
#         if remove_node_index == 0:
#             return head.next
#         while find_node:
#             if not remove_node_index and prev_node:
#                 prev_node.next = find_node.next
#             prev_node = find_node
#             find_node = find_node.next
#             remove_node_index -=1
        
#         return head