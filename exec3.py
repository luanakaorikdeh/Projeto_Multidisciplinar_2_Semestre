#Ordenação de lista - Quick Sort.

import random
novoArr = [random.randint(-1,1001) for i in range (10)]
pos_meio = []

print(f'Primeira lista não organizada: {novoArr}')

def quick_sort(novoArr):
    if len(novoArr) < 2:
        return novoArr
    else:
        pivo = novoArr[len(novoArr) // 2]
        menores = [i for i in novoArr if i < pivo]
        iguais = [i for i in novoArr if i == pivo]
        maiores = [i for i in novoArr if i > pivo]
        return quick_sort(menores) + iguais + quick_sort(maiores)     
    
lista_organizada = quick_sort(novoArr)

print(f'Segunda lista organizada: {lista_organizada}')