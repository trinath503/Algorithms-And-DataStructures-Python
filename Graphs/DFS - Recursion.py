class Graph:
    #constrcutor
    def __init__(self, edges, N):
        #nodes
        self.graph_dict = {}
        self.visited = set()
        self.add_edges(edges)

    #for adding a vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

        #since its bi-directional
        if neighbour not in self.graph_dict:
            self.graph_dict[neighbour] = []

    def add_edges(self,edges):
        for (src_node, dest_node) in edges:
            self.addEdge(src_node, dest_node)

    def ShowEdges(self):
        for node in self.graph_dict:
            print('node', node)
            for neighbour in self.graph_dict[node]:
                 print("(",node,", ",neighbour,")")

    def is_node_visited(self,node):
        if node not in self.visited:
            self.visited.add(node)
            print(node)
            for neighbour in self.graph_dict[node]:
                self.is_node_visited(neighbour)

    def dfs(self):
        for node in self.graph_dict:
            self.is_node_visited(node)


    def iterativeDFS(self):
        for node in self.graph_dict:
            #create a stack
            maitian_stack = []
            maitian_stack.append(node)
            # print(node)
            while maitian_stack:
                cur_node = maitian_stack.pop(0)
                if cur_node in self.visited:
                    continue
                else:
                    self.visited.add(cur_node)
                    print('--',cur_node,maitian_stack)
                    for neighbour in self.graph_dict[cur_node]:
                        print(neighbour)
                        if neighbour not in self.visited:
                            maitian_stack.insert(0,neighbour)





    #this is test function to return random test case
    def return_random(self):
        print(self.graph_dict.items())







if __name__ == '__main__':

    # take the list of nodes
    nodes = [1,2,3,4,5,6,7,8,9,10,11,12]

    total_nodes = len(nodes)
    print(total_nodes)

    #list of graph edges
    edges = [
        # Notice that node 0 is unconnected node
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
        # , (6, 9) # introduce cycle
    ]

    total_edges = len(edges)

    construct_graph = Graph(edges, total_nodes)
    construct_graph.ShowEdges()
    construct_graph.iterativeDFS()



