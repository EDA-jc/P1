import networkx as nx
import matplotlib.pyplot as plt

#função p/ ler o arquivi txt
def ler_arquivivo(arquivo):
    with open(arquivo, "r", encoding="UTF-8") as arq:
        linhas = [linha.strip() for linha in arq if linha.strip()] #retorna uma lista com as linhas não vazias

        tipo = linhas[0] #conteúdo da primeira linha
        arestas = [tuple(linha.split(" ")) for linha in linhas [1:]] #uma lista de tuplas que contém as arestas

        return tipo, arestas


#construindo o grafo a partir de uma lista de adjacência
def construir_grafo(arestas, dirigido=False, evitar_duplicatas=True): #por padrão criamos um grafo não dirigido
    if evitar_duplicatas:
        grafo = {}
        for u, v in arestas: #aqui lidamos com conjuntos pois eles não permitem valores permitidos
            grafo.setdefault(u, set()).add(v)
            if not dirigido:
                grafo.setdefault(v, set()).add(u)
        return {k: sorted(list(v)) for k, v in grafo.items()} #****
    else:
        grafo = {} 
        for u, v in arestas: #como nesse caso é permitido duplicatas, então já podemos lidar diretamente com listas (listas permitem duplicatas)
            grafo.setdefault(u, list()).append(v)
            if not dirigido:
                grafo.setdefault(v, list()).append(u)
        return grafo
    
#função para imprimir a lista de adjacência
def imprimir_listadj(grafo):
    print("Lista de Adjacência")
    separador = ", "
    for x, y in grafo.items():
        print(x, "->", separador.join(y))


#Função p/ indentificar os pontos críticos do grafo 

#função para plotar o grafo
def plotar_grafo(grafo, dirigido=False): #assume que o valor padrão de dirigido é false, ou seja que estamos trabalhando com um grafo não dirigido
    #criando o grafo
    G = nx.DiGraph() if dirigido else nx.Graph() #se o dirifido for verdadeiro então cria um grafo dirigido, se não cria um grafo não dirigido
    #adicionando as arestas
    for u, adjacentes in grafo.items():
        for v in adjacentes: 
            G.add_edges_from([(u, v)])
    
    nx.draw(
        G,                          #grafo em questão
        with_labels = True,
        font_size = 10,             #fonte
        node_color = "lightblue",   #cor do vértice
        edge_color = "gray",        #cor da aresta
        node_size = 600             #tamanho do vértice
    )

    print("Gerando Grafo...")

    plt.show()

#Função para listar arestas
def listar_arestas(arestas):
    print("Arestas: ")
    for u, v in arestas:
        print(f"({u}, {v})")

#função para calcular grau
def calcular_grau(grafo, vertice):
    if vertice in grafo.keys():
        print(f"{vertice} tem grau {len(grafo.get(vertice))}")
    else:
        print("Informe um vértice que exista no grafo.")

#funcao para listar vizinhos
def listar_vizinhos(grafo, vertice):
    if vertice in grafo.keys():
        print(f"Vizinhos de {vertice}: {grafo.get(vertice)}")
    else:
        print("Informe um vértice que exista no grafo.")

#funçao para verificar adjacência
def ver_adj(grafo, vertice1, vertice2):
     if vertice1 in grafo.get(vertice2):
        return True
     if vertice2 in grafo.get(vertice1):
         return True
     else:
         return False


if __name__ == "__main__":
    arquivo = "grafo 1.txt"

    tipo, arestas = ler_arquivivo(arquivo)

    if(tipo == "D"):
        dirigido = True
    else:
        dirigido = False

    grafo = construir_grafo(arestas, dirigido)

    imprimir_listadj(grafo)


    listar_arestas(arestas)
    listar_vizinhos(grafo, "S1")
    calcular_grau(grafo, "S1")


    if "S1" in grafo.keys() and "S2" in grafo.keys():
        if ver_adj(grafo, "S1", "S2") == True:
            print("São adjacentes")
        else:
            print("Não são adjacentes")
    else:
        print("Informe vértices que existam no grafo.")

    
    if "S10" in grafo.keys() and "S2" in grafo.keys():
        if ver_adj(grafo, "S10", "S2") == True:
            print("São adjacentes")
        else:
            print("Não são adjacentes")
    else:
        print("Informe vértices que existam no grafo.")





    plotar_grafo(grafo, dirigido)
    





