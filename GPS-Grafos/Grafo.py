# from arquivo import classe
import heapq
from Vertice import Vertice


class Grafo:
    def __init__(self):
        self.Vertices = [] # Cria uma lista vazia de vértices
        
    def __str__(self):
        return f'Este grafo possui {len(self.Vertices)} vértices.'
    
    def Add_Vertice(self, label):
        # Testar se o vértice já existe
        if label not in self.Vertices:
            novoVertice = Vertice(label)
            self.Vertices.append(novoVertice)
        else:
            print("Erro: Vértice já cadastrado")
            
    def Show_Vertices(self):
        for vertice in self.Vertices:
            #print(vertice)
            vertice.Show_Adjacencias()
        # Alterar este método para mostrar as 
        # Adjacências, para a próxima aula        
            
    # Implementar para a próxima aula
    # Vou sortear 3 alunos para mostrar :)    
    def Add_Aresta(self, label_origem, label_destino, peso):
        # parâmetro label_origem será uma string com o label da cidade de origem
        # parâmetro label_destino será uma string com o label da cidade de destino
        # 1) Buscar o objeto "origem" na lista de vertices (origem)
        origem = None
        for vertice in self.Vertices:
            if vertice.Label == label_origem: # verifica se é o vértice com o label que estou procurando
                origem = vertice # salvo o objeto com o label que eu estava procurando
                break  # saio do loop
                
        # 2) Buscar o objeto "destino" na lista de vertices (destino)
        destino = None
        for vertice in self.Vertices:
            if vertice.Label == label_destino: # verifica se é o vértice com o label que estou procurando
                destino = vertice # salvo o objeto com o label que eu estava procurando
                break  # saio do loop
            
        # 3) Chamar o "Add_Adjacencia" do objeto (origem) e passar
        #    (destino) como parâmetro   
        if origem != None and destino != None:
            origem.Add_Adjacencia(destino, peso)
            destino.Add_Adjacencia(origem, peso)
        else:
            print('Informe origem e destino válido')
    
    
    def Dijkstra(self, inicio_label):
        distancias = {vertice.Label: float('infinity') for vertice in self.Vertices}
        # Inicializa distâncias
        distancias[inicio_label] = 0
        pq = [(0, inicio_label)]  # Fila de prioridade

        while len(pq) > 0:
            distancia_atual, vertice_atual_label = heapq.heappop(pq)
            # Extrai o vértice com menor distância

            # condição de verificação
            if distancia_atual > distancias[vertice_atual_label]:
                continue

            # Encontrar o objeto vertice_atual correspondente ao vertice_atual_label
            vertice_atual = None
            for vertice in self.Vertices:
                if vertice.Label == vertice_atual_label:
                    vertice_atual = vertice
                    break

            if vertice_atual is None:
                continue  # Se o vértice não for encontrado, pula para o próximo

            # Iterar sobre as adjacências do vértice atual
            for aresta in vertice_atual.Adjacencias:
                distancia = distancia_atual + aresta.Peso

                if distancia < distancias[aresta.Destino.Label]:
                    distancias[aresta.Destino.Label] = distancia
                    heapq.heappush(pq, (distancia, aresta.Destino.Label))
                    # Atualiza a fila de prioridade

        return distancias

                    
        