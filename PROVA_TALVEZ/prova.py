
from functools import reduce
def head(L):
    if not L:
        return None 
    return L[0]

def tail(L):
    if not L:
        return []
    return L[1:]

def last(L):
    if not L:
        return None
    return L[-1]

def init(L):
    if not L:
        return []
    return L[:-1]

#Bruno se vc cobrar isso vai toma um belo café cara
def merge(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    elif head(a) < head(b):
        return [head(a)] + merge(tail(a), b)
    else:
        return [head(b)] + merge(a, tail(b))
#ORDENAÇÃO
def merge_sort(L):
    if len(L) < 2:
        return L
    else:
        return merge(merge_sort(L[:(len(L)//2)]), merge_sort(L[len(L)//2:]))
#FAZENDO UM MAP PROPRIO COM RECURSAO SLA O QUE 
def new_map(func, lista):
    if not lista:
        return [] 
    return [func(head(lista))] + new_map(func, tail(lista))

def func(n):
    return len(n)
#FAZENDO UM FILTER PROPRIO COM RECURSAO, TAMBÉM EASY PRA CACETE
def new_filter(func, lista):
    if not lista:
        return []
    elif func(head(lista)): #Entra na lista
        return [head(lista)] + new_filter(func, tail(lista))
    else: #SAI FORA!
        return new_filter(func, tail(lista))

def filter_func(x):
    if x < 18:
        return False
    return True
#TENTE ENTENDER ESSA DESGRAÇA 
def new_reduce_aux(func, lista, acc):
    if not lista:
        return acc
    return new_reduce_aux(func, tail(lista), func(acc, head(lista)))

def new_reduce(func, lista):
    return new_reduce_aux(func, tail(lista), head(lista))

def somar(acc, item):
    return acc + item

def counter(L, item, acc=0):
    
    if not L:
        return acc
    if item == head(L):
        return counter(tail(L), item, acc + 1)
    else:
        return  counter(tail(L), item, acc )


#SELECTION SORT FAZENDO O TESTE. FUNCIONA SEM ELEMENTOS REPETIDOS, FODASSE!
def selection_sort(L):
    if not L:
        return []
    min_value = reduce(lambda x, y: x if x<y else y, L)
    return [min_value] * counter(L, min_value) + selection_sort(list(filter(lambda x: x != min_value, L)))

print(selection_sort([94, 54, 57, 57, 92, 91, 101, 101, 24, 23, 21, 21, 12, 19, 71, 73, 73, 494, 1101, 1, 1, 5, 7, 99]))
