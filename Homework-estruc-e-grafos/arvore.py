from No import No

class Arvore:
    #inicia a arvore (Raiz = null)
    def _init_(self):
        self.Raiz = None
        
    def Add(self,novoValor):
        #cria um novo nó pra o novo Valor
        novoNo = No(novoValor)
        
        #verifica se a arvore esta vazia
        if(self.Raiz == None):
            #a arvore esta vazia então novoNo
            #passa a ser a Raiz
            self.Raiz = novoNo
        else:
            self.Raiz.Add(novoNo)
        
     # Método para remover um nó com um valor específico
    def Remover(self, valor):
        self.Raiz = self._remover_no(self.Raiz, valor)
    
    def _remover_no(self, raiz, valor):
        if raiz is None:
            return raiz

        if valor < raiz.Info:
            raiz.Sae = self._remover_no(raiz.Sae, valor)
        elif valor > raiz.Info:
            raiz.Sad = self._remover_no(raiz.Sad, valor)
        else:
            # Nó com apenas um filho ou nenhum
            if raiz.Sae is None:
                return raiz.Sad
            elif raiz.Sad is None:
                return raiz.Sae
            
            # Nó com dois filhos, pegar o sucessor (menor na subárvore direita)
            temp = raiz.Sad.encontrar_minimo()
            raiz.Info = temp.Info
            raiz.Sad = self._remover_no(raiz.Sad, temp.Info)

        return raiz

    # Método para podar a árvore, removendo todas as folhas
    def Podar(self):
        self.Raiz = self._podar(self.Raiz)
    
    def _podar(self, no):
        if no is None:
            return None
        
        if no.Sae is None and no.Sad is None:
            return None
        
        no.Sae = self._podar(no.Sae)
        no.Sad = self._podar(no.Sad)
        
        return no

    def __str__(self):
        return f'Raiz: {self.Raiz}'
        