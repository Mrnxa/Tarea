#12 Escribe un programa en Python para encontrar la longitud de un diccionario de valores.

diccionario=dict(a=1,b=50,c=80,d=200,g=0,e=5,f=60,t=100,z=10)

def longitudDiccionario(diccionario):
    return len(diccionario)

longitud=longitudDiccionario(diccionario)

print(longitud)