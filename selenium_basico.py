import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def navegador():
    #user-name
    #password
    #login-button

    user="standard_user"
    password="secret_sauce"

    s=Service(ChromeDriverManager().install())#Configura el driver q se usará
    ops=Options()
    ops.add_argument('--window-size=1920x1080')#tamaño de navegador
    navegador= webdriver.Chrome(service=s,options=ops)
    navegador.get('https://www.saucedemo.com')
    time.sleep(2)#no pasa la siguiente linea de codigo por 2s
    txtuser=navegador.find_element(By.ID,"user-name")
    txtpassword=navegador.find_element(By.ID,"password")
    btnlogin=navegador.find_element(By.ID,"login-button")

    txtuser.send_keys(user)
    time.sleep(2)
    txtpassword.send_keys(password)
    time.sleep(2)
    btnlogin.click()
    time.sleep(2)
    navegador.save_screenshot('test.png')
    navegador.close()#cierra la pagina



if __name__=='__main__':
    navegador()