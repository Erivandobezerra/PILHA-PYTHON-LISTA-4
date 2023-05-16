class Item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, valor):
        novoItem = Item(valor)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
        
    def pop(self): 
        if self.size == 0:
            raise Exception("A pilha está vazia!")
        valor = self.top.valor
        self.top = self.top.next
        self.size -= 1
        return valor
    
    def top(self):
        if self.size == 0:
            raise Exception ("A pilha está vazia!")
        return self.top.valor

    def is_empty(self):
        return self.size == 0
    
    def __len__(self): 
        return self.size

def verificar(exp):
    pilha = Pilha()
    for p in exp:
        if p == '(':
            pilha.push(p)
        elif p == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.push(p)
    return pilha.is_empty()

exp = input('Digite uma expressão matemática : ')
if verificar(exp):
    print('Parênteses estão balanceados.')
else:
    print('Parênteses desbalanceados.')