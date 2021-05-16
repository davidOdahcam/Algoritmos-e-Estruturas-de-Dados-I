import time
import random
from fila import Queue

capacities = [10]

for c in capacities: # Fazendo com que todos os valores solicitados pelo professor sejam analisados em uma única execução
  queue = Queue(c) # Instanciando uma fila
  print(queue.isEmpty())
  # INSERÇÃO
  begin = int(round(time.time() * 1000)) # Marcando o início da execução
  for i in range(queue.capacity):
    queue.enqueue(random.randint(0, queue.capacity)) # Adicionando valores inteiros, entre 0 e a capacidade do loop, à fila
  end = int(round(time.time() * 1000)) # Marcando o fim da execução
  print('Tempo de execução para inserir {} elementos: {}ms'.format(queue.capacity, (end - begin))) # Imprimindo o tempo de execução

  # REMOÇÃO
  begin = int(round(time.time() * 1000)) # Marcando o início da execução
  for i in range(queue.capacity):
    queue.dequeue() # Removendo item da fila
  end = int(round(time.time() * 1000)) # Marcando o fim da execução
  print('Tempo de execução para remover {} elementos: {}ms\n'.format(queue.capacity, (end - begin))) # Imprimindo o tempo de execução

  # Desfazendo fila
  del queue