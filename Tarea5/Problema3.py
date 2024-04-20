#3 Escribe un programa en Python para convertir dos listas en un diccionario.
lista1=['a','b','c','d']
lista2=[1,2,3,4]

def dictForLists(keys,values):
    diccionario={}

    if len(keys)!=len(values):
        print('Las listas deben de tener la misma longitud')
        
        return
    
    for i in range(len(keys)):
            diccionario[keys[i]]=values[i]
       
    return diccionario

diccionario2Listas=dictForLists(lista1,lista2)

print(diccionario2Listas)