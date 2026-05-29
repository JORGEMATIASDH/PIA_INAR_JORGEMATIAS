def bfs(graph):
    queue = [(graph.initial_state, [graph.initial_state], 0.0)]
    visited = set()

    while queue:
        current, path, cost = queue.pop(0)
        
        if current == graph.goal_state:
            return path, cost
            
        if current not in visited:
            visited.add(current)
            for neighbor, weight in graph.get_neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + weight))
    return None, 0.0