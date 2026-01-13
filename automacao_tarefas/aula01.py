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

#Lendo um arquivo com o pandas
tabela = pd.read_csv(r'C:\Users\User\PycharmProjects\MiniCursoPython - Hashtang\automacao_tarefas\produtos.csv')
print(tabela)
for linha in tabela.index:
    #Cadastrar um produto
    pyautogui.click(x=743, y=285)
    #Codigo
    pyautogui.write('MOLO000251')
    pyautogui.press('tab')
    #Marca
    pyautogui.write('Logitech')
    pyautogui.press('tab')
    #Tipo
    pyautogui.write('Mouse')
    pyautogui.press('tab')
    #categoria
    pyautogui.write('1')
    pyautogui.press('tab')
    #Preço unitário
    pyautogui.write('25.95')
    pyautogui.press('tab')
    #Custo
    pyautogui.write('6.50')
    pyautogui.press('tab')
    #OBS
    pyautogui.write('obs')
    pyautogui.press('tab')

    pyautogui.press('enter')
