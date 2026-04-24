def head(L):
    if not L:
        return None
    else:
        return L[0]

def tail(L):
    if not L:
        return []
    else:
        return L[1:]

def last(L):
    return L[-1]
def init(L):
    return L[:-1]

def fatorial(N):
    
    if N == 1:
        return 1

    return N * fatorial(N - 1)


def q_7(N):
    if N == 0:
        return 1 
    return 1/fatorial(N) + q_7(N - 1)

def q_8_aux(soma = 0):
    x = int(input())
    if x == 0:
        return soma 
    elif x < 0:
        return q_8_aux(soma+x)
    else:
        return q_8_aux(soma)

def size(L):
    if not L:
        return 0
    return 1 + size(tail(L))

def prime_aux(N, dividend = 2):
    if dividend <= 1:
        return False 

    elif dividend > int(N**(1/2)):
        return True  

    elif N % dividend == 0:
        return False

    else:
        return prime_aux(N, dividend + 1)

def prime(N):
    return prime_aux(N)

def first_primes_aux(N, actual=2 ,count=[], counter = 0):
    if N == counter:
        return count 
    elif prime(actual):
        return first_primes_aux(N, actual + 1, count + [actual], counter + 1)
    else:
        return first_primes_aux(N, actual + 1, count, counter)

def first_primes(N):
    return first_primes_aux(N)

def concatena(L1, L2):
    
    if not L2:
        return L1
    
    return concatena(L1 + [head(L2)], tail(L2))    

def soma(L):
    if not L:
        return 0
    
    return head(L) + soma(tail(L))

def produto(L):
    if not L:
        return 1
    return head(L) * produto(tail(L))

def pertence(L, e):
    if not L:
        return False 
    elif head(L) == e:
        return True 
    return pertence(tail(L), e) 

def union(L1, L2):
    if not L2:
        return L1
    if not pertence(L1, head(L2)):
        return union(L1 + [head(L2)], tail(L2))
    return union(L1, tail(L2))

def greater_aux(L, n, count=0):
    if not L:
        return count 
    if head(L) > n:
        return greater_aux(tail(L), n, count + 1)

    return greater_aux(tail(L), n, count)

def greater(L, n):
    return greater_aux(L, n)

def greater_list_aux(L, n, new_list =[]):
    if not L:
        return new_list
    if head(L) > n:
        return greater_list_aux(tail(L), n, new_list + [head(L)])
    return greater_list_aux(tail(L), n, new_list)

def greater_list(L, n):
    return greater_list_aux(L, n)

def invert_list(L):
    if not L:
        return []
    return [last(L)] + invert_list(init(L))

def pa_gen_aux(L, new_word = ""):
    if not L:
        return new_word

    return pa_gen_aux(init(L), new_word + last(L)) 

def pa_gen(L):
    return pa_gen_aux(L, L)

def strip_aux(L1, L2, new_list =[]):
   
    if not L2:

        return new_list
    
    elif pertence(L1, head(L2)): #pertence a parada
     
        return strip_aux(L1, tail(L2), new_list)
    
    else:
       
        return strip_aux(L1, tail(L2), new_list + [head(L2)])
def strip(L1, L2):
    return strip_aux(L1, L2)

print(strip([1, 2, 3, 4], [1, 5, 2,4, 6, 7]))
