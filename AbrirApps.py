import pyautogui
import time
print ("Boas Vindas \n")
escolha = str(input("Digite o programa desejado (word, excel, google chrome): "))
escolha2 = str(input("Digite a Conta desejada (BurguerGuy, Escola, Terra): ")).lower()

if escolha2 == "burguerguy":
  pyautogui.press('win')
  pyautogui.write('chrome')
  pyautogui.press('enter')
  time.sleep(1)
  pyautogui.click(x=617, y=619)
if escolha2 == "escola":
 pyautogui.press('win')
 pyautogui.write('chrome')
 pyautogui.press('enter')
 time.sleep(1)
 pyautogui.click(x=827, y=606)
if escolha2 == "terra":
 pyautogui.press('win')
 pyautogui.write('chrome')
 pyautogui.press('enter')
 time.sleep(1)
 pyautogui.click(x=1104, y=606)
          
#pyautogui.press("win")
#time.sleep(2)
#pyautogui.write(escolha)
#pyautogui.press("enter")
#pyautogui.press("enter")
#time.sleep(2)
#pyautogui.press("tab")
#pyautogui.press("enter")