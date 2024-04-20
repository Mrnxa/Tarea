#5 Escribe un programa en Python para obtener los valores máximo y mínimo de un diccionario.



diccionario=dict(a=1,b=110,c=100,d=20,g=0,e=500,f=60)

def maxMinOfDictValues(diccionario):
    valores=diccionario.values()
    maximo=float('-inf')
    minimo=float('inf')
    for values in valores:
        if values>=maximo:
            maximo=values
        elif values<=minimo:
            minimo=values
    maxMin=(maximo,minimo)        
    return maxMin

maximoMinimo=maxMinOfDictValues(diccionario)

print(maximoMinimo)
