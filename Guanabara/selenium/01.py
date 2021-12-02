from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser =  Firefox()

browser.get(url)
sleep(1)
a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')

a.click()
a.click()
a.click()
a.click()

print(f'O texto de A: {a.text}')
print(f'O texto de P: {p.text}')
