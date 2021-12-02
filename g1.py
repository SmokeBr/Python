from google import search

for resultado in search('"código logo jarvis" youtube', stop=10):
    print(resultado)