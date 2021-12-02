import requests
url = "https://api.github.com/users/"
user=str(input("Digite o usuario: "))
dados=requests.get(url+user)
print(dados.json()["name"])
