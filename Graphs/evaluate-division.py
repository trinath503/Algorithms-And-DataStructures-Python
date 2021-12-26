class EvaluteDivision:

    def __init__(self) -> None:
        self.graph = {}


    def build_equation_value(self, denomirator , numerator, value):

        if denomirator in self.graph:
            self.graph[denomirator].append((numerator, value))
        else:
            self.graph[denomirator]=[(numerator, value)]

    def find_paths(self, denomirator , numerator):

        if denomirator not in self.graph or numerator not in self.graph:
            return -1.0

        q = [(denomirator, 1.0)]

        visited = set()

        while q:
            cur_item, cur_product = q.pop(0)

            if cur_item == numerator:
                return cur_product

            visited.add(cur_item)

            for neighbour, cur_value in self.graph[cur_item]:
                if neighbour not in visited:
                    q.append((neighbour, cur_product*cur_value))

        return -1


    def read_input(self, equations, values, quries):

        for equation, value in zip(equations, values):
            denomirator , numerator = equation
            self.build_equation_value(denomirator , numerator, value)
            self.build_equation_value(numerator, denomirator ,  1/value)
        print(self.graph)
        for query in quries:
            denomirator , numerator = query
            print(self.find_paths(denomirator , numerator))



ED = EvaluteDivision()
ED.read_input([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
"""
3.75
0.4
5.0
0.2
"""


# soution -2 :
# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

#         graph = {}
        
#         def build_graph(equations, values):
#             def add_edge(f, t, value):
#                 if f in graph:
#                     graph[f].append((t, value))
#                 else:
#                     graph[f] = [(t, value)]
            
#             for vertices, value in zip(equations, values):
#                 f, t = vertices
#                 add_edge(f, t, value)
#                 add_edge(t, f, 1/value)
        
#         def find_path(query):
#             b, e = query
            
#             if b not in graph or e not in graph:
#                 return -1.0
                
#             q = collections.deque([(b, 1.0)])
#             visited = set()
            
#             while q:
#                 front, cur_product = q.popleft()
#                 if front == e:
#                     return cur_product
#                 visited.add(front)
#                 for neighbor, value in graph[front]:
#                     if neighbor not in visited:
#                         q.append((neighbor, cur_product*value))
            
#             return -1.0
        
#         build_graph(equations, values)
#         return [find_path(q) for q in queries]
        