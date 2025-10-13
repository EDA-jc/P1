import grafo as gr

arquivo = "grafo 1.txt"

tipo, arestas = gr.ler_arquivivo(arquivo)
if tipo == "D":
    dirigido = True
else:
    dirigido = False

grafo = gr.construir_grafo(arestas, dirigido)  #construção do grafo

i = 1

while i >= 1 and i <= 3: 
    i = int(input("1. Funções Básicas \n2. Vizualizar Lista Adjacência \n3. Vizualizar Grafo\n"))
    if i == 1:
        j = int(input("1. Listas Arestas \n2. Listar Vizinhos \n3. Calcular Grau \n4. Verificar Adjacênciaz\n "))
        if j == 1:
            gr.listar_arestas(arestas)

        if j == 2:
            vertice = input("Informe o vértice que você deseja visualizar os vizinhos: ").upper()
            gr.listar_vizinhos(grafo, vertice)

        if j == 3:
            vertice = input("Informe o vértice: ").upper()
            gr.calcular_grau(grafo, vertice)

        if j == 4:
            vertice1 = input("Informe o primeiro vértice: ").upper()
            vertice2 = input("Informe o segundo vértice: ").upper()
            if vertice1 in grafo.keys() and vertice2 in grafo.keys():
                if gr.ver_adj(grafo, vertice1, vertice2) == True:
                    print("São adjacentes")
                else:
                    print("Não são adjacentes")
            else:
                print("Informe vértices que existam no grafo.")

    if i == 2:
        gr.imprimir_listadj(grafo)
    if i == 3:
        gr.plotar_grafo(grafo, dirigido)
