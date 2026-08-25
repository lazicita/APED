def declarar():
    t=(1,3,5,7)
    lista=[1,2,3,4,5]
    t2=tuple(lista)





def slicing():
    t = (1, 3, 5, 7,10,15)
    print(t[1])
    print(t[1:5:2])


def recorrer():
    t = (1, 3, 5, 7)
    t2=(10,30,50,70)
    for i in t:
        print(i)

    for index in range(len(t)):
        print(t[index])

    for index, item in enumerate(t):
        print(index,"---" ,item)

    for item_1, item_2 in zip(t,t2):
        print(item_1, item_2)


def funciones():
    t = (1, 3, 5, 7, 10, 15,15)
    conteo=t.count(15)
    print("15 aparece;",conteo,"veces")
    indice=t.index(15)
    print("15 aparece en el indice:",indice)

if __name__ == '__main__':
    declarar()
    slicing()
    recorrer()
    funciones()