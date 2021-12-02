num = int(input('Digite um numero inteiro: '))
print('''Escolha um das bases para Conversão:
[ 1 ] Converte para BINÀRIO
[ 2 ] Converte para OCTAL
[ 3 ] Converte para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} para BINÁRIO é igual {(bin(num)[2:])} ')
if opção == 2:
    print(f'{num} para OCTAL é igual {(oct(num)[2:])}')
elif opção == 3:
    print(f'{num} para HEXADECIMAL é igual {(hex(num)[2:])}')
else:
    print(f'Tente novamente !!! ')
