import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


data={"titulos":[],"puntos":[],"fecha": [],"comentarios": []}
def extraer(html,data):

    soup=BeautifulSoup(html,'html.parser')
    titulos=soup.find_all('span',class_="titleline") #encuentra segun la clase

    for titulo in titulos:
        data['titulos'].append(titulo.text)

    sublineas = soup.find_all('td', class_="subtext")


    for subline in sublineas:
        puntos=subline.find("span", class_="score")
        fecha=subline.find("span", class_="age")
        comentarios=subline.find_all("a")[-1]

        #VALIDACIONES
        if puntos:
            data['puntos'].append(puntos.text)
        else:
            data['puntos'].append("0 points")
        data['fecha'].append(fecha["title"].split(" ")[0])
        if "comments" in comentarios.text or "comment" in comentarios.text:
            data['comentarios'].append(comentarios.text)
        else:
            data['comentarios'].append("0 comments")

        #print([fecha["title"].split(" ")[0])






def navegar(paginas):
    url="https://news.ycombinator.com/"
    s = Service(ChromeDriverManager().install())  # Configura el driver q se usará
    ops = Options()
    ops.add_argument('--window-size=1020,800')  # tamaño de navegador
    navegador = webdriver.Chrome(service=s,options=ops)
    navegador.get(url)
    time.sleep(2)
    for pagina in range(paginas):
        time.sleep(1)
        extraer(navegador.page_source,data)
        next=navegador.find_element(By.CLASS_NAME,"morelink")
        #next=navegador.find_element(By.LINK.TEXT,"More")
        next.click()


    navegador.close()
    return data



if __name__=="__main__":
    paginas=3
    data=navegar(paginas)
    print("Cantidad Final:",len(data["titulos"]))
    print(data)
    df=pd.DataFrame(data)
    df.to_csv("datasets/data.csv",index=False)

