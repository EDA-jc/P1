import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() #criando um novo grafo

G.add_edges_from([("PC0", "S1"),("PC1", "S1"),("PC2", "S1"),("S1", "R1")]) #Adicionando uma subrede
G.add_edges_from([("PC3", "S2"),("PC4", "S2"),("PC5", "S2"),("S2", "R1")]) #Adcionando uma subrede
G.add_edges_from([("PC6", "S3"),("PC7", "S3"),("PC8", "S3"),("S3", "R4")]) #Adicionando uma subrede
G.add_edges_from([("PC9", "S4"),("PC10", "S4"),("PC11", "S4"),("S4", "R4")]) #Adicionando uma subrede
G.add_edges_from([("PC12", "S5"),("PC13", "S5"),("PC14", "S5"),("S5", "R3")]) #Adicionando uma subrede
G.add_edges_from([("PC15", "S6"),("PC16", "S6"),("PC17", "S6"),("S6", "R3")]) #Adicionando uma subrede
G.add_edges_from([("PC18", "S7"),("PC19", "S7"),("PC20", "S7"),("S7", "R2")]) #Adicionando uma subrede
G.add_edges_from([("PC21", "S8"),("PC22", "S8"),("PC23", "S8"),("S8", "R2")]) #Adicionando uma subrede


G.add_edges_from([("R1", "R0"), ("R2", "R0"), ("R3", "R0"), ("R4", "R0")]) #Conexão com os roteadores

nx.draw(
    G,                          #grafo G
    with_labels=True, 
    node_color="red",           #cor dos vértices
    edge_color = "lightblue",   #cor das arestas
    node_size = 600,             #tamanho dos vértices     
    font_size = 10             #tamanho da fonte            
    )

print("Gerando grafo...")

plt.show(block=True) #plotando o grafo

plt.title("Grafo 1", fontsize = 100)
