import pandas as pd
import win32com.client as win32

#importar a base de dados
tabelas_vendas = pd.read_excel('Vendas.xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None) #mostrar máximo de coluna
print(tabelas_vendas)

print('-'*45)

#faturamento de cada loja
#para filtrar mais de uma coluna, use dois colchetes
faturamento = tabelas_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum() # filtrou as tabelas e somou o valor total
print(faturamento)

print('-'*45)

#quantidade de produtos vendidos de cada loja
quantidade = tabelas_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-'*45)

#ticket médio por produto de cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame() #serve para transformar em tabela, pq quando faz um cálculo de colunas ele transforma em uma série de dados
print(ticket_medio)

#enviar relatório para um email
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'geovanacastro0712@outlook.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Atte.,</p>
<p>Geovana</p>
'''

mail.Send()

print('Email Enviado')