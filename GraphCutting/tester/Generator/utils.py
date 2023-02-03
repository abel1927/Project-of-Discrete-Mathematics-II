def open_file(path : str):
    file = open(path, 'w')
    return file

def contain_edge(graph : list, u : int, v : int) -> bool:
    return graph[u].__contains__(v) and graph[v].__contains__(u)

