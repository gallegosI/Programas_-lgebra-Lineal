#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Teorìa de Grafos
#   Matemática Algoritmica
#   ESFM-IPN    Marzo-2025
#==================================

import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo():
    G = nx.Graph()  # Grafo no dirigido

    # Ingresar el primer vértice
    nodo_inicial = input("Ingresa el primer vértice (Ejemplo: C1): ").strip()
    G.add_node(nodo_inicial)

    while True:
        opcion = input("\n¿Deseas agregar conexiones para este vértice? (s/n): ").strip().lower()
        if opcion == 'n':
            break

        conexiones = input(f"Inserta los vértices a conectar con {nodo_inicial}, separados por espacio (Ejemplo: C2 C3 C4): ").strip().split()

        for nodo in conexiones:
            G.add_edge(nodo_inicial, nodo)  # Conectar con aristas no dirigidas

        nodo_inicial = input("\nIngresa otro vértice para conectar más nodos (o presiona Enter para terminar): ").strip()
        if nodo_inicial == "":
            break
        G.add_node(nodo_inicial)

    return G

def crear_subgrafo_inducido(G):
    nodos_subgrafo = input("\nIngresa los vértices del subgrafo inducido separados por espacio (Ejemplo: C1 C3 C5): ").strip().split()

    # Verificar que los nodos existan en el grafo original
    nodos_subgrafo = [nodo for nodo in nodos_subgrafo if nodo in G.nodes]

    # Crear el subgrafo inducido
    subG = G.subgraph(nodos_subgrafo).copy()

    return subG

def dibujar_grafo(G, title="Grafo"):
    plt.figure(figsize=(6,6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', font_size=12)
    plt.title(title)
    plt.show()

# Crear el grafo original
grafo = crear_grafo()
dibujar_grafo(grafo, "Grafo Original")

# Crear y mostrar el subgrafo inducido
subgrafo = crear_subgrafo_inducido(grafo)
dibujar_grafo(subgrafo, "Subgrafo Inducido")

