nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))#deixa o nome no meio
print('Prazer em te conhecer {:=^20}!'.format(nome))#imprimi =======oi======!
n1 = int(input('Digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2#\n pula a linha
print('A soma foi {}, o produto é {} e a divisão é {:.3f} '.format(s,m,d), end=' ')#mostrar somente 3 casa decimais flutuantes{:.3f}
print('Divisão inteira {} e a potencia {}'.format(di,e))#end='' nao pula a linha msm com mais de um print fica tudo na msm linda 
            
