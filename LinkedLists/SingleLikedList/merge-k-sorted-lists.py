# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, left, right):
        start_node = cur_node = ListNode(0)
        
        if None in (left, right):
            return left or right
        
        while left and right:
            if left.val <= right.val:
                cur_node.next = left
                left = left.next
            else:
                cur_node.next = right
                right = right.next
                
            cur_node = cur_node.next
            
        cur_node.next = left or right
        
        return start_node.next
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) //2
        
        left , right = self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left, right)
        
        
        
"""
# Solution -2

from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

"""