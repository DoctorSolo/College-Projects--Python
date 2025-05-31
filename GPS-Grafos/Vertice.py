# from arquivo import classe
from Aresta import Aresta

class Vertice:
    def __init__(self, label):
        self.Label = label # Rótulo ou ID do vértice
        self.Adjacencias = [] # Lista vazia (arestas) de adjacências 
    
    def __str__(self):
        return self.Label
    
    # Adiciona uma nova adjacência para este vértice
    # A origem é o próprio vértice (self)
    def Add_Adjacencia(self, destino, peso):
        novaAresta = Aresta(self, destino, peso)
        self.Adjacencias.append(novaAresta)
        
    def Show_Adjacencias(self):
        print(f'Vértice: {self.Label}')
        for aresta in self.Adjacencias:
            print(f'\t{aresta}')
        
