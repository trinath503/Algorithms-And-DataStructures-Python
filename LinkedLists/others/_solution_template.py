"""
LINKED LISTS / OTHERS — Quick solution templates (Stack, etc.)
See: Stack.py in this folder.
"""

from typing import List, Optional

# =============================================================================
# STACK (list-based or linked-list based)
# =============================================================================
class Stack:
    def __init__(self):
        self._data: List = []

    def push(self, x) -> None:
        self._data.append(x)

    def pop(self):
        if not self._data:
            return None
        return self._data.pop()

    def peek(self):
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)


# Use stack for: valid parentheses, next greater element, DFS (iterative), undo.
