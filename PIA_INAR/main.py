import os
import sys
from graph import Graph
from bfs import bfs
from dfs import dfs
from ucs import ucs
from dls import dls
from iddfs import iddfs
from greedy import greedy
from astar import astar

def parse_file(filename):
    graph = Graph()
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            
        section = None
        for line in lines:
            if line.startswith("INITIAL:"):
                graph.initial_state = line.split(":")[1].strip()
            elif line.startswith("GOAL:"):
                graph.goal_state = line.split(":")[1].strip()
            elif line == "EDGES:":
                section = "EDGES"
            elif line == "HEURISTICS:":
                section = "HEURISTICS"
            else:
                if section == "EDGES":
                    parts = line.split()
                    if len(parts) == 3:
                        u, v, cost = parts
                        graph.add_edge(u, v, cost)
                elif section == "HEURISTICS":
                    parts = line.split()
                    if len(parts) == 2:
                        node, h = parts
                        graph.add_heuristic(node, h)
        return graph
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def manual_input():
    graph = Graph()
    graph.initial_state = input("Ingrese el estado INICIAL: ").strip()
    graph.goal_state = input("Ingrese el estado FINAL: ").strip()
    
    print("\n-- Ingreso de transiciones (Aristas) --")
    print("Formato: NodoOrigen NodoDestino Costo (ej. A B 5)")
    print("Escriba 'FIN' para terminar de ingresar aristas.")
    while True:
        line = input("> ").strip()
        if line.upper() == 'FIN':
            break
        parts = line.split()
        if len(parts) == 3:
            graph.add_edge(parts[0], parts[1], parts[2])
        else:
            print("Formato incorrecto. Intente de nuevo.")

    print("\n-- Ingreso de Heurísticas (opcional, necesario para A* y Avara) --")
    print("Formato: Nodo ValorHeuristico (ej. A 10)")
    print("Escriba 'FIN' para terminar.")
    while True:
        line = input("> ").strip()
        if line.upper() == 'FIN':
            break
        parts = line.split()
        if len(parts) == 2:
            graph.add_heuristic(parts[0], parts[1])
        else:
            print("Formato incorrecto. Intente de nuevo.")
            
    return graph

def main():
    print("=== SIMULADOR DE ALGORITMOS DE BÚSQUEDA ===")
    print("1. Cargar espacio de estados desde archivo txt")
    print("2. Capturar espacio de estados manualmente en línea")
    
    choice = input("Seleccione una opción (1/2): ").strip()
    
    if choice == '1':
        filename = input("Ingrese el nombre del archivo (ej. grafo.txt): ").strip()
        if not os.path.exists(filename):
            print("El archivo no existe.")
            sys.exit()
        graph = parse_file(filename)
    elif choice == '2':
        graph = manual_input()
    else:
        print("Opción no válida.")
        sys.exit()

    if not graph or not graph.initial_state or not graph.goal_state:
        print("Error: El grafo no está bien definido (Falta estado inicial o final).")
        sys.exit()

    while True:
        print("\n--- MENÚ DE ALGORITMOS ---")
        print("1. Búsqueda por Amplitud (BFS)")
        print("2. Búsqueda por Costo Uniforme (UCS)")
        print("3. Búsqueda por Profundidad (DFS)")
        print("4. Búsqueda por Profundidad Limitada (DLS)")
        print("5. Búsqueda por Profundidad Iterativa (IDDFS)")
        print("6. Búsqueda Avara (Greedy)")
        print("7. Búsqueda A*")
        print("8. Salir")
        
        alg_choice = input("Seleccione un algoritmo: ").strip()
        
        path, cost = None, 0.0
        
        if alg_choice == '1':
            path, cost = bfs(graph)
        elif alg_choice == '2':
            path, cost = ucs(graph)
        elif alg_choice == '3':
            path, cost = dfs(graph)
        elif alg_choice == '4':
            limit = int(input("Ingrese el límite de profundidad: "))
            path, cost = dls(graph, limit)
        elif alg_choice == '5':
            path, cost = iddfs(graph)
        elif alg_choice == '6':
            path, cost = greedy(graph)
        elif alg_choice == '7':
            path, cost = astar(graph)
        elif alg_choice == '8':
            print("Saliendo del simulador...")
            break
        else:
            print("Opción no válida.")
            continue
            
        print("\n--- RESULTADO ---")
        if path:
            print(f"Ruta encontrada: {' -> '.join(path)}")
            print(f"Costo total: {cost}")
        else:
            print("No se encontró una ruta hacia el estado final.")

if __name__ == "__main__":
    main()