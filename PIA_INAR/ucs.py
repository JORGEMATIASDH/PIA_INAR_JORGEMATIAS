import heapq
import itertools

def ucs(graph):
    counter = itertools.count()
    # Priority queue almacena: (costo_acumulado, contador, nodo_actual, ruta)
    pq = [(0.0, next(counter), graph.initial_state, [graph.initial_state])]
    visited = set()

    while pq:
        cost, _, current, path = heapq.heappop(pq)

        if current == graph.goal_state:
            return path, cost

        if current not in visited:
            visited.add(current)
            for neighbor, weight in graph.get_neighbors(current):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, next(counter), neighbor, path + [neighbor]))
    return None, 0.0