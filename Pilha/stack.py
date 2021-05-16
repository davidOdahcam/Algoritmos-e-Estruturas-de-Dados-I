class Stack:
  # Construtor
  def __init__(self, capacity):
    self.items = []
    self.capacity = capacity

  # Função que checa se a pilha está vazia
  def isEmpty(self):
    return self.items == []

  # Função que adiciona item à pilha
  def push(self, item):
    if (len(self.items) < self.capacity):
      self.items.append(item)
    else:
      print('Overflow')

  # Função que remove item da pilha
  def pop(self):
    if (self.isEmpty != True):
      self.items.pop()
    else:
      print('Underflow')

  # Função que retorna o item que está no topo da pilha
  def peek(self):
    return self.items[len(self.items)-1]

  # Função que retorna o tamanho da pilha
  def size(self):
    return len(self.items)

  # Função que imprime a pilha
  def show(self):
    if (self.isEmpty()):
      print('A pilha está vazia!')
    else:
      for i in self.items[::-1]:
        print(i)