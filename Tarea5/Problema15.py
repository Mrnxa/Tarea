#15 Escribe un programa en Python para convertir un diccionario en una lista de listas. 
# Diccionario original: {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'} 
# Convierte el mencionado diccionario en una lista de listas: 
# [[1, 'rojo'], [2, 'verde'], [3, 'negro'], [4, 'blanco'], [5, 'negro']]

diccionarioOrig={1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}
lista=[]


for key,value in diccionarioOrig.items():
    listaMenor=[key,value]
    lista.append(listaMenor)
    
    
print(lista)
    