import heapq
import itertools

def astar(graph):
    counter = itertools.count()
    # Priority queue almacena: (f(n), contador, nodo_actual, ruta, costo_g)
    # f(n) = g(n) + h(n)
    g_init = 0.0
    h_init = graph.get_heuristic(graph.initial_state)
    f_init = g_init + h_init
    
    pq = [(f_init, next(counter), graph.initial_state, [graph.initial_state], g_init)]
    visited = set()

    while pq:
        _, _, current, path, cost_g = heapq.heappop(pq)

        if current == graph.goal_state:
            return path, cost_g

        if current not in visited:
            visited.add(current)
            for neighbor, weight in graph.get_neighbors(current):
                if neighbor not in visited:
                    new_g = cost_g + weight
                    f = new_g + graph.get_heuristic(neighbor)
                    heapq.heappush(pq, (f, next(counter), neighbor, path + [neighbor], new_g))
    return None, 0.0