a1 =  str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiusculo fica: {(a1.upper())}')
print(f'Seu nome em minusculo fica: {(a1.lower())}')
print('Seu nome tem ao todo {} letras'.format(len(a1) - a1.count('')))
separa = a1.split()
print('Seu primeiro nom é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


