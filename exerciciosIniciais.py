# 1 - verificar se um número é par

def eh_par(x):
    if x%2 == 0:
        return True
    else:
        return False
        
# 2 - verificar se o número é um inteiro

def eh_inteiro(x):
    if x%1 == 0:
        return True
    else:
        return False
        
# 3 - soma os digitos de um número

def soma(n):
	n = str(n)
	total = 0
	for i in n:
		i = int(i)
		total = total + i
        return total
        
# 4 - Fatorial

def fatorial(x):
	fat = 1
	while x>0:
		fat *=x
		x -= 1

        return fat
        
# 5 - se um número é primo

def eh_prime(x):
    if(x < 2):
        return False
    elif (x == 2 or x == 3):
        return True
    else:
        for item in range(2,x):
            if (x % item == 0):
                return False
                break

        return True
        
# 6 - retorna a string invertida

def reverse(text):
    tam_len = len(text)-1
    tam = len(text)
    l = []
    while tam != 0:
        l.append(text[tam_len])
        tam_len -=1
        tam -=1
    
    return ''.join(l)
    
# 7 - Elimina as vogais

def tira_vogal(text):
    text = text.replace("a","")
    text = text.replace("e","")
    text = text.replace("i","")
    text = text.replace("o","")
    text = text.replace("u","")
    text = text.replace("A","")
    text = text.replace("E","")
    text = text.replace("I","")
    text = text.replace("O","")
    text = text.replace("U","")
    return text

""" 
8 - Jogo Scrabble - é um jogo em que os jogadores ganham pontos ao soletrar palavras. 
Cada letra tem o seu valor. 
(neste programa, deixamos de fora as pontuações por letras duplas e triplas e a pontuação por palavra).
"""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
	l = []
	
	word = word.lower()
	
	for a in word:
		l.append(score[a])
	return sum(l)
	
	
# 9 - retorna a quantidade de repetições feitas de um mesmo número em uma lista

def count(sequence, item):
    found = 0
    for i in range(0, len(sequence)):
        if sequence[i] == item:
            found += 1
    return found
    
# 10 - remove todos os números ímpares de uma lista

def tira_impares(d):
    imp = []
    for i in d:
        if i %2 == 0:
            imp.append(i)
    return 

# 11 - toma uma lista de inteiros como entrada e retorna o produto de todos os elementos da lista.

def produto(l):
    t = len(l)
    s = 1
    vezes = len(l)
    while vezes !=0:
        s *= l[0] 
        del l[0]
        vezes -=1
    return s
    
# 12 - toma uma lista como entrada e remove todos os elementos repetidos deixando apenas um de cada


def remove_duplicados(l):
    lista = []
    for i in l:
        if i not in lista:
            lista.append(i)
    return lista


# 13 - retorna a mediana de uma lista

def mediana(x):
    x = sorted(x)
    if len(x) % 2 != 0:
        med = x[len(x)/2]
    elif len(x) == 1:
        med = x[0]
    else:
        pos = len(x)/2
        med = (x[pos]+(x[pos-1]))/2.0
    return med
    
