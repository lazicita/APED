from datetime import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())#Configura el driver q se usará
ops=Options()
ops.add_argument('--window-size=1200,800')#tamaño de ordenador
navegador=webdriver.Chrome(service=s,options=ops)
navegador.get('https://www.google.com')
time.sleep(5)#no pasa la siguiente linea de codigo por 5s
navegador.close()#cierra la pagina
