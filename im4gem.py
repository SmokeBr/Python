import requests

url = 'http://imagens.us/times-futebol/corinthians/corinthians%20(29).jpg'

r = requests.get(url)

with open('img.jpg', 'wb') as f:
    f.write(r.content)
