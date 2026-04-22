#E eu achei que teria alguma dificuldade nessa matéria...

#Q_1 
def head(L):
    if not L:
        return None
    else:
        return L[0]
#Q_2
def tail(L):
    if not L:
        return None
    else:
        return L[1:]
#Q_3
def init(L):
    if not L:
        return None
    else: 
        return L[:-1]
#Q_4
def last(L):
    if not L:
        return None
    else:
        return L[-1]
#Q_5
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
#Q_6
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
#Q_7
def calculate_e(n):
    if n == 0:
        return 1
    else: #Erro nessa parte aqui! 
        #print(f"1/{n}! + ", end = ' ')
        return 1/fatorial(n) + calculate_e(n - 1)
#Q_8 
def sum_int(n=0): #N é o valor da soma
    print(f"Valor da soma está em {n}")
    valor_somado = int(input(""))
    if valor_somado == 0:
        return n 
    elif valor_somado < 0:
        #print(f"Era para ser {n - valor_somado}")
        return sum_int(n + valor_somado)
    else:
        return sum_int(n)
#Q_9
def real_counter(n=0): #N é a quantidade de valores negativos 
    print(n)
    valor_real = int(input(""))
    if valor_real < 0:
        return real_counter(n + 1)
    else:
        return real_counter(n)

#Q_10 
def list_size(L, soma=0):
    if not L:
        return soma
    else: #O que caralhos está errado aqui!
        #print("Estamos aqui")
        return list_size(tail(L), soma + 1)

#Q_11
def eh_primo(n, atual=2): #N é o valor que queremos verificar! 
    if n == atual: #Caso do 2, ou caso ele nn ache nenhum outro 
        return True
    elif n < atual:
        return False #Caso do 1 
    else:
        if n % atual == 0:
            return False 
        else:
            return eh_primo(n, atual + 1)
#Q_12
def first_primes(n, qtd_primos =0, atual=1):
    if n == qtd_primos: #Base da recursão 
        return 
    else:
        if eh_primo(atual):
            qtd_primos = qtd_primos + 1
            print(atual, end= ' ')
        return first_primes(n, qtd_primos=qtd_primos, atual=atual + 1)
#Q_13
def concatena_list(L_1, L_2):
    if not L_1:
        return L_2
    elif not L_2:
        return L_1
    else:
        L_1.append(head(L_2)) #Adicionamos o head, não sei se posso fazer isso de adicionar com o append! 
        return concatena_list(L_1, tail(L_2))

#Q_14
def exists(n, L): #Onde n é o elemento e L a lista
    if n == head(L):
        return True 
    elif not L:
        return False
    else:
        return exists(n, tail(L))
#Q_15 
def math_union(L_1, L_2):
    if not L_1:
        return L_2
    elif not L_2:
        return L_1
    else:
        if not exists(head(L_2), L_1):
            L_1.append(head(L_2))
        return math_union(L_1, tail(L_2))

#Q_16
def fun_greater_n(L, n, total=0):
    soma = total
    if not L:
        return total
    elif head(L) > n:
        soma = total + 1
    return fun_greater_n(tail(L), n, soma)
#Q_17
def fun_greater_n_list(L, n, new_list=[]):
    if not L:
        return new_list
    elif head(L) > n:
        new_list.append(head(L))
    return fun_greater_n_list(tail(L), n, new_list)

#Q_18
def invert_list(L):
    if not L:
        return L
    else:
        return [last(L)] + invert_list(init(L))
        
#Q_19 
def gera_palindromo(palavra, nova_palavra = [], atual_antiga = 0, atual_nova = 0, original_size = 0):
    palavra = list(palavra) 
    if not nova_palavra:
        nova_palavra = palavra #Os dois apontam para o mesmo endereço
        atual_antiga = list_size(palavra) #Definimos o tamanho atual como sendo esse e vamo adicionando e removendo 
        atual_nova = atual_antiga #Com isso vamos chamando recursivamente a 
        original_size = atual_antiga 
    if list_size(nova_palavra) == original_size * 2:
        nova_palavra = ''.join(nova_palavra)
        return str(nova_palavra) 
    else:
        nova_palavra.append(palavra[atual_antiga - 1])
        return gera_palindromo(palavra, nova_palavra, atual_antiga - 1, atual_nova + 1, original_size)

#Q_20
def recursion_strip(L_1, L_2):
    if not L_1:
        return L_2 
    else:
        item_to_remove = head(L_1)
        if exists(item_to_remove, L_2):
            L_2.remove(item_to_remove)
        return recursion_strip(tail(L_1), L_2)

#Q_21
def consoant_list(first_string, consoants, vowals = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']): 
    first_string = recursion_strip(list(consoants), list(first_string))  #Tiramos as consoantes
    first_string = recursion_strip(vowals, list(first_string))
    if not first_string:
        return True
    else:
        return False 
#Q_22_AUX
def compare(string, con):
    if not string:
        return False
    elif not con:
        return True 
    if head(string) == head(con):
        return compare(tail(string), tail(con))
    else:
        return compare(tail(string), con)

#Q_22
def matches(strings, con):
    func = lambda x: compare(x, con)
    return list(filter(func, strings))

#Q_23
def first_prime_greater(n):
    if not eh_primo(n + 1):
        return first_prime_greater(n + 1)
    else:
        return n + 1  

#Q_24
def primes(n, base =2):
    if n == 1:
        return []
    elif (n % base) == 0:
        return [base] + primes(n //base, base)
    else:
        return primes(n, first_prime_greater(base))

#Q_25_AUX
def prime_factors_aux(l, element):
    if not l:
        return []
    
    fun = (lambda x: x == element)
    fun_2 = (lambda x: x != element)
    new_list = list(filter(fun_2, l))
    return [(element,  len(list(filter(fun, l))))] + prime_factors_aux(new_list, head(new_list))

#Q_25 dava pra fazer tudo nessa prime_factors, mas fodasse!
def prime_factors(n):
    return prime_factors_aux(primes(n), head(primes(n)))

#Q_26 ESSA EU NÃO SEI COMO REFATORAR PARA FICAR BONITINHA!
def split_token(n, l):
    if not l:
        return []
    if head(l) != n:
        return [head(l)] + split_token(n, tail(l))
    elif head(l) == n:
        return [split_token(n, tail(l))]

#Q_27 DE VDD ENTENDI FOI NAD!
def join_token(n, l):
    fun = lambda acc, item: acc + [n] + item
    from functools import reduce

    return reduce(fun, l)

#Q_28_AUX
def split_half_1(n, l, count=0):
    if count == n //2:
        return []
    else:
        return [head(l)] + split_half_1(n, tail(l), count + 1) 

def split_half_2(n, l, count=0):
    if count == n//2:
        return []
    else:
        return split_half_2(n, init(l), count + 1) + [last(l)]

#Q_28
def split_half(l):
    if len(l) % 2 == 0:
        return [split_half_1(len(l), l), split_half_2(len(l), l)] 
    else:
        return [split_half_1(len(l) + 1, l), split_half_2(len(l), l)] 

#Q_29_AUX 
def pyths_aux(n, primer= 2, segun = 2):
    if primer >= n:
        return []
    elif segun >= n:
        return pyths_aux(n, primer + 1, 2)
    if ((primer ** 2) + (segun **2)) < n ** 2:
        return pyths_aux(n, primer, segun + 1)
    elif ((primer ** 2) + (segun **2)) == n** 2:
        return [(primer, segun, n), (segun, primer, n)]
    elif ((primer ** 2) + (segun **2)) > n ** 2:
        return pyths_aux(n, primer + 1, 2)
#Q_29
def pyths(n):
    return pyths_aux(n)
#Q_30_AUX_1
def fatores(n, divisor=1):
    if n == 0 or n <= divisor:
        return []
    else:
        if n % divisor == 0: #É um fator do numero
            return [divisor] + fatores(n, divisor + 1)
        else:
            return fatores(n, divisor + 1)

def sum_list(l):
    if not l:
        return 0
    else:
        return head(l) + sum_list(tail(l))
#Q_30
def perfects(n, atual= 3):
    x = fatores(atual)
    if not x or atual == n:
        return []
    else:
        if (sum_list(x) == atual):
            return [atual] + perfects(n, atual+ 1) 
        else:
            return perfects(n, atual + 1)
print(perfects(500))

