from marvel import Marvel

m = Marvel(PUBLIC_KEY = 'ae1ed95095975c3c640f74f3120c11b3'
,PRIVATE_KEY = 'c4d2cd4702bb95599bf49478be569e0d4e178e8b')

# getting the characters object
characters = m.characters 
  
# serial code of your favourite character
# this can be different according to your preference
x = 1011334 
for n in range (0, 6): 
    
      # serach for comics of this character
    all_characters=characters.comics(x) 
      
    x = x+1 
    for i in range (1,12):
      print(all_characters['data']['results'][int(i)]['title'])
