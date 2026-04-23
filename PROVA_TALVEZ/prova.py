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
numeros = [1, 2, 3, 4]
resultado = new_reduce(somar, numeros)
print(resultado)
