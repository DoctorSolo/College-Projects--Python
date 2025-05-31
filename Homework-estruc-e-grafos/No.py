class No:
    
#inicia o objeto com valor iniciais para suapropriedades 
    def _init_(self,valor):
        self.Info = valor#informação a ser quardada no Nó
        self.Sae = None#sub arvore esquerda
        self.Sad = None#sub arvore direita
        
    
    #usando para o print do objeto
    def _str_(self):
            return print(f'Info : {self.Info} Sae: {self.Sae} Sad {self.Sad}')
        
    
    #adiciona filhos
    def Add(self,novoFilho):
        if(novoFilho.Info < self.Info):
            if(self.Sae == None):
                     self.Sae = novoFilho
            else: 
                self.Sae.Add(novoFilho)
            
        else:
            if(self.Sad == None):
                self.Sad = novoFilho
            else:
                self.Sad.Add(novoFilho)
    
    # encontra o mínimo valor na subárvore
    def encontrar_minimo(self):
        atual = self
        while atual.Sae is not None:
            atual = atual.Sae
        return atual
        
        
    