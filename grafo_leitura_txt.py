import networkx as nx
import matplotlib.pyplot as plt


def ler_arquivo_grafo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = [linha.strip() for linha in f if linha.strip()]

    tipo = linhas[0]

    arestas = [tuple(linha.split()) for linha in linhas[1:]]

    return tipo, arestas

def construir_lista_adjacencia(arestas, dirigido=False, evitar_duplicatas=True):
    if evitar_duplicatas:
        grafo = {}
        for u, v in arestas:
            grafo.setdefault(u, set()).add(v)
            if not dirigido:
                grafo.setdefault(v, set()).add(u)
        return{k: sorted(list(v)) for k, v in grafo.items()}
    else:
        grafo = {}
        for u, v in arestas:
            grafo.setdefault(u, [].append(v))
            if not dirigido:
                grafo.setdefault(v, []).append(u)
        return grafo

def imprimir_grafo(grafo):
    print("Lista de Adjacência: ")
    for vertice, vizinhos in grafo.items(): 
        print(f"{vertice} -> {','.join(vizinhos)}")



#função para plotar o grafo
def plotar_grafo(grafo, dirigido= False):
    G = nx.Digraph() if dirigido else nx.Graph()

    for u, vizinhos in grafo.items():
        for v in vizinhos:
            G.add_edge(u, v)   #adiciona uma nova ligação entre vértice

    plt.figure(figsize=(10,8))

    nx.draw(
        G,
        with_labels=True,
        node_color = "lightblue",
        edge_color = "gray",
        node_size = 800,
        font_size = 10  
    )

    plt.show()


if __name__ == "__main__":
    arquivo = "grafo 1.txt"

    tipo, arestas = ler_arquivo_grafo(arquivo)

    dirigido = tipo == "D"

    grafo = construir_lista_adjacencia(arestas, dirigido)

    imprimir_grafo(grafo)

    plotar_grafo(grafo, dirigido)