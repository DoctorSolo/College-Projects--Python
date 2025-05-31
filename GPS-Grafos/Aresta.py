class Aresta:
    def __init__(self, origem, destino, peso = 1):
        self.Origem = origem
        self.Destino = destino
        self.Peso = peso

    def __str__(self):
        return f'{self.Origem} --> {self.Destino}: {self.Peso}'
    