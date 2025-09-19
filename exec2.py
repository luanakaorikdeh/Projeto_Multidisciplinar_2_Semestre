# Pesquisa Binária

novoArr = []
menor = 0
chute = 0
i = 0
maior = 0
meio = (menor + maior) // 2


import time
inicio = time.perf_counter()

while i < 1000001:
  novoArr.append(i)
  i += 1

maior = len(novoArr) - 1

escolha = int(input('Digite um número entre 1 e 1000000:'))

while escolha < 1 or escolha > 1000000:
  print('Número inválido, tente novamente.')
  escolha = int(input('Digite um número entre 1 e 1000000:'))

while menor <= maior:
  meio = (menor + maior) // 2
  chute = novoArr[meio]
  if chute == escolha:
    print(f'O número escolhido foi {chute}.')
    break
  elif chute < escolha:
    menor = meio + 1
  else:
    maior = meio - 1

tempo_fim = time.perf_counter()

tempo_total = int(tempo_fim - inicio)
 
 
print(f'Tempo de execução: {tempo_total}s')