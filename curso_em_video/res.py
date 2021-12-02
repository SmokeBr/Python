
import requests

url = requests.get('https://github.com/')

nome = str(input('Digite o nome do usuário: '))

resul = url + nome

print(resul.text)

