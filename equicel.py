import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel(r"/home/cezar/Área de Trabalho/Pessoas.xlsx")

plt.plot(x["Idade"])
plt.show()

print(x)
print(x['Idade'][1])
