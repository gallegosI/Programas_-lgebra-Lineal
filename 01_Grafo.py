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

        # Ingresar múltiples vértices conectados al nodo inicial
        conexiones = input(f"Inserta los vértices a conectar con {nodo_inicial}, separados por espacio (Ejemplo: C2 C3 C4): ").strip().split()

        for nodo in conexiones:
            G.add_edge(nodo_inicial, nodo)  # Conectar con aristas no dirigidas

        nodo_inicial = input("\nIngresa otro vértice para conectar más nodos (o presiona Enter para terminar): ").strip()
        if nodo_inicial == "":
            break
        G.add_node(nodo_inicial)

    return G

def dibujar_grafo(G):
    plt.figure(figsize=(6,6))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', font_size=12)
    plt.show()

# Crear y mostrar el grafo
grafo = crear_grafo()
dibujar_grafo(grafo)

