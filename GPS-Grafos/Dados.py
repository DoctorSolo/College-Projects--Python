from Grafo import Grafo

# Lista contendo os dados
cidades = ['Ituiutaba', 'Capinópolis', 'Trevão', 'Prata', 'Monte Alegre', 'Araguari', 'Uberlândia']
distan = [['Ituiutaba', 'Capinópolis', 30],['Ituiutaba', 'Trevão', 40],['Trevão', 'Prata', 70],['Trevão', 'Monte Alegre', 20],
        ['Uberlândia', 'Prata', 70],['Uberlândia', 'Monte Alegre', 60],['Uberlândia', 'Araguari', 30]]
dados = []

grafo = Grafo()

# Adiciona os dados
for dado in cidades:
    grafo.Add_Vertice(dado)

for o, des, dis in distan:
    grafo.Add_Aresta(o, des, dis)

# Para ver os vertices e sua distancia
grafo.Show_Vertices()

# Executa o algoritmo de Dijkstra a partir de cada cidade    
for cidade in cidades:
    distancias = grafo.Dijkstra(cidade)
        
    for vertice, distancia in distancias.items():
        dado_temp = {
            'Inicio'    :   cidade,
            'Destino'   :   vertice,
            'Distancia' :   distancia
        }
        dados.append(dado_temp) # Adiciona os dados temporarios a lista de dados principal
