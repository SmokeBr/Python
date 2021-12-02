import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto numero: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem de apresentação será: ')
print(lista)
