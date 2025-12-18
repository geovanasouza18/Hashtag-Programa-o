import pandas as pd
import smtplib
import email.message

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
def enviar_email():
    corpo_email = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">
        <p>Prezados,</p>
    
        <p>Segue o Relatório de Vendas por cada Loja.</p>
    
        <p><strong>Faturamento:</strong></p>
        {faturamento.to_html(index=False, border=1)}
    
        <p><strong>Quantidade Vendida:</strong></p>
        {quantidade.to_html(index=False, border=1)}
    
        <p><strong>Ticket Médio:</strong></p>
        {ticket_medio.to_html(index=False, border=1)}
    
        <p>Qualquer dúvida estou à disposição.</p>
    
        <p>Atte.,<br>Geovana</p>
    </body>
    </html>
    """
    msg = email.message.Message()
    msg['From'] = f'geovana.developer@gmail.com'
    msg['To'] = f'geovana.developer@gmail.com'
    password = 'pdyb ulob eufx ugfg'
    msg['Subject'] = 'Relatório de Vendas por Loja'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s= smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()



print('Email enviado com sucesso 📤🔥')
