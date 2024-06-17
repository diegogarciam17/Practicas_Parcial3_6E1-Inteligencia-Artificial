# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Practica 3
Simulador Árbol Parcial mínimo de Prim.
"""
#Como lo implementarias en tu trabajo de ensueño?
#Red de suminstros de refacciones
import heapq

def dijkstra(graph, start):
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    min_heap = [(0, start)]  # (cost, node)
    parent = [-1] * num_nodes

    while min_heap:
        current_distance, u = heapq.heappop(min_heap)

        if current_distance > distances[u]:
            continue

        for v, weight in enumerate(graph[u]):
            if weight > 0:
                distance = current_distance + weight
                if distance < distances[v]:
                    distances[v] = distance
                    parent[v] = u
                    heapq.heappush(min_heap, (distance, v))

    return distances, parent

def print_paths(start, distances, parent):
    num_nodes = len(distances)
    for i in range(num_nodes):
        if i != start:
            print(f"Distancia mínima desde {chr(start + 65)} hasta {chr(i + 65)}: {distances[i]}")
            print(f"Ruta: {get_path(start, i, parent)}\n")

def get_path(start, end, parent):
    path = []
    while end != start:
        path.append(chr(end + 65))
        end = parent[end]
    path.append(chr(start + 65))
    return ' -> '.join(path[::-1])

# Grafo representado como matriz de adyacencia
graph = [
    [0, 3, 4, 7, 2],
    [3, 0, 2, 3, 5],
    [4, 2, 0, 5, 6],
    [7, 3, 5, 0, 1],
    [2, 5, 6, 1, 0]
]

start_node = 0  # Nodo A
distances, parent = dijkstra(graph, start_node)
print_paths(start_node, distances, parent)
