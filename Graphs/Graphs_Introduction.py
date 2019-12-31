class Graph:
    def __init__(self):
        self.graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def ShowEdges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                 print("(",node,", ",neighbour,")")



g= Graph()
g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('2', '3')
g.addEdge('2', '1')
g.addEdge('3', '1')
g.addEdge('3', '2')
g.addEdge('3', '4')
g.addEdge('4', '3')
g.ShowEdges()