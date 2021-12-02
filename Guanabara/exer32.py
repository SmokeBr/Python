from date import date
ano = int(input('Digite um ano para analisar ou digite [0] para saber o ano'))
if ano == 0:
    ano = date.today().year()
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} ´ BISSEXTO'.format(ano))
else:
    print('O ano {} NÂO É BISSEXTO'.format(ano))
