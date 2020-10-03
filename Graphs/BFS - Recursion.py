class Graph:
    def __init__(self, edges, N):
        self.graph = {}
        self.visited = set()
        self.addEdges(edges)

    def add_vertex(self,vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []

    def add_edge(self,src_node, dest_node):
        if src_node not in self.graph.keys():
            self.graph[src_node] = [dest_node]
        else:
            self.graph[src_node].append(dest_node)
        #since bi-directional
        if dest_node not in self.graph:
            self.graph[dest_node] = [src_node]
        else:
            self.graph[dest_node].append(src_node)

    def addEdges(self, edges):
        for src_node, dest_node in edges:
            self.add_edge(src_node, dest_node)

    def is_visited_node(self,node):
        if node not in self.visited:
            self.visited.add(node)
            print(node)
            for neighbour in self.graph[node]:
                self.is_visited_node(neighbour)


    def dfs_traversal(self):
        for node in self.graph:
            self.is_visited_node(node)



    def bfs_traversal(self):
        starting_node = list(self.graph.keys())[0]
        queue = []
        queue.append(starting_node)
        #doing bfs
        while queue:
            current_node = queue.pop(0)
            if current_node is not self.visited:
                print(current_node)
                self.visited.add(current_node)
                for neigbhour in self.graph[current_node]:
                    if neigbhour not in self.visited:
                        queue.append(neigbhour)







if __name__ == '__main__':

    # # take the list of nodes
    # nodes = [1,2,3,4,5,6,7,8,9,10,11,12]
    #
    # total_nodes = len(nodes)
    # # print(total_nodes)
    #
    # #list of graph edges
    # edges = [
    #     # Notice that node 0 is unconnected node
    #     (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
    #     (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    #     # , (6, 9) # introduce cycle
    # ]
    #
    # total_edges = len(edges)
    #
    # construct_graph = Graph(edges, total_nodes)
    # construct_graph.dfs_traversal()
    ''' BFS DETAILS '''
    nodes = [1,2,3,4,5,6,7,8,9,10,11,12]

    total_nodes = len(nodes)
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13 and 14 are single nodes
    ]

    construct_graph = Graph(edges, total_nodes)
    construct_graph.bfs_traversal()
