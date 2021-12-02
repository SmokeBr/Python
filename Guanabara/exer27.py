n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Muito prazer em te conhecer {(nome[0])} ')
print(f'Seu ultimo nome é {(nome[len(nome)-1])}')
