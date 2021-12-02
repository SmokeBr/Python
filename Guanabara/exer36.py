casa = float(input('Valor da Ta casa: R$ '))
salario = float(input('Seu do Comprador: R$ '))
anos = int(input('Quanto anos de Financiamento: '))
prestação = casa / (anos * 12)
minimo = prestação * 30 / 100
print('Para para a casa de R${:.2f} em {} anos'.format(casa,anos, end=''))
print('A prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('EMPRESTIMO LIBERADO !!!! ')
else:
    print('EMPRETIMO NEGADO SEU ARROMBADO !!!!!!')
