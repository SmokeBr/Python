from random import randint
from time import sleep
pc = randint(0,10)
print('-=-'*20)
print('adivinhe o numero que o Computador penso !!!')
print('-=-'*20)
jogador = int(input('Digite um numero e teste sua sorte: '))
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('Você ganhou !!!')
else:
    print('Perdeu o numero do Computador foi: {}'.format(pc))
print('-=-'*20)
