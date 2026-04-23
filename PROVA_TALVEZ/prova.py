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

def merge_sort(L):
    if len(L) < 2:
        return L
    else:
        return merge(merge_sort(L[:(len(L)//2)]), merge_sort(L[len(L)//2:]))

L = [5, 3, 6, 1, 10, 33, 22, 14, 10]

print(merge_sort(L))
