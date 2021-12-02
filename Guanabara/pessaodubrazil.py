from cidadaobr import CidadaoBrasileiro

cidadao = CidadaoBrasileiro(nome='Yan Orestes', data_nascimento='23/10/2000', estado='SP')
print(c.json())
print('\n' + cidadao['nome'])
