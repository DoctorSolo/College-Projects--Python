# Codigo desevolvido por:
#   @ Miguel Eduardo da Silva,
#   @ Jeferson Alves.



# Bibliotecas nescessarias
from time import time
from time import sleep

# tabela ira armazenar os dados
# do teste das questões
tabela = {
    "a)" : {},
    "b)" : {}
}


# Letra A da questão
def letraA(x, x1, n):
    tabelaTemp = {} # Declaro uma tabela temporaria
    lista = []  # Declaro a lista para adicionar os elementos
    cont = 0    # Declaro o contador
    
    # este for ira criar a lista com n elementos
    for i in range(n):
        lista.append(i)
    
    
    # O teste começa aqui
    
    # Para ser mais fiel ao exercicio
    # decidi criar um for que percorre
    # a lista para contar o numero de
    # passos
    x_existe = False    # Decidi definir duas variaveis booleanas para
    x1_existe = False   # informar se o numero existe.
    
    for i in range(n):
        cont += 1
        
        if x == i:
            cont += 1
            x_existe = True
            cont += 1

        if x1 == i:
            cont += 1
            x1_existe = True
            cont += 1
    
    # Caso as variaveis booleanas sejam verdadeiras
    # atribuiu a lista
    def existeValor(y, boleano, cont):
        if boleano:
            cont += 1
            tabelaTemp[f"{y+1} elemento"] = lista[y]
            cont += 1
        else:
            cont += 1
            tabelaTemp[f"{y+1} elemento"] = "Não existe"
            cont += 1
        return cont
    
    cont = existeValor(x, x_existe, cont)
    cont = existeValor(x1,x1_existe,cont)
    
    # No final o programa ira armazenar o contador
    # na tabela
    tabelaTemp["Contador"] = cont
    texteID = f"{n} elementos"          # Este ID serve para os valores não serem sobrescritos
    tabela["a)"][texteID] = tabelaTemp  # Em exercicio a) armazenar tabelaTemporaria



# Letra B da questão
def letraB(x, x1, n):
    tabelaTemp = {} # Declaro uma tabela temporaria
    lista = []  # Declaro a lista para adicionar os elementos
    
    # este for ira criar a lista com n elementos
    for i in range(n):
        lista.append(i)
    
    
    # O teste começa aqui
    t_inicial = time()
    
    # apenas subistiui o cont pelo sleep para um delay no codigo
    x_existe = False
    x1_existe = False
    
    for i in range(n):
        sleep(0.1)
        
        if x == i:
            sleep(0.1)
            x_existe = True
            sleep(0.1)
        
        if x1 == i:
            sleep(0.1)
            x1_existe = True
            sleep(0.1)
    
    # Caso as variaveis booleanas sejam verdadeiras
    # atribuiu a lista
    def existeValor(y, boleano):
        
        if boleano:
            sleep(0.1)
            tabelaTemp[f"{y+1} elemento"] = lista[y]
            sleep(0.1)
        else:
            sleep(0.1)
            tabelaTemp[f"{y+1} elemento"] = "Não existe"
            sleep(0.1)
    
    existeValor(x, x_existe)
    existeValor(x1, x1_existe)
    
    # O Texte termina aqui
    t_final = time()
    # para obter o tempo de execução e só tirar a diferença de
    # t_inicial e t_final e multiplicar por 1000 para obter valor
    # em ms
    t_total = int(f"{((t_final - t_inicial) * 1000):.0f}")
    # No final o programa ira armazenar o tempo 
    # em milisegundos na tabela
    tabelaTemp["tempo de execução"] = t_total
    texteID = f"{n} elementos"
    tabela["b)"][texteID] = tabelaTemp




# Codigos otimizados


# Letra A da questão
def letraAOtimizado(x, x1, n):
    tabelaTemp = {}
    lista = []  # Declaro a lista para adicionar os elementos
    cont = 0    # Declaro o contador
    
    # este for ira criar a lista com n elementos
    for i in range(n):
        lista.append(i)
    
    
    # O teste começa aqui  
    # Tenta passar o valor de x para a lista
    # se der errado o valor não existe
    def verificaLista(y, cont):
        
        try:
            cont += 1
            tabelaTemp[f"{y+1} elemento"] = lista[y]
            cont += 1
        # Se parar aqui é porque o numero passou
        # do limite da lista
        except IndexError:
            cont += 1
            # caso não exista o elemento a lista ira armazenar "Não existe"
            tabelaTemp[f"{y+1} elemento"] = "Não existe"
            cont += 1
        return cont
            
    cont = verificaLista(x, cont)
    cont = verificaLista(x1, cont)

    # No final o programa ira armazenar o contador
    # na tabela
    tabelaTemp["Contador"] = cont
    texteID = f"{n} elementos (Otimizado)"
    tabela["a)"][texteID] = tabelaTemp


# Letra B da questão
def letraBOtimizado(x, x1, n):
    tabelaTemp = {}
    lista = []  # Declaro a lista para adicionar os elementos
    
    # este for ira criar a lista com n elementos
    for i in range(n):
        lista.append(i)
    
    
    # O teste começa aqui
    t_inicial = time()
    
    # Apenas copiei o programa passado
    # dessa vez coloqui um delay de 0.1
    # para medirmos o tempo
    def verificaLista(y):    
        
        try:
            sleep(0.1)
            tabelaTemp[f"{y+1} elemento"] = lista[y]
            sleep(0.1)
        # Se parar aqui é porque o numero passou
        # do limite da lista
        except IndexError:
            sleep(0.1)
            # caso não exista o elemento a lista ira armazenar "Não existe"
            tabelaTemp[f"{y+1} elemento"] = "Não existe"
            sleep(0.1)

    verificaLista(x)
    verificaLista(x1)
    
    t_final = time()
    t_total = int(f"{((t_final - t_inicial) * 1000):.0f}")
    # No final o programa ira armazenar o tempo 
    # em milisegundos na tabela
    tabelaTemp["tempo de execução"] = t_total
    texteID = f"{n} elementos (Otimizado)"
    tabela["b)"][texteID] = tabelaTemp