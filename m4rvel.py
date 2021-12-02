import json
from marvel import Marvel

conteudo = Marvel(PUBLIC_KEY = 'ae1ed95095975c3c640f74f3120c11b3'
,PRIVATE_KEY = 'c4d2cd4702bb95599bf49478be569e0d4e178e8b')

characters = conteudo.characters
comics = conteudo.comics
creators = conteudo.creators
events = conteudo.events
series = conteudo.series
stories = conteudo.stories

all_characters = characters.all()
character = characters.get(1011334)
quadrinhos = characters.comics(1011334)
thumb = characters.Image(1011334)
#code = characters.code(1011334)
print(character)
print(quadrinhos)
#print(code)

#thumbnail': {'path': 'http://i.annihil.us/u/prod/marvel/i/mg/c/e0/535fecbbb9784', 'extension': 'jpg'}


