from random import randint

v =0
while True:
    jogador = int(input('Digite um valor:  '))
    pc = randint(0,10)
    total = jogador + pc
    tipo = ''

    while tipo not in 'PI':
            tipo = str(input('PAR OU IMPAR Digite P para Par e I para Impar [P/I]')).strip().upper()[0]
        print(f'Voce Jogou: {jogador} e o Computador: {pc} Total de: {total}', end='')
        print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
        if tipo == 'P':
            if total % 2 == 0:
                print('VOCE VENCEU')
                v += 1
            else:
                print('VOCE PERDEU')
                break
        elif tipo == 'I':
                if total % 2 == 1:
                    print('VOCE VENCEU')
                    v += 1
                else:
                    print('VOCE PERDEU !!!')
                    break
        print('VAMOS JOGAR NOVAMENTE ')
    print(f'GAME OVER !!! VOCE VENCEU {v} VEZES !')
