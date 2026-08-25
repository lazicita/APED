def funciones():
    l=[]
    l.append(1)
    l.append(4)
    l.append(10)
    l.append(20)
    l.append(30)
    l.insert(0,2)
    eliminado=l.pop(2)
    print(eliminado)
    l.remove(4)



def recorrer():
    l=[2,4,6,7,0,10]
    l2=[3,4,5,6,7,0,10]
    for i in l:
        print(i)

    for index in range(len(l)):
        print(l[index])

    for index, item in enumerate(l):
        print(index,"---" ,item)

    for item_1, item_2 in zip(l,l2):
        print(item_1, item_2)

def slicing():
    l=[2,4,6,7,0,10]
    print(l[-1])
    print(l[2:5])



def declarar():
    lista=[]
    l2=[2,4,2.4,"asd", True]
    l3=[lista,l2]
    l4=list()
    l5=list("azul")


if __name__ == '__main__':
    declarar()
    slicing()
    recorrer()
    funciones()