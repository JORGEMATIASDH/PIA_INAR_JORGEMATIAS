def dfs(graph):
    stack = [(graph.initial_state, [graph.initial_state], 0.0)]
    visited = set()

    while stack:
        current, path, cost = stack.pop()
        
        if current == graph.goal_state:
            return path, cost
            
        if current not in visited:
            visited.add(current)
            # Invertimos los vecinos para explorar en orden correcto si se añade a una pila
            for neighbor, weight in reversed(graph.get_neighbors(current)):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + weight))
    return None, 0.0