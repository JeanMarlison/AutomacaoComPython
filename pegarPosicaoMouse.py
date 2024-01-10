#Imports
import pyautogui
import time

# Para esperar para poder seguir o resto do código
time.sleep(5) 

# Par pegar a Posição do Mouse, para saver onde clicar
print(pyautogui.position())

# Vericar o quantos de Scroll
pyautogui.scroll(-200)