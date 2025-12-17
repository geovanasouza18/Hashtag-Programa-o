import pandas as pd

#importar a base de dados
tabelas_vendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None) #mostrar máximo de coluna
print(tabelas_vendas)

#faturamento de cada loja


#quantidade de produtos vendidos de cada loja

#ticket médio por produto de cada loja

#enviar relatório para um email