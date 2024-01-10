#Imports
import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1

# Abrir o navegador #
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")


# Estou utilizando o PC do LADES com tela EliteDisplay e tem 6 contas logadas.
# Para resolver esse problema, foi feita essa adaptação no código.

# Maximizando a Tela
pyautogui.click(x=1400, y=137)
time.sleep(0.2)

for i in range(1, 8):
    pyautogui.press("tab")
    
#time.sleep(0.1)

pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Acessar o site do sistema com login e senha #

time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("teste@teste.de.jean")
pyautogui.press("tab")
pyautogui.write("Teste@2024")
pyautogui.press("tab")
pyautogui.press("enter")
#pyautogui.press("tab") # Aqui vamos para o primeiro campo

# Inserir todas as informações do produto #

tabela = pd.read_csv("produtos.csv") 

for line in tabela.index:
    pyautogui.click(x=678, y=291) # Aqui vamos para o primeiro campo
    pyautogui.write(str(tabela.loc[line, "codigo"])) # Escrever o código da tabela
    pyautogui.press("tab") # Para o próximo campo
    
    # Vamos repetir isso para os próximos campos
    
    pyautogui.write(str(tabela.loc[line, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[line, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[line, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[line, "custo"]))
    pyautogui.press("tab")
    
    if not pd.isna(tabela.loc[line, "obs"]):
        pyautogui.write(str(tabela.loc[line, "obs"]))

    # Enviar as informações para o sistema #

    pyautogui.press("tab")
    pyautogui.press("enter")
    
    time.sleep(0.5)

    # pyautogui.doubleClick(x=868, y=775)
    #pyautogui.press("enter")
    # pyautogui.scroll(-200)
    
 # Repetir o cadastro até acabar o cadastro de todos os produtos #

#Pyautogui.press – Serve para pressionar uma tecla do seu teclado
#Pyautogui.write – Serve para escrever com o teclado (como se fosse você digitando)
#Pyautogui.click – Serve para clicar com o mouse