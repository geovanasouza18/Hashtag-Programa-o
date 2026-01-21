texto = 'Geovana é linda'
print(len(texto))

faturamento = 20000
custo = 15400
lucro = faturamento - custo
print(f'O faturamento foi de {faturamento}, o custo foi de {custo} e o lucro foi de {lucro}')

print('@' in 'geovana@gmail.com')
print('@' in 'geovanagmail.com')

texto1 = 'Programação'
print(texto1.casefold())
print(texto1.lower())

#endswith - usado para verificar se o texto termina com um valor específico e dar a resposta True or False
print(texto.endswith('linda'))

frase = '''Progamação em Python
Aprendendo a trabalhar com Strings
Python Impressionador
'''
print(frase.splitlines())