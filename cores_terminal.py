#print('\033[31mOlá Mundo !!! ')

#print('\033[31;43mOlá, Mundo !!! ')

#print('\033[4;34;42mAureo')

#print('\033[0;31;44mTESTE')

#print('\033[7;30mteste2')

#print('\033[31mAUREO CEZAR')


a = 555
b = 666
nome = 'Cezar'

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',}

print('OS valores são \033[32m{} e \033[31m{}'.format(a,b))

print('Olá muito prazer, {}{}{}'.format('\033[4;34m', nome,
                                         '\033[m'))

print('Meu nome é {}{}{} !!!'.format(cores['amarelo'], nome, cores['limpa']))