# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Practica 5
"""
#Como lo implementaria en la vida?
#Red de suministros de Alimentos
import heapq

def dijkstra(graph, start):
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))
    distances = {vertex: float('infinity') for vertex in graph['vertices']}
    distances[start] = 0
    shortest_path_tree = {}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph['edges'][current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path_tree[neighbor] = (current_vertex, weight)
                heapq.heappush(pq, (distance, neighbor))
        
        # Mostrar el estado actual del algoritmo
        print(f"Current Vertex: {graph['vertices'][current_vertex]}, Distance: {current_distance}")
        print(f"Distances: {{v: distances[v] for v in graph['vertices']}}")
        print(f"Priority Queue: {pq}\n")

    return distances, shortest_path_tree

# Definición de un grafo de ejemplo para la red de suministros de alimentos
graph = {
    'vertices': ['Centro de Distribución', 'Supermercado A', 'Supermercado B', 'Tienda C', 'Tienda D'],
    'edges': {
        0: [(1, 2), (2, 5)],  # Centro de Distribución - Supermercado A: 2, Centro de Distribución - Supermercado B: 5
        1: [(0, 2), (2, 4), (3, 6)],  # Supermercado A - Centro de Distribución: 2, Supermercado A - Supermercado B: 4, Supermercado A - Tienda C: 6
        2: [(0, 5), (1, 4), (3, 2), (4, 3)],  # Supermercado B - Centro de Distribución: 5, Supermercado B - Supermercado A: 4, Supermercado B - Tienda C: 2, Supermercado B - Tienda D: 3
        3: [(1, 6), (2, 2), (4, 1)],  # Tienda C - Supermercado A: 6, Tienda C - Supermercado B: 2, Tienda C - Tienda D: 1
        4: [(2, 3), (3, 1)]  # Tienda D - Supermercado B: 3, Tienda D - Tienda C: 1
    }
}

# Ejecución del algoritmo de Dijkstra desde el Centro de Distribución
start_vertex = 0  # Centro de Distribución
distances, shortest_path_tree = dijkstra(graph, start_vertex)

# Resultados finales
print("Distances from Centro de Distribución:", {graph['vertices'][v]: d for v, d in distances.items()})
print("Shortest Path Tree:", {(graph['vertices'][k], graph['vertices'][v[0]]): v[1] for k, v in shortest_path_tree.items()})
