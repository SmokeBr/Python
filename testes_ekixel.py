import pandas as pd
import numpy as np

col = 'Prova01 Prova02 Prova03 Prova04'.split()
lin = 'Ana Joana Laura Paulo Pedro Maria Estephano Carlos Eduardo'.split()
notas = np.random.randint(1,10,36).reshape(9,4)

dados = pd.DataFrame(data = notas, index = lin, columns = col)

dados.to_excel('notas_turma.xls')
