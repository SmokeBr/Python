import random
from time import sleep

chute = random.randint(0,100)
print('Jogo Digite um numero de 0 a 100')
numero = int(input('Digite seu numero:  '))
print('===========Processando==========')
print('='*10,'Precessando','='*10)
sleep(2)
if numero == chute:
    print('Voce  venceu o PC Pararabens  !!!')
else:
    print(f'Voce pedeu o computador escolheu {chute} e voce escolheu {numero}')
