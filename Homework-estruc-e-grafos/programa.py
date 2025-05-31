from No import No
from arvore import Arvore

print("Árvore Binarias do Lajota")
arvore = Arvore()
arvore.Add(10)
arvore.Add(8)
arvore.Add(5)
arvore.Add(15)
arvore.Add(12)

print(arvore)

# Testando remoção
arvore.Remover(8)
print("Após remoção de 8:")
print(arvore)

# Testando poda
arvore.Podar()
print("Após poda:")
print(arvore)