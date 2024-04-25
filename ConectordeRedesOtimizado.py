"""
Enunciado:
Você foi solicitado pela Prefeitura de Maricá para desenvolver um algoritmo que otimize a conexão de sensores pluviométricos em uma rede que compreende sensores e conexões com fios entre eles. O objetivo é otimizar a conectividade da rede usando exatamente W fios do seu estoque para maximizar o número de computadores que podem ser conectados juntos dentro das restrições dadas. Os sensores são considerados conectados se compartilharem uma conexão com fio direta ou indireta, e o valor de W sempre será menor que o número de redes isoladas na configuração dada, podendo até ser zero.

Formato de Entrada:

    S: Número de sensores na rede.
    A: Número de arestas conectando os computadores.
    W: Número de cabos disponíveis no seu estoque.
    A lista de arestas, onde cada par (a_i, b_i) representa uma conexão dos fios entre os computadores com IDs a_i e b_i, respectivamente.
    A list

Formato de Saída:
Um único número inteiro representando o tamanho da maior rede (computadores conectados) que pode ser formada após conectar W fios.

Restrições:

    1 ≤ S ≤ 10^5: O número de sensores na rede.
    1 ≤ A ≤ 2 * 10^5: O número de conexões com fios entre os sensores.

A solução do algoritmo será desenvolvida utilizando a biblioteca NetworkX para manipulação de grafos e Matplotlib para visualização gráfica da rede.

"""

# Objetivo: Conectar sensores pluviométricos para otimizar a conectividade da rede.
# Usaremos exatamente W fios para conectar o maior número possível de computadores.
# Uma conexão é válida se os sensores estiverem conectados direta ou indiretamente.
# O valor de W é sempre menor que o número de redes isoladas, podendo ser zero.
# O desafio é criar um algoritmo para maximizar o número de computadores conectados.
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Função para conectar os maiores subgrafos isolados usando fios W
def conectar_maior_rede(G, W):
    subgrafos = list(nx.connected_components(G))
    heap = [(-len(subgrafo), subgrafo) for subgrafo in subgrafos]
    heapq.heapify(heap)

    while W > 0 and len(heap) > 1:
        _, sg1 = heapq.heappop(heap)
        _, sg2 = heapq.heappop(heap)
        
        # Assumindo que sg1 e sg2 são os sets dos nós de cada subgrafo
        nodo1 = next(iter(sg1))  # Escolhe um nó arbitrário de sg1
        nodo2 = next(iter(sg2))  # Escolhe um nó arbitrário de sg2

        # Conecta os subgrafos sg1 e sg2
        G.add_edge(nodo1, nodo2)
        W -= 1  # Decrementa o contador de fios disponíveis

        # Junta os subgrafos sg1 e sg2 em um novo subgrafo sg
        sg = sg1.union(sg2)
        heapq.heappush(heap, (-len(sg), sg))

    # Retorna o tamanho do maior subgrafo conectado
    if heap:
        _, maior_subgrafo = heap[0]
        return len(maior_subgrafo)
    return 0

# Entrada de dados conforme enunciado
S, A, W = 13, 11, 2
conexoes = [
    (1, 2), (3, 4), (4, 5), (3, 6), (7, 8), (8, 9), (7, 10),
    (8, 10), (8, 9), (11, 12), (11, 13), (12, 13)
]

# Cria o grafo e adiciona as arestas
G = nx.Graph()
G.add_edges_from(conexoes)

# Chama a função para conectar os subgrafos e imprime o resultado
tamanho_maior_rede = conectar_maior_rede(G, W)
print(f'O tamanho da maior rede que pode ser formada é: {tamanho_maior_rede}')

# Visualização do grafo após otimização
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', edge_color='gray')
plt.title('Rede de Sensores e Computadores após Otimização')
plt.show()


# Análise de Complexidade:
# A complexidade temporal do algoritmo é O(n log n) para ordenação dos subgrafos,
# e a complexidade espacial é O(n + m) devido ao armazenamento do grafo e dos subgrafos.

