"""
DOUBLY LINKED LIST — Quick solution templates (this folder)
See: DoubleLinkedList.py, flatten-a-multilevel-doubly-linked-list, flattening-a-linked-list.
"""

from typing import Optional

class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child  # multilevel


# =============================================================================
# FLATTEN MULTILEVEL DOUBLY LINKED LIST (child → next, then continue)
# =============================================================================
def flatten(head: Optional[DoublyListNode]) -> Optional[DoublyListNode]:
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


# =============================================================================
# BASIC DOUBLY NODE INSERT / DELETE (for reference)
# =============================================================================
def insert_after(node: DoublyListNode, val: int) -> DoublyListNode:
    new_node = DoublyListNode(val, prev=node, next=node.next)
    if node.next:
        node.next.prev = new_node
    node.next = new_node
    return new_node
