def dls(graph, limit):
    def recursive_dls(node, path, cost, depth):
        if node == graph.goal_state:
            return path, cost
        if depth == limit:
            return None, 0.0
            
        for neighbor, weight in graph.get_neighbors(node):
            if neighbor not in path: # Evitar ciclos simples en la ruta actual
                result_path, result_cost = recursive_dls(neighbor, path + [neighbor], cost + weight, depth + 1)
                if result_path is not None:
                    return result_path, result_cost
        return None, 0.0

    return recursive_dls(graph.initial_state, [graph.initial_state], 0.0, 0)