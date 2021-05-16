from node import Node

# Definindo a classe da lista encadeada
class LinkedList:
  # Contrutor
  def __init__(self, capacity):
    self.head = None
    self.capacity = capacity

  # Função que adiciona um elemento ao início
  def addBegin(self, element):
    # Instanciando um novo nó
    node = Node(element)
    node.next = self.head
    self.head = node

  # Função que remove o elemento inicial
  def removeBegin(self):
    if self.head == None: # Checando se a lista está vázia
      print("A lista já está vazia!")
      return
    self.head = self.head.next

  # Função que converte uma lista encadeada em array simples
  def toList(self):
    node = []
    current = self.head

    while current: # Iterando a lista enquanto o nó for diferente de None
      node.append(current.data) # Adicionando o nó ao vetor
      current = current.next # Atualizando o nó que será avaliado para o próximo
    return node

  # Função que transforma array simples em lista encadeada
  def toLinkedList(self, array):
    for i in array[::-1]: # Iterar o vetor de trás para frente
      self.addBegin(i)

  # Função de ordenação: Merge Sort
  def mergeSort(self, array):
    if len(array) > 1:
      mid = len(array) // 2 # Calculando o meio do vetor
      left = array[:mid]
      right = array[mid:]

      self.mergeSort(left) # Chamando a função novamente até que o lado esquerdo seja completamente dividido
      self.mergeSort(right) # Chamando a função novamente até que o lado direito seja completamente dividido

      i = 0
      j = 0
      k = 0

      # Analisando e mesclando todas as divisões
      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          array[k] = left[i]
          i = i + 1
        else:
          array[k] = right[j]
          j = j + 1
        k = k + 1

      while i < len(left):
        array[k]=left[i]
        i = i + 1
        k = k + 1

      while j < len(right):
        array[k]=right[j]
        j = j + 1
        k = k + 1
    return array

  def __repr__(self):
    return str(self.head)