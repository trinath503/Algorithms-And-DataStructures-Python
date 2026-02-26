"""
SINGLY LINKED LIST — Quick solution templates (this folder)
See: ReverseList, middle-of-the-linked-list, remove-nth-node-from-end, merge-two-sorted, Add two numbers, merge-k-sorted-lists.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# REVERSE
def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


# MIDDLE (fast & slow)
def middle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# REMOVE NTH FROM END (dummy + fast ahead by n+1)
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow, fast = slow.next, fast.next
    slow.next = slow.next.next
    return dummy.next


# MERGE TWO SORTED
def merge_two(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


# ADD TWO NUMBERS (carry)
def add_two(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        v = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        carry, v = v // 10, v % 10
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


# MERGE K SORTED (heap of (val, list_index, node) or divide-and-conquer merge)
# Use: import heapq; heap = []; push first node of each list; pop min, append to result, push next.
