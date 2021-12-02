while True:
    n = int(input(f'Qual tabuda voce quer saber: '))
    print('=' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
        print('=' * 30)
    print('PROGRAMA ENCERADO NÃO PODE SER TABUADA NEGATIVA !!!')
