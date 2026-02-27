# FAANG Interview — Glance & Detailed Structure

**One-page glance** of all top patterns and logics commonly asked at Meta (Facebook), Amazon, Apple, Netflix, and Google. Use this for quick revision and to see how topics connect.

---

## At a glance — Topic map

```
FAANG Interview Topics
├── 1. ARRAYS & STRINGS
│   ├── Two Pointers
│   ├── Sliding Window (fixed / variable)
│   ├── Binary Search (classic + on answer)
│   ├── Prefix Sum + Hash
│   ├── Kadane / Max subarray
│   ├── Cyclic Sort (1..n)
│   ├── Hashing / Frequency
│   └── Monotonic Stack
├── 2. LINKED LISTS
│   ├── Fast & Slow (cycle, middle, nth from end)
│   ├── Reverse / Reorder
│   ├── Merge (two / K sorted)
│   └── Doubly / Multilevel (flatten)
├── 3. TREES & BST
│   ├── DFS (path, sum, serialize)
│   ├── BFS (level order, min depth)
│   ├── BST (search, kth, range)
│   └── Build / LCA / Diameter
├── 4. GRAPHS
│   ├── BFS / DFS (traversal, shortest path)
│   ├── Topological Sort
│   ├── Union-Find
│   └── Grid (islands, flood fill)
├── 5. HEAPS & INTERVALS
│   ├── Top K (largest / frequent)
│   ├── Merge K sorted
│   ├── Merge Intervals
│   └── Meeting rooms / Events
├── 6. DYNAMIC PROGRAMMING
│   ├── Linear 1D (stairs, robber)
│   ├── Knapsack (0/1, unbounded)
│   ├── LIS / LCS
│   ├── Grid (paths, maximal square)
│   └── Partition / Subset sum
├── 7. BACKTRACKING
│   ├── Subsets / Combinations
│   ├── Permutations
│   └── N-Queens / Constraint satisfaction
├── 8. BIT MANIPULATION
│   ├── XOR (single number, missing)
│   └── Bits (power of 2, count set bits)
└── 9. DESIGN & MISC
    ├── LRU / LFU Cache
    ├── Data structure design
    └── Math / Simulation
```

---

## 1. Arrays & Strings — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **Two Pointers** | Two indices (often start/end or slow/fast) | Sorted pair sum, palindrome, partition (e.g. Dutch flag) | Move left/right by condition; or same-direction for “in-place” | O(n) | `Arrays/`, `Strings/` |
| **Sliding Window** | Contiguous segment of fixed or variable size | Max sum subarray of size K, longest substring with at most K distinct | Expand right; shrink left when constraint violated; track window state in map/count | O(n) | `Arrays/longestSubstring.py`, `sliding-window-maximum.py` |
| **Binary Search** | Halve search space each step | Sorted search, rotated sorted, “min capacity”, Kth smallest | `mid = (lo+hi)//2`; compare and set `lo=mid+1` or `hi=mid-1`; variant: binary search on answer | O(log n) | `Arrays/binary_search.py`, `search-in-rotated-sorted-array.py` |
| **Prefix Sum + Hash** | Running sum + count of prefix sums | Subarray sum equals K, contiguous sum | `prefix += x`; `count += seen[prefix - K]`; `seen[prefix] += 1` | O(n) | Concept in `Arrays/`, `Hashing/` |
| **Kadane** | Best contiguous sum ending at each index | Maximum subarray sum | `cur = max(x, cur + x)`; `best = max(best, cur)` | O(n) | `Arrays/maximum-subarray.py` |
| **Cyclic Sort** | Place value `v` at index `v-1` by swapping | Missing number, duplicate, array 1..n in place | While at `i`, if `arr[i]` not at correct pos, swap with `arr[arr[i]-1]` | O(n) | (Add under Arrays) |
| **Hashing / Freq** | Map element → count or index | Two sum, anagrams, first non-repeating | `dict` or `Counter`; complement lookup for two sum | O(n) | `Arrays/two_sum.py`, `Strings/Anagrams.py`, `Hashing/` |
| **Monotonic Stack** | Stack keeping elements in sorted order (e.g. descending) | Next greater element, largest rectangle in histogram | Pop while current > stack top; use popped index for result | O(n) | `Arrays/sliding-window-maximum.py`, `maximal-rectangle.py` |

**Pseudocode / structure (Arrays & Strings)**

```text
# Two Pointers (sorted pair / palindrome)
left, right = 0, len(arr)-1
while left < right:
    if condition_met: return or record
    if need_bigger: left += 1
    else: right -= 1

# Sliding Window (variable size)
left = 0
for right in range(len(arr)):
    add arr[right] to window
    while window_invalid: remove arr[left], left += 1
    update best

# Binary Search (classic)
lo, hi = 0, len(arr)-1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid
    if arr[mid] < target: lo = mid + 1
    else: hi = mid - 1

# Prefix Sum + Hash (subarray sum = K)
prefix = 0; seen = {0: 1}; count = 0
for x in arr:
    prefix += x
    count += seen.get(prefix - K, 0)
    seen[prefix] = seen.get(prefix, 0) + 1

# Kadane (max subarray sum)
best = cur = arr[0]
for i from 1 to n-1:
    cur = max(arr[i], cur + arr[i])
    best = max(best, cur)

# Cyclic Sort (array 1..n)
for i in range(n):
    while arr[i] != i+1 and arr[i] in valid_range:
        swap arr[i] and arr[arr[i]-1]

# Two Sum (hash)
seen = {}
for i, x in enumerate(arr):
    if target - x in seen: return [seen[target-x], i]
    seen[x] = i

# Monotonic Stack (next greater)
stack = []  # indices
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        result[idx] = arr[i]  # next greater for idx
    stack.append(i)
```

---

## 2. Linked Lists — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **Fast & Slow** | Two pointers: slow +1, fast +2 (or fast ahead by n) | Cycle detection, middle node, Nth from end | Cycle: if slow==fast then cycle; middle: when fast reaches end, slow at middle; Nth from end: fast ahead by n+1, then move both | O(n) | `LinkedLists/SingleLikedList/middle-of-the-linked-list.py`, `remove-nth-node-from-end-of-list.py` |
| **Reverse** | Change next pointers in one pass | Reverse list, reverse K nodes | `prev=None`; while head: `nxt=head.next`; `head.next=prev`; `prev=head`; `head=nxt` | O(n) | `LinkedLists/SingleLikedList/ReverseList.py` |
| **Merge Two Sorted** | Dummy node, attach smaller | Merge two sorted lists | Dummy tail; while both: attach smaller; tail.next = remaining | O(n+m) | `merge-two-sorted-linked-lists.py` |
| **Merge K Sorted** | Heap of (value, list_id, index) or divide-and-conquer merge | Merge K sorted lists | Push first node of each; pop min, append, push next from same list | O(N log K) | `merge-k-sorted-lists.py` |
| **Add Two Numbers** | Digit-by-digit with carry | Two numbers as linked lists (reverse order) | Carry; while l1 or l2 or carry: sum digits, update carry, create node | O(n) | `Add two numbers.py` |
| **Doubly / Flatten** | Multilevel: recurse on child, stitch list | Flatten multilevel doubly linked list | For each node with child: flatten child, connect cur→child, tail of child→next | O(n) | `LinkedLists/DoubleLikedList/` |

**Pseudocode / structure (Linked Lists)**

```text
# Fast & Slow — cycle
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    if slow == fast: return True  # cycle

# Fast & Slow — middle
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
return slow

# Fast & Slow — Nth from end (remove nth)
dummy = node(0, head); slow = fast = dummy
for _ in range(n+1): fast = fast.next
while fast: slow, fast = slow.next, fast.next
slow.next = slow.next.next; return dummy.next

# Reverse
prev = None
while head:
    nxt = head.next; head.next = prev; prev = head; head = nxt
return prev

# Merge two sorted
dummy = tail = node(0)
while l1 and l2:
    if l1.val <= l2.val: tail.next, l1 = l1, l1.next
    else: tail.next, l2 = l2, l2.next
    tail = tail.next
tail.next = l1 or l2; return dummy.next

# Add two numbers (carry)
dummy = tail = node(0); carry = 0
while l1 or l2 or carry:
    v = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
    carry, v = v // 10, v % 10
    tail.next = node(v); tail = tail.next
    if l1: l1 = l1.next; if l2: l2 = l2.next
return dummy.next

# Flatten multilevel (doubly)
cur = head
while cur:
    if cur.child:
        nxt = cur.next; cur.next = cur.child; cur.child.prev = cur
        tail = cur.child; while tail.next: tail = tail.next
        tail.next = nxt; if nxt: nxt.prev = tail; cur.child = None
    cur = cur.next
```

---

## 3. Trees & BST — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **DFS (recursive)** | Recurse on left/right with state | Path sum, max depth, serialize, invert | Base: null or leaf; recurse with updated sum/depth/path | O(n) | `Trees/path-sum-fromroot-to-leaf.py`, `serialize-and-deserialize-binary-tree.py` |
| **BFS (level order)** | Queue, process by level | Level order, min depth, width | Queue; for each level size, pop and add children | O(n) | `Trees/BinaryTrees/Maz width of tree.py` |
| **BST search / range** | Use BST property (left < root < right) | Search, kth smallest, range sum | Search: go left if target < root.val else right; kth: inorder; range: prune outside [low,high] | O(h) / O(n) | `Trees/Binary Search Tree/`, `Trees/BinaryTrees/Inorder Succsedor.py` |
| **Build tree** | From preorder+inorder or level order | Construct from pre+in, deserialize | Preorder gives root; inorder splits left/right; recurse | O(n) | `Trees/construct-*` |
| **Height / Balanced / Diameter** | Post-order: get height from children | Balanced tree, diameter | Height: 1+max(L,R); balanced: abs(L-R)<=1 and both balanced; diameter: max(diam L, diam R, 1+L+R) | O(n) | Concept in `Trees/` |

**Pseudocode / structure (Trees & BST)**

```text
# DFS (path sum, serialize, invert)
def dfs(root, state):
    if not root: return base_value
    state = update(state, root.val)
    if is_leaf(root) and goal(state): return True or record
    return dfs(root.left, state) or dfs(root.right, state)

# BFS level order
q = deque([root])
while q:
    level = []
    for _ in range(len(q)):
        node = q.popleft(); level.append(node.val)
        if node.left: q.append(node.left); if node.right: q.append(node.right)
    result.append(level)

# BST search
def search(root, val):
    if not root or root.val == val: return root
    return search(root.left, val) if val < root.val else search(root.right, val)

# BST kth smallest — inorder, count
def inorder(node):
    if not node: return
    inorder(node.left)
    k -= 1; if k == 0: ans = node.val
    inorder(node.right)

# Build from preorder + inorder
root = TreeNode(pre[0]); i = in.index(pre[0])
root.left = build(pre[1:1+i], in[:i]); root.right = build(pre[1+i:], in[i+1:])
return root

# Height / balanced
def height(node):
    if not node: return 0
    L, R = height(node.left), height(node.right)
    if abs(L-R) > 1: return -1  # unbalanced
    return 1 + max(L, R)
```

---

## 4. Graphs — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **BFS** | Queue; level-by-level | Shortest path (unweighted), level order | Visit from queue; add unvisited neighbors; track distance/level | O(V+E) | `Graphs/BFS - Recursion.py` |
| **DFS** | Stack or recursion | Traversal, cycle, connected components | Visit node; recurse/stack all unvisited neighbors | O(V+E) | `Graphs/DFS - Recursion.py` |
| **Grid DFS/BFS** | 2D matrix, 4 or 8 directions | Number of islands, flood fill | For each cell, if unvisited and land/color, run DFS/BFS and mark | O(rows*cols) | `Matrix/NumberOfIslands.py`, `Arrays/number-of-islands.py` |
| **Topological Sort** | Order such that edge u→v ⇒ u before v | Course schedule, task ordering | Kahn: indegree 0 queue; or DFS post-order reverse | O(V+E) | Concept in `Graphs/` |
| **Union-Find** | Disjoint set with find + union | Connected components, cycle in undirected | Parent array; find with path compression; union by rank | O(α(n)) ≈ O(1) | (Add under Graphs if needed) |

**Pseudocode / structure (Graphs)**

```text
# BFS (shortest path unweighted)
q = deque([start]); visited = {start}; dist = 0
while q:
    for _ in range(len(q)):
        u = q.popleft()
        if u == end: return dist
        for v in graph[u]:
            if v not in visited: visited.add(v); q.append(v)
    dist += 1

# DFS (recursive)
def dfs(u):
    visited.add(u); process(u)
    for v in graph[u]:
        if v not in visited: dfs(v)

# Grid DFS (islands)
def dfs_grid(r, c):
    if out_of_bounds(r,c) or grid[r][c]=='0' or (r,c) in seen: return
    seen.add((r,c))
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]: dfs_grid(r+dr, c+dc)
# call: for each cell if grid[i][j]=='1' and (i,j) not in seen: dfs_grid(i,j); count += 1

# Topological (Kahn)
indeg = [0]*n; for u in graph: for v in graph[u]: indeg[v] += 1
q = deque([i for i in range(n) if indeg[i]==0]); order = []
while q:
    u = q.popleft(); order.append(u)
    for v in graph[u]: indeg[v] -= 1; if indeg[v]==0: q.append(v)
# if len(order) != n: cycle
```

---

## 5. Heaps & Intervals — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **Top K largest** | Min-heap of size K | Kth largest, top K elements | Push all; if len>K pop min; result = heap | O(n log K) | `Arrays/top-k-elements.py`, `Heaps/` |
| **Top K frequent** | Count freq; heap (freq, val) size K | K most frequent elements | Counter; min-heap by freq; keep size K | O(n log K) | `Heaps/` |
| **Merge K sorted** | Heap of (first value, list_id, index) | Merge K sorted lists/arrays | Push first of each; pop min, push next from same list | O(N log K) | `LinkedLists/.../merge-k-sorted-lists.py`, `Heaps/` |
| **Merge Intervals** | Sort by start; merge overlapping | Merge intervals, insert interval | Sort; if current overlaps last merged, extend; else append new | O(n log n) | `Arrays/MergeIntervals.py`, events in `Heaps/` |
| **Max events / scheduling** | Sort by start; min-heap of end times | Max events attendable, meeting rooms | For each day: add events starting today to heap (by end); pop one to attend | O(n log n) | `Heaps/.../maximum-number-of-events-that-can-be-attended.py` |

**Pseudocode / structure (Heaps & Intervals)**

```text
# Top K largest (min-heap size k)
heap = []
for x in nums:
    heappush(heap, x)
    if len(heap) > k: heappop(heap)
return heap

# Top K frequent
count = Counter(nums)
heap = []  # (freq, val)
for val, freq in count.items():
    heappush(heap, (freq, val))
    if len(heap) > k: heappop(heap)
return [val for _, val in heap]

# Merge K sorted (arrays/lists)
heap = [(arr[i][0], i, 0) for i in range(k) if arr[i]]
while heap:
    val, i, j = heappop(heap)
    result.append(val)
    if j+1 < len(arr[i]): heappush(heap, (arr[i][j+1], i, j+1))

# Merge intervals
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for s, e in intervals[1:]:
    if s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
    else: merged.append([s, e])

# Max events (sort by start, heap by end)
events.sort(key=lambda x: x[0]); heap = []; day = 1; i = 0; count = 0
while day <= max_end:
    while i < n and events[i][0] <= day: heappush(heap, events[i][1]); i += 1
    while heap and heap[0] < day: heappop(heap)
    if heap: heappop(heap); count += 1
    day += 1
```

---

## 6. Dynamic Programming — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **Linear 1D** | dp[i] from dp[i-1], dp[i-2] | Climbing stairs, house robber, min cost | Base cases; loop: dp[i] = f(dp[i-1], dp[i-2], …); can reduce to variables | O(n) | `Dynamic-Programming/climbing-stairs.py`, `house-robber.py` |
| **0/1 Knapsack** | Pick or skip each item once | Max value with weight limit | dp[i][w] = max(dp[i-1][w], val[i]+dp[i-1][w-wt[i]]) | O(n*W) | `03.knapsack_top_down_dp.py`, `04.subset_sum_problem_dp.py` |
| **Unbounded** | Same item repeatable | Coin change (ways/min coins), rod cutting | Loop coins first; for each amount: dp[a] += dp[a-c] or min | O(amount * len(coins)) | `09.coin_change_max_ways-unbounded.py` |
| **LIS** | Longest increasing subsequence | LIS length | dp[i] = 1 + max(dp[j] for j<i if nums[j]<nums[i]) | O(n²) or O(n log n) with binary search | `Arrays/longest-increasing-subsequence.py` |
| **Grid 2D** | dp[i][j] from neighbors | Unique paths, maximal square | dp[i][j] = f(dp[i-1][j], dp[i][j-1], grid[i][j]) | O(rows*cols) | `Arrays/maximal-square.py`, `maximal-rectangle.py` |
| **Partition / Subset sum** | Subset of array sums to target | Partition equal subset, subset sum | Boolean dp[sum]; for each num, update from right to left | O(n * sum) | `Dynamic-Programming/05.equal_sum_partition_problem.py`, `06.count_of_subsets_with_given_sum.py` |

**Pseudocode / structure (Dynamic Programming)**

```text
# Linear 1D (stairs, robber)
dp[0], dp[1] = base0, base1
for i in range(2, n): dp[i] = f(dp[i-1], dp[i-2], arr[i])
# space-opt: use two vars prev, curr and update in loop

# 0/1 Knapsack
dp[i][w] = 0 for i==0 or w==0
for i in 1..n, w in 0..W:
    if wt[i-1] <= w: dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]])
    else: dp[i][w] = dp[i-1][w]

# Coin change (ways, unbounded)
dp[0] = 1
for c in coins:
    for a in range(c, amount+1): dp[a] += dp[a-c]

# LIS
dp[i] = 1 for all i
for i in 1..n-1:
    for j in 0..i-1:
        if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)
return max(dp)

# Subset sum (boolean)
dp[0] = True
for x in nums:
    for s in range(target, x-1, -1):
        if dp[s-x]: dp[s] = True
```

---

## 7. Backtracking — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **Combination Sum** | Reuse / no reuse; unique combos | Combination sum I/II, subsets | Backtrack(start, path, total): base total==target; for i in range(start, n): path.append; backtrack(i or i+1, …); path.pop; sort + skip duplicate for unique | Exponential | `backtracking/combination-sum.py`, `combination-sum-ii*.py` |
| **Subsets** | All subsets | Subsets, subset with dup | Backtrack(start, path): result.append(path); for i from start: path.append; backtrack(i+1); path.pop | O(2^n) | Template in `backtracking/_solution_template.py` |
| **Permutations** | All orderings | Permutations, permute with dup | Backtrack(path, remaining): if not remaining: result.append(path); for each in remaining: path.append; backtrack(remaining without each); path.pop | O(n!) | Template in `backtracking/_solution_template.py` |
| **N-Queens / placement** | Place with row/col/diag constraints | N-Queens, Sudoku | Try each row/col; if valid, place and recurse; backtrack remove | Exponential | (Add if needed) |

**Pseudocode / structure (Backtracking)**

```text
# Generic backtrack skeleton
result = []
def backtrack(start, path, state):
    if goal_met(state): result.append(path[:]); return
    if invalid(state): return
    for i in range(start, n):
        if skip_duplicate(i): continue
        path.append(candidates[i]); state = update(state, candidates[i])
        backtrack(i or i+1, path, state)   # i = reuse, i+1 = use once
        path.pop()

# Combination sum (reuse)
backtrack(0, [], 0)
# inside: if total==target: result.append(path[:]); return
#         if total>target: return
#         for i in range(start, len(c)): path.append(c[i]); backtrack(i, path, total+c[i]); path.pop()

# Subsets
def backtrack(start, path):
    result.append(path[:])
    for i in range(start, n): path.append(nums[i]); backtrack(i+1, path); path.pop()

# Permutations (remaining list)
def backtrack(path, remaining):
    if not remaining: result.append(path[:]); return
    for i, x in enumerate(remaining):
        path.append(x); backtrack(path, remaining[:i]+remaining[i+1:]); path.pop()
```

---

## 8. Bit manipulation — Detailed structure

| Pattern | What it is | When asked | Key logic | Complexity | In this repo |
|--------|------------|------------|-----------|------------|--------------|
| **XOR** | a^a=0, a^0=a; order doesn’t matter | Single number (others twice), missing number | Single: xor all → result; missing in 1..n: xor all with 1..n | O(n) | `Bitwise/find-the-element-that-appears-once.py` |
| **Thrice except one** | Every element 3 times, one once | Single number II | 3*sum(set)-sum // 2; or bit-count mod 3 per position | O(n) | Same file |
| **Power of 2 / bits** | n&(n-1)==0 for power of 2 | Power of two, count set bits | Count: while n: c+=n&1; n>>=1 | O(1) / O(bits) | `Bitwise/_solution_template.py` |

**Pseudocode / structure (Bit manipulation)**

```text
# Single number (all twice except one) — XOR
res = 0
for x in nums: res ^= x
return res

# Missing number in 1..n (XOR)
xor_all = 0
for i, x in enumerate(nums): xor_all ^= (i+1) ^ x
return xor_all  # or xor_all ^ len(nums) depending on problem

# Single number (all 3 times except one) — math
return (3 * sum(set(nums)) - sum(nums)) // 2

# Power of two
return n > 0 and (n & (n - 1)) == 0

# Count set bits
c = 0
while n: c += n & 1; n >>= 1
return c
```

---

## 9. Design & misc — Detailed structure

| Topic | What it is | When asked | Key logic | In this repo |
|-------|------------|------------|-----------|--------------|
| **LRU Cache** | Evict least recently used | Design LRU cache | OrderedDict: get→move_to_end; put→move_to_end or popitem(last=False) if over cap | `Miscs/LRU Cache.py` |
| **TinyURL / Encode-decode** | Short URL ↔ long URL | Encode-decode design | Map short→long and long→short; generate short with random or counter | `Strings/encode-decode-tinyurl.py` |
| **Math / Simulation** | Next time, digit rules | Next closest time, etc. | Enumerate valid options; pick best | `Miscs/Next-closest-time.py` |

**Pseudocode / structure (Design & misc)**

```text
# LRU Cache (OrderedDict)
get(key): if key not in cache: return -1; cache.move_to_end(key); return cache[key]
put(key, val): if key in cache: cache.move_to_end(key)
               cache[key] = val
               if len(cache) > cap: cache.popitem(last=False)

# Encode-decode (TinyURL)
encode(long): short = generate_unique(); map[short]=long; rev[long]=short; return short
decode(short): return map[short]
```

---

## Quick reference — Where to look in this repo

| Topic | Folder / files |
|-------|----------------|
| Arrays (two sum, window, binary search, Kadane, etc.) | `Arrays/` |
| Strings (palindrome, anagram, parentheses) | `Strings/` |
| Linked lists (singly, doubly, merge, add two) | `LinkedLists/`, `SingleLikedList/`, `DoubleLikedList/` |
| Trees & BST | `Trees/`, `Trees/BinaryTrees/`, `Trees/Binary Search Tree/` |
| Graphs & grid | `Graphs/`, `Matrix/` |
| Heaps & events | `Heaps/`, `Heaps/MinHeap/`, `Heaps/PriorityQueues/` |
| DP | `Dynamic-Programming/` |
| Backtracking | `backtracking/` |
| Bitwise | `Bitwise/` |
| Hashing | `Hashing/` |
| Stacks & queues | `Stacks & Queues/` |
| Design / misc | `Miscs/` |

---

## How to use this file

1. **Glance** — Use the topic map at the top to see all categories and sub-patterns.
2. **Deep dive** — Use the tables under each section for “what it is”, “when asked”, “key logic”, and “where in repo”.
3. **Recall** — Use the **Pseudocode / structure** blocks right after each table: copy-paste style snippets for each pattern so you can quickly recall the structure during prep or interview.
4. **With other docs** — Use **README.md** (or FAANG-PATTERNS-GUIDE) for *clue → pattern*; use **`_solution_template.py`** in each folder for *full code skeletons*; use this file for *structure, logic summary, and easy-to-recall pseudocode*.
