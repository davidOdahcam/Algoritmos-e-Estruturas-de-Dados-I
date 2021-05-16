class Queue:
  # Construtor
  def __init__(self, capacity):
    self.items = []
    self.capacity = capacity

  # Função que verifica se a fila está vazia
  def isEmpty(self):
    return self.items == []

  # Função que empilha
  def enqueue(self, item):
    if (len(self.items) < self.capacity):
      self.items.insert(0,item)
    else:
      print('Overflow')

  # Função que desempilha
  def dequeue(self):
    if (self.isEmpty != True):
      return self.items.pop()
    else:
      print('Underflow')

  # Função que retorna o tamanho da fila
  def size(self):
    return len(self.items)

  # Função que realiza busca
  def search(self, item):
    for i in range(len(self.items)):
      if (item == self.items[i]):
        print('O elemento {} existe e está na posição {}'.format(item, i))
        return
    print('O elemento não foi encontrado!')
  
  def show(self):
    for i in self.items[::-1]:
      print(i, end=" | ")