"""
LINKED LISTS — Quick solution templates (FAANG quick reference)
Singly: SingleLikedList/*.py  |  Doubly: DoubleLikedList/*.py  |  Stack: others/Stack.py
"""

from typing import Optional

# =============================================================================
# SINGLY LINKED LIST NODE
# =============================================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# =============================================================================
# 1. REVERSE LINKED LIST (iterative)
# Time: O(n)  Space: O(1)
# =============================================================================
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


# =============================================================================
# 2. FAST & SLOW — middle, cycle, nth from end
# Time: O(n)  Space: O(1)
# =============================================================================
def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next


# =============================================================================
# 3. MERGE TWO SORTED LISTS
# =============================================================================
def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


# =============================================================================
# 4. ADD TWO NUMBERS (digits in reverse)
# =============================================================================
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        v = carry
        if l1:
            v += l1.val
            l1 = l1.next
        if l2:
            v += l2.val
            l2 = l2.next
        carry, v = v // 10, v % 10
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


# =============================================================================
# DOUBLY LINKED LIST NODE (for DoubleLikedList folder)
# =============================================================================
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child  # for flatten

def flatten_doubly_list(head: Optional[DoublyListNode]) -> Optional[DoublyListNode]:
    """Flatten multilevel doubly linked list: recurse on child, then stitch."""
    if not head:
        return None
    cur = head
    while cur:
        if cur.child:
            nxt = cur.next
            cur.next = cur.child
            cur.child.prev = cur
            tail = cur.child
            while tail.next:
                tail = tail.next
            tail.next = nxt
            if nxt:
                nxt.prev = tail
            cur.child = None
        cur = cur.next
    return head
