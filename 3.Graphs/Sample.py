graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    paths=[]
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            for each_path in newpath:
                paths.append(each_path)
    return paths


print(find_path(graph, 'A', 'D'))