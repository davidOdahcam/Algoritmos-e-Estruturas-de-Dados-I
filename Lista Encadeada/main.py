import time
import random
from linkedList import LinkedList

capacities = [10, 100, 1000, 10000, 100000, 1000000] # Capacidades solicitadas pelo professor

for c in capacities:
  linkedList = LinkedList(c)
  # Marcando o início da execução
  begin = int(round(time.time() * 1000))
  for i in range(linkedList.capacity):
    linkedList.addBegin(random.randint(0, linkedList.capacity))
  # Marcando o fim da execução
  end = int(round(time.time() * 1000))
  # Imprimindo o tempo de execução
  print('Tempo de execução para inserir {} elementos: {}ms'.format(linkedList.capacity, (end - begin)))
  
  # Armazenando a lista encadeada em um vetor
  linkedList_array = linkedList.toList()

  # Marcando o início da execução
  begin = int(round(time.time() * 1000))
  for i in range(linkedList.capacity):
    linkedList.removeBegin()
  # Marcando o fim da execução
  end = int(round(time.time() * 1000))
  # Imprimindo o tempo de execução
  print('Tempo de execução para remover {} elementos: {}ms'.format(linkedList.capacity, (end - begin)))

  # Marcando o início da execução
  begin = int(round(time.time() * 1000))
  # Realizando a ordenação no array
  linkedList_array = linkedList.mergeSort(linkedList_array)
  # Convertendo o array para uma lista encadeada
  linkedList.toLinkedList(linkedList_array)
  # Marcando o fim da execução
  end = int(round(time.time() * 1000))
  # Imprimindo o tempo de execução
  print('Tempo de execução para ordenar {} elementos: {}ms\n'.format(linkedList.capacity, (end - begin)))

  # Desfazendo a lista encadeada e o array
  del linkedList, linkedList_array