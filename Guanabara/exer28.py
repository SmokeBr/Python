from random import randint
from time import sleep
pc = randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero de 0 a 5 .Tente Adivinhar ')
print('-=-'*20)
jogador = int(input('e que numero pensei ??? '))
print('PROCESSANDO')
sleep(2)
if jogador == pc:
    print('PARABENS VOCE GANHOU  !!!!!!!! ')
else:
    print('PC ganhou ele pensou em {} e o jogador em {}'.format(pc,jogador))
