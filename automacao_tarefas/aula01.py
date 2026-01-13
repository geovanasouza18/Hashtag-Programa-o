import pyautogui
import time
import pandas as pd
#Clica -> pyautogui.click()
#escreve um texto → pyautogui.write
#aperta uma tecla → pyautogui.press
#aperta um atalho → pyautogui.hotkey('ctrl', 'c')
pyautogui.PAUSE = 0.5
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
#Fazer uma pausa maior para o site carregar
time.sleep(3)

#Fazendo login
pyautogui.click(x=700, y=408)
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')
pyautogui.write('python123')
pyautogui.click(x=954, y=566)
time.sleep(3)

#Lendo um arquivo com o pandas
tabela = pd.read_csv(r'C:\Users\User\PycharmProjects\MiniCursoPython - Hashtang\automacao_tarefas\produtos.csv')
print(tabela)
for linha in tabela.index:
    #Cadastrar um produto
    pyautogui.click(x=743, y=285)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, 'codigo']
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press('tab')
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)

