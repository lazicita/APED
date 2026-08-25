from bs4 import BeautifulSoup


def pagina():
    return """
        <html>
            <body>
                <div>
                    <h1 id="titulo"> Libros Disponibles </h1>
                    <div class="libro" data-isbn="900">
                        <h2> Python Basico </h2>
                        <span class="precio"> $1200 </span>
                    </div>
                    
                    <div class="libro" data-isbn="901">
                        <h2> Base de Datos </h2>
                        <span class="precio"> $900 </span>
                    </div>
                    
                    <div class="libro" data-isbn="902">
                        <h2> Innovacion Tec. </h2>
                        <span class="precio"> $800 </span>
                    </div>
                </div>
            </body>
        </html>
    
    """


def extraer(html:str):
    soup=BeautifulSoup(html,"html.parser")
    titulo=soup.find("h1", id="titulo")
    print(titulo.text)

    lista_li=soup.find_all("div", class_="libro")
    print(len(lista_li))
    data=[]
    for libro in lista_li:
        titulo_li=libro.h2
        precio_li=libro.find("span", class_="precio")
        isbn_li=libro["data-isbn"]
        data.append({
            "titulo":titulo_li.text,
            "precio":precio_li.text,
            "isbn":isbn_li
        })
    return data



if __name__ == "__main__":
    html=pagina()
    data=extraer(html)
    print(data)
