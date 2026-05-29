class Graph:
    def __init__(self):
        self.edges = {}
        self.heuristics = {}
        self.initial_state = None
        self.goal_state = None

    def add_edge(self, u, v, cost):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, float(cost)))
        # Asegurar que el nodo v exista en el diccionario aunque no tenga salidas
        if v not in self.edges:
            self.edges[v] = []

    def add_heuristic(self, node, h):
        self.heuristics[node] = float(h)

    def get_neighbors(self, node):
        return self.edges.get(node, [])

    def get_heuristic(self, node):
        return self.heuristics.get(node, 0.0)