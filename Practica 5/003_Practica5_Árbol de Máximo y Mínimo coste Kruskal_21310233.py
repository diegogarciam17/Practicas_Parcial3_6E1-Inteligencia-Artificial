# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Practica 5
"""
#Como lo implementaria en mi trabajo de en sueño?
#Suministro de refacciones
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

def kruskal(graph, maximize=False):
    edges = sorted(graph['edges'], key=lambda x: x[2], reverse=maximize)
    uf = UnionFind(len(graph['vertices']))
    mst = []

    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append(edge)
        
        # Mostrar el estado actual del MST y la estructura Union-Find
        print(f"Current Edge: ({u} --{weight}--> {v})")
        print(f"MST: {mst}")
        print(f"Union-Find Parent: {uf.parent}")
        print(f"Union-Find Rank: {uf.rank}\n")

    return mst

# Definición de un grafo de ejemplo para la red de suministros de autopartes
graph = {
    'vertices': ['Fábrica', 'Almacén1', 'Almacén2', 'Distribuidor1', 'Distribuidor2'],
    'edges': [
        (0, 1, 10),  # Fábrica - Almacén1: 10
        (0, 2, 20),  # Fábrica - Almacén2: 20
        (1, 2, 30),  # Almacén1 - Almacén2: 30
        (1, 3, 40),  # Almacén1 - Distribuidor1: 40
        (2, 3, 50),  # Almacén2 - Distribuidor1: 50
        (2, 4, 60),  # Almacén2 - Distribuidor2: 60
        (3, 4, 70)   # Distribuidor1 - Distribuidor2: 70
    ]
}

# Ejecución del algoritmo para el Árbol de Expansión Mínima
print("Minimum Spanning Tree:")
mst_min = kruskal(graph, maximize=False)

# Ejecución del algoritmo para el Árbol de Expansión Máxima
print("Maximum Spanning Tree:")
mst_max = kruskal(graph, maximize=True)

# Resultados finales
print("Minimum Spanning Tree:", mst_min)
print("Maximum Spanning Tree:", mst_max)
Implementación Gráfica (Opcional)
Para una implementación gráfica, podríamos usar bibliotecas como matplotlib y networkx para visualizar el grafo y el progreso del algoritmo. Aquí tienes un ejemplo básico de cómo podría hacerse:

Código para Visualización
python
Copiar código
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, mst_edges, title):
    G = nx.Graph()
    
    for u, v, weight in graph['edges']:
        G.add_edge(graph['vertices'][u], graph['vertices'][v], weight=weight)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    # Dibujar las aristas del árbol de expansión
    mst_edges_graph = nx.Graph()
    for u, v, weight in mst_edges:
        mst_edges_graph.add_edge(graph['vertices'][u], graph['vertices'][v], weight=weight)
    nx.draw(mst_edges_graph, pos, edge_color='red', width=2.0)
    
    plt.title(title)
    plt.show()

# Definición de un grafo de ejemplo para la red de suministros de autopartes
graph = {
    'vertices': ['Fábrica', 'Almacén1', 'Almacén2', 'Distribuidor1', 'Distribuidor2'],
    'edges': [
        (0, 1, 10),  # Fábrica - Almacén1: 10
        (0, 2, 20),  # Fábrica - Almacén2: 20
        (1, 2, 30),  # Almacén1 - Almacén2: 30
        (1, 3, 40),  # Almacén1 - Distribuidor1: 40
        (2, 3, 50),  # Almacén2 - Distribuidor1: 50
        (2, 4, 60),  # Almacén2 - Distribuidor2: 60
        (3, 4, 70)   # Distribuidor1 - Distribuidor2: 70
    ]
}

# Ejecución del algoritmo para el Árbol de Expansión Mínima
print("Minimum Spanning Tree:")
mst_min = kruskal(graph, maximize=False)

# Ejecución del algoritmo para el Árbol de Expansión Máxima
print("Maximum Spanning Tree:")
mst_max = kruskal(graph, maximize=True)

# Dibujar los grafos y los árboles de expansión
print("Minimum Spanning Tree:")
draw_graph(graph, mst_min, "Minimum Spanning Tree")

print("Maximum Spanning Tree:")
draw_graph(graph, mst_max, "Maximum Spanning Tree")