
import string

from numpy.testing.print_coercion_tables import print_coercion_table

#import pandas as pd

# Cria um dicionário onde cada letra é a chave e o número é o valor (A=1, B=2, etc.)
alfabeto_numerado = {letra: i for i, letra in enumerate(string.ascii_lowercase, start=1)}

# Exibe o resultado
print(alfabeto_numerado)
#alfabeto_numerado.head()

nome= input("pò bota seu nome:\n")
lista = list(nome)
variavel = tuple(lista)

print(variavel)
print(type(variavel))


print(type(alfabeto_numerado))
soma = 0
for i in range(len(variavel)): #len ver o tamanho do bagulho (La ele)
    numero = alfabeto_numerado[variavel[i]]
    soma = soma + numero
print(soma)


print("asdçfkhadsçofn")

   # print(nome)