# iteratively

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        start = curr =  ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:

                curr.next = l1
                l1 = l1.next

            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 or l2 

        return start.next



# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# in-place, iteratively        
# def mergeTwoLists(self, l1, l2):
#     if None in (l1, l2):
#         return l1 or l2
#     dummy = cur = ListNode(0)
#     dummy.next = l1
#     while l1 and l2:
#         if l1.val < l2.val:
#             l1 = l1.next
#         else:
#             nxt = cur.next
#             cur.next = l2
#             tmp = l2.next
#             l2.next = nxt
#             l2 = tmp
#         cur = cur.next
#     cur.next = l1 or l2
#     return dummy.next