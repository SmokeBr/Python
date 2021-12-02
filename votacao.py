
from selenium import webdriver

'''url = 'https://afazenda.r7.com/a-fazenda-12'

driver = webdriver.Firefox()
driver.get(url)

a1 = find_element_by_name("voting-button--hidden").click()'''

driver = webdriver.Firefox()
driver.get('https://google.com.br')
driver.find_element_by_name('q').send_keys('Aureo cezar')
driver.find_element_by_name('btnK').click()

