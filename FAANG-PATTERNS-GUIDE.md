Here is a cleaner and more polished rephrased version:

---

# FAANG Interview Patterns – Quick Recognition Guide

Use this guide when solving problems: identify the **key clues**, map them to the correct **pattern**, and apply the appropriate approach.
Practice examples are referenced from this repository.

---

## 1. Two Pointers

| When to Use                        | Common Clues                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------ |
| **Sorted arrays or pair problems** | “Two numbers that sum to X”, “pair with target”, “remove duplicates in sorted array” |
| **Palindrome / symmetry checks**   | “Check palindrome”, “valid palindrome”, “reverse”                                    |
| **Partitioning elements**          | “Move zeros to end”, “partition array”, “Dutch national flag”                        |

**Time Complexity:** O(n)
**Practice Files:** `Arrays/two_sum.py`, `Arrays/Unique Triplets.py`, `Strings/valid-palindrome-i.py`, `Strings/valid-palindrome-ii.py`

---

## 2. Sliding Window (Fixed or Variable)

| When to Use                       | Common Clues                                                               |
| --------------------------------- | -------------------------------------------------------------------------- |
| **Subarray / substring problems** | “Longest substring with K distinct”, “max sum of size K”, “minimum window” |
| **Contiguous sequences**          | “Contiguous subarray”, “consecutive elements”, “window”                    |
| **Range-based constraints**       | “At most K”, “no more than K”, “every subarray of size K”                  |

**Time Complexity:** O(n)
**Practice Files:** `Arrays/longestSubstring.py`, `Arrays/sliding-window-maximum.py`, `Arrays/distinct-numbers-in-each-subarray.py`, `Strings/longest-substring-given-string-containing-distinct-characters.py`

---

## 3. Binary Search (Including Binary Search on Answer)

| When to Use               | Common Clues                                                        |
| ------------------------- | ------------------------------------------------------------------- |
| **Sorted data**           | “Sorted array”, “search in log time”, “find element”                |
| **Min/Max optimization**  | “Minimum capacity”, “smallest/largest X such that…”, “Kth smallest” |
| **Rotated sorted arrays** | “Rotated sorted array”, “find pivot”                                |

**Time Complexity:** O(log n)
**Practice Files:** `Arrays/binary_search.py`, `Arrays/search-in-rotated-sorted-array.py`, `backtracking/from bisect import bisect.py`

---

## 4. Fast & Slow Pointers (Linked Lists)

| When to Use                | Common Clues                          |
| -------------------------- | ------------------------------------- |
| **Cycle detection**        | “Cycle in linked list”, “detect loop” |
| **Middle or Nth from end** | “Middle of list”, “Nth node from end” |
| **Palindrome linked list** | “Check if linked list is palindrome”  |

**Time Complexity:** O(n)
**Practice Files:** `LinkedLists/SingleLikedList/middle-of-the-linked-list.py`, `LinkedLists/SingleLikedList/remove-nth-node-from-end-of-list.py`

---

## 5. Merge Intervals

| When to Use             | Common Clues                                                      |
| ----------------------- | ----------------------------------------------------------------- |
| **Overlapping ranges**  | “Merge intervals”, “insert interval”, “non-overlapping intervals” |
| **Scheduling problems** | “Meeting rooms”, “events”, “conflicts”                            |
| **Coverage problems**   | “Minimum arrows”, “erase overlapping intervals”                   |

**Time Complexity:** Typically O(n log n)
**Practice Files:** `Heaps/PriorityQueues/maximum-number-of-events-that-can-be-attended.py`, `Arrays/maximum-number-of-events-that-can-be-attended.py`

---

## 6. Cyclic Sort (Array Range 1..n or 0..n-1)

| When to Use                      | Common Clues                                                   |
| -------------------------------- | -------------------------------------------------------------- |
| **Numbers in fixed range**       | “Find missing number”, “find duplicate”, “numbers from 1 to n” |
| **In-place sorting requirement** | “Sort in place”, “O(1) extra space”                            |

**Time Complexity:** O(n)
**Concept:** Place each number at index `value - 1` using swaps.

---

## 7. Top K Elements (Heap)

| When to Use                     | Common Clues                                     |
| ------------------------------- | ------------------------------------------------ |
| **K largest/smallest problems** | “Top K”, “K most frequent”, “K closest elements” |
| **Order not strictly required** | “Any K elements”, “Kth largest”                  |
| **Streaming data**              | “Kth largest in stream”, “median of stream”      |

**Time Complexity:** O(n log k) or O(n log n)
**Practice Files:** `Arrays/top-k-elements.py`, `Heaps/`, `Heaps/PriorityQueues/`, `Heaps/MinHeap/`

---

## 8. BFS / DFS (Trees & Graphs)

| When to Use                                   | Common Clues                                              |
| --------------------------------------------- | --------------------------------------------------------- |
| **Level-order or shortest path (unweighted)** | “Level order traversal”, “shortest path”, “minimum steps” |
| **Full traversal / connectivity**             | “Connected components”, “islands”, “visit all nodes”      |
| **Tree paths / structure problems**           | “Path sum”, “serialize tree”, “construct tree”            |

**Time Complexity:** O(V + E) or O(n) for trees
**Practice Files:** `Graphs/BFS - Recursion.py`, `Graphs/DFS - Recursion.py`, `Trees/`, `Matrix/NumberOfIslands.py`, `Arrays/number-of-islands.py`, `Trees/path-sum-fromroot-to-leaf.py`, `Trees/serialize-and-deserialize-binary-tree.py`

---

## 9. Dynamic Programming (DP)

| When to Use                 | Common Clues                                                   |
| --------------------------- | -------------------------------------------------------------- |
| **Optimization problems**   | “Maximum”, “minimum”, “longest”, “shortest”                    |
| **Decision-based problems** | “Choose or skip”, “take or not take”                           |
| **Overlapping subproblems** | “Number of ways”, “count”, “how many”                          |
| **Classic patterns**        | Knapsack, LIS, LCS, Coin Change, Climbing Stairs, House Robber |

**Time Complexity:** O(n) to O(n²) (or more depending on state space)
**Practice Files:** `Dynamic-Programming/`, `Arrays/longest-increasing-subsequence.py`, `Arrays/maximum-subarray.py`, `Arrays/maximal-square.py`, `Arrays/maximal-rectangle.py`

---

## 10. Backtracking

| When to Use                    | Common Clues                                                |
| ------------------------------ | ----------------------------------------------------------- |
| **Generate all possibilities** | “All possible combinations”, “generate permutations”        |
| **Constraint-based problems**  | “No duplicates”, “use each element once”, “valid placement” |
| **Step-by-step construction**  | “N-Queens”, “subset generation”, “combination sum”          |

**Time Complexity:** Often exponential
**Practice Files:** `backtracking/combination-sum.py`, `backtracking/combination-sum-ii (unique sub array results).py`

---

## 11. Monotonic Stack

| When to Use                      | Common Clues                                     |
| -------------------------------- | ------------------------------------------------ |
| **Next greater/smaller element** | “Next greater element”, “daily temperatures”     |
| **Area problems**                | “Largest rectangle in histogram”, “maximum area” |
| **Span/range queries**           | “Stock span”, “previous smaller element”         |

**Time Complexity:** O(n)
**Practice Files:** `Arrays/sliding-window-maximum.py`, `Arrays/maximal-rectangle.py`

---

## 12. Hashing / Frequency Map

| When to Use                 | Common Clues                                 |
| --------------------------- | -------------------------------------------- |
| **Counting occurrences**    | “Frequency”, “count occurrences”, “anagram”  |
| **Fast lookup requirement** | “Find in O(1)”, “check existence”, “two sum” |
| **Uniqueness checks**       | “First non-repeating”, “unique”, “duplicate” |

**Time Complexity:** O(n) average
**Practice Files:** `Arrays/two_sum.py`, `Strings/Anagrams.py`, `Hashing/`, `Miscs/LRU Cache.py`

---

## 13. Bit Manipulation

| When to Use                 | Common Clues                             |
| --------------------------- | ---------------------------------------- |
| **Single element problems** | “Element appears once”, “missing number” |
| **Binary logic**            | “Bits”, “XOR”, “power of two”            |

**Time Complexity:** O(n)
**Practice Files:** `Bitwise/find-the-element-that-appears-once.py`

---

## 14. Graph Algorithms (BFS, DFS, Topological Sort, Union-Find)

| When to Use                 | Common Clues                                         |
| --------------------------- | ---------------------------------------------------- |
| **Dependencies / ordering** | “Course schedule”, “task ordering”, “before/after”   |
| **Connected components**    | “Number of islands”, “connected graph”, “union find” |
| **Shortest path problems**  | Unweighted → BFS; Weighted → Dijkstra                |

**Practice Files:** `Graphs/`, `Matrix/NumberOfIslands.py`, `Graphs/evaluate-division.py`

---

# Quick Decision Flow

1. **Sorted array or pair problem?** → Two Pointers / Binary Search
2. **Subarray / substring / contiguous range?** → Sliding Window
3. **Linked list cycle or middle element?** → Fast & Slow Pointers
4. **Intervals or scheduling?** → Merge Intervals
5. **Top K or Kth largest?** → Heap
6. **Tree/graph traversal or shortest path?** → BFS / DFS
7. **Optimization + overlapping subproblems?** → Dynamic Programming
8. **Generate all valid combinations?** → Backtracking
9. **Next greater element or histogram area?** → Monotonic Stack
10. **Counting or O(1) lookups?** → Hashing

---

# One-Line Cheat Sheet

| Clue Words                              | Pattern                  |
| --------------------------------------- | ------------------------ |
| Sum, pair, sorted, palindrome           | Two Pointers             |
| Subarray, substring, window, contiguous | Sliding Window           |
| Sorted, search, min/max capacity        | Binary Search            |
| Cycle, middle, Nth from end             | Fast & Slow Pointers     |
| Intervals, meetings, overlap            | Merge Intervals          |
| 1..n array, missing/duplicate           | Cyclic Sort              |
| Top K, Kth, most frequent               | Heap                     |
| Level order, shortest path, islands     | BFS / DFS                |
| Max/min/count ways, choices             | Dynamic Programming      |
| All combinations, place/choose          | Backtracking             |
| Next greater, histogram, span           | Monotonic Stack          |
| Count, frequency, anagram, O(1) lookup  | Hashing                  |
| Appears once, XOR, bits                 | Bit Manipulation         |
| Dependencies, course schedule           | Graph / Topological Sort |

---

Use this guide to quickly **identify the pattern from the problem statement**, then open the corresponding folder/file in this repository to refresh the implementation approach.
