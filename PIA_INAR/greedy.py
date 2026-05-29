import heapq
import itertools

def greedy(graph):
    counter = itertools.count()
    # Priority queue almacena: (heuristica, contador, nodo_actual, ruta, costo_real)
    h_init = graph.get_heuristic(graph.initial_state)
    pq = [(h_init, next(counter), graph.initial_state, [graph.initial_state], 0.0)]
    visited = set()

    while pq:
        _, _, current, path, cost = heapq.heappop(pq)

        if current == graph.goal_state:
            return path, cost

        if current not in visited:
            visited.add(current)
            for neighbor, weight in graph.get_neighbors(current):
                if neighbor not in visited:
                    h = graph.get_heuristic(neighbor)
                    heapq.heappush(pq, (h, next(counter), neighbor, path + [neighbor], cost + weight))
    return None, 0.0