#Busca em Largura

from collections import deque

grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['claire'] = ['thom','jonny']
grafo['alice'] = ['peggy']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []


def pessoas_letra_a(pessoa):
  if pessoa[0] == 'a':
    return True
  else:
    return False

def pesquisa(nome):
  fila_de_pesquisa = deque()
  fila_de_pesquisa += grafo['voce']
  verificada = []
  nomesA = []
  while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa not in verificada:
      if pessoas_letra_a(pessoa):
        nomesA.append(pessoa)
      else:    
        fila_de_pesquisa += grafo[pessoa]
        verificada.append(pessoa)
  return nomesA

nomesA = pesquisa('voce')
print(f'As pessoas que o nome começa com A são: {nomesA}')