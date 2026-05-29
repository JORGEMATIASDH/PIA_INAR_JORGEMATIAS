from dls import dls

def iddfs(graph, max_depth=50):
    for limit in range(max_depth):
        path, cost = dls(graph, limit)
        if path is not None:
            return path, cost
    return None, 0.0