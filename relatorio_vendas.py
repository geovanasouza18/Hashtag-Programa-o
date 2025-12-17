import pandas as pd

#importar a base de dados
tabelas_vendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None) #mostrar máximo de coluna
print(tabelas_vendas)

#faturamento de cada loja
faturamento = tabelas_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum() # filtrou as tabelas e somou o valor total
print(faturamento)

#quantidade de produtos vendidos de cada loja
quantidade = tabelas_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

#ticket médio por produto de cada loja


#enviar relatório para um email