#2 Escribe un programa en Python para eliminar una clave de un diccionario.

numeros=dict(a=2,b=5,c=7,d=8)
print(f'Diccionario inicial: {numeros}')
def eliminarClavesDict(diccionario):
    
    valorAEliminar=input('Ingrese la clave deseada a eliminar y pulse ENTER: ')
    if valorAEliminar in diccionario:
        del numeros[valorAEliminar]
    else:
        print('La clave deseada a eliminar no se encuentra en el diccionario')
    
eliminarClavesDict(numeros)
print(f'Diccionario final: {numeros}')