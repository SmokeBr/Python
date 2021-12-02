import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
soup = BeautifulSoup(page.text, 'html.parser')

container = soup.findAll("div", {"class": "maincounter-number"})
cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip()

print(cases)
print(deaths)
print(recovered)
