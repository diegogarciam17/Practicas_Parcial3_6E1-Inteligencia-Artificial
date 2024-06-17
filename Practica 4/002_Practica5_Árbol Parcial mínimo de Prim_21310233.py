# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Practica 4
Simulador Árbol Parcial mínimo de Prim.
"""
#Como lo implementarias en tu vida?
#Red de suminstros de alimentos

import heapq

def prim_mst(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    min_heap = [(0, 0)]  # (cost, node)
    mst_cost = 0
    mst_edges = []

    while len(min_heap) > 0:
        cost, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        mst_cost += cost

        for v, weight in enumerate(graph[u]):
            if not visited[v] and weight > 0:
                heapq.heappush(min_heap, (weight, v))
                mst_edges.append((u, v, weight))

    return mst_cost, mst_edges

# Grafo representado como matriz de adyacencia
graph = [
    [0, 1, 3, 4, 2],
    [1, 0, 1, 5, 7],
    [3, 1, 0, 2, 3],
    [4, 5, 2, 0, 6],
    [2, 7, 3, 6, 0]
]

mst_cost, mst_edges = prim_mst(graph)
print(f"Coste total del MST: {mst_cost}")
print("Aristas del MST:")
for u, v, weight in mst_edges:
    print(f"{u} - {v}: {weight}")
