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
pyautogui.press("tab")
pyautogui.write('python123')
pyautogui.click(x=954, y=566)
time.sleep(3)
pyautogui.hotkey('alt', 'tab')

#Lendo um arquivo com o pandas
tabela = pd.read_csv(r'C:\Users\User\PycharmProjects\MiniCursoPython - Hashtang\automacao_tarefas\produtos.csv')
print(tabela)
