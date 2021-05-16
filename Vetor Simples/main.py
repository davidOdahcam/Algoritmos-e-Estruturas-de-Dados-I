import time
import random

capacities = [10, 100, 1000, 10000, 100000, 1000000] # Capacidades solicitadas pelo professor

# Apesar de funcionar, preferi não considerar o cálculo do bubbleSort() por demorar de mais para obter resultado
def bubbleSort(array): # Função de ordenação: Bubble Sort
  length = len(array) # Guardando a quantidade de índices existentes no vetor
  for i in range(length - 1): # Iterando em todos os índices do vetor e evitando que seja executado um loop desnecessário
    for j in range(0, length - i - 1): # O último índice já está em seu lugar
      if array[j] > array[j + 1]: # Analisando se array[j] é maior do que array[j + 1]
        array[j], array[j + 1] = array[j + 1], array[j] # Realizando a troca de valores cajo array[j] seja maior do que array[j + 1]

# Função de ordenação: Selection Sort
def selectionSort(array): # Função de ordenação: Selection Sort
  for i in range(0, len(array)): # Iterando por todo o vetor
    minimum = i # Posição inicial para o menor valor dentro do vetor
    for j in range(i + 1, len(array)): # Iterando a partir do índice seguinte para encontrar um valor menor dentro do vetor
      if array[j] < array[minimum]: # Verificando o índice que vem logo em seguida aos já analisados
        minimum = j # Caso seja encontrado um valor menor, este mesmo valor deve ser armazenado na variável minimum
    array[i], array[minimum] = array[minimum], array[i] # Trocando o conteúdo do índice inicial com o índice com menor valor
    
# Função de ordenação: Merge Sort
def mergeSort(array):
  if len(array) > 1:
    mid = len(array) // 2 # Calculando o meio do vetor
    left = array[:mid]
    right = array[mid:]

    mergeSort(left) # Chamando a função novamente até que o lado esquerdo seja completamente dividido
    mergeSort(right) # Chamando a função novamente até que o lado direito seja completamente dividido

    i = 0
    j = 0
    k = 0

    # Analisando e mesclando todas as divisões
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      array[k]=left[i]
      i += 1
      k += 1

    while j < len(right):
      array[k]=right[j]
      j += 1
      k += 1
  return array

for c in capacities: # Realizando testes com os tamanhos solicitados pelo professor
  array = [] # Iniciando um vetor vázio

  # INSERÇÃO
  begin = int(round(time.time() * 1000)) # Marcando o início da execução
  for i in range(c):
    array.append(random.randint(0, c)) # Adicionando valores inteiros, entre 0 e a capacidade do loop, à lista
  end = int(round(time.time() * 1000)) # Marcando o fim da execução
  print('Tempo de execução para inserir {} elementos: {}ms'.format(c, (end - begin))) # Imprimindo o tempo de execução
  
  # ORDENAÇÃO
  begin = int(round(time.time() * 1000)) # Marcando o início da execução
  bubbleSort(array) # Chamando a função de ordenação
  end = int(round(time.time() * 1000)) # Marcando o fim da execução
  print('Tempo de execução para ordenar {} elementos: {}ms'.format(c, (end - begin))) # Imprimindo o tempo de execução

  # REMOÇÃO
  begin = int(round(time.time() * 1000)) # Marcando o início da execução
  for i in range(c):
    array.pop() # Removendo índice da lista
  end = int(round(time.time() * 1000)) # Marcando o fim da execução
  print('Tempo de execução para remover {} elementos: {}ms\n'.format(c, (end - begin))) # Imprimindo o tempo de execução

  del array # Desfazendo o vetor