from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui



janela = webdriver.Chrome()
janela.get('https://web.whatsapp.com/')


# Aguarda o elemento de Qrcode carregar
while True:
    while len(janela.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div/div[2]/div/canvas')) < 1:
        pass
# Aguarda as mensagens serem carregadas
    while len(janela.find_elements(By.ID, 'side')) < 1:
        pass

    pyautogui.sleep(30)
   
    janela.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('Anotações')
    pyautogui.sleep(5)
    pyautogui.press('enter')
    pyautogui.sleep(5)
    while True:
         janela.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('TESTE')
         pyautogui.press('enter')