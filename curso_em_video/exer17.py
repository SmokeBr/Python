from math import hypot
cd=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adiacente: '))
hi=hypot(cd,ca)
print('A hipotenusa vai medir {:.2f} '.format(hi))
