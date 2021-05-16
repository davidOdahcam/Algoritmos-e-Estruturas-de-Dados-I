import time
import random
from stack import Stack

capacities = [10, 100, 1000, 10000, 100000, 1000000]

# Fazendo com que todos os valores solicitados pelo professor sejam analisados em uma única execução
for c in capacities:
  stack = Stack(c) # Instanciando uma pilha

  # INSERÇÃO
  begin = int(round(time.time() * 1000)) # Marcando o início da execução
  for i in range(stack.capacity):
    stack.push(random.randint(0, stack.capacity)) # Adicionando valores inteiros, entre 0 e a capacidade do loop, à pilha
  end = int(round(time.time() * 1000)) # Marcando o fim da execução
  print('Tempo de execução para inserir {} elementos: {}ms'.format(stack.capacity, (end - begin))) # Imprimindo o tempo de execução

  # REMOÇÃO
  begin = int(round(time.time() * 1000)) # Marcando o início da execução
  for i in range(stack.capacity):
    stack.pop() # Removendo item da pilha
  end = int(round(time.time() * 1000)) # Marcando o fim da execução
  print('Tempo de execução para remover {} elementos: {}ms\n'.format(stack.capacity, (end - begin))) # Imprimindo o tempo de execução
  
  # Desfazendo pilha
  del stack