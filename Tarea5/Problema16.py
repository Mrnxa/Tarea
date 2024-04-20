#16 Escribe un programa en Python para filtrar números pares de un diccionario de valores. 
# Diccionario original: {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]} 
# Filtra números pares de los valores del diccionario mencionado: 
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]} 
# Diccionario original: {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]} 
# Filtra números pares de los valores del diccionario mencionado: 
# {'V': [], 'VI': [], 'VII': [2]}

diccionarioOriginal1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]} 
diccionarioOriginal2={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]} 
#P para PAR - I para impar
def filtroParImpar(diccionario,mode):

    diccionarioFiltrado={}
    for key,listas in diccionario.items():
        pares=[]
        impares=[]
        
        for numero in listas:
            if numero%2==0:
                pares.append(numero)
            else:
                impares.append(numero)
        match mode:
            case 'P':
                diccionarioFiltrado[key]=pares
            case 'I':
                diccionarioFiltrado[key]=impares
    return diccionarioFiltrado
                
                
print(filtroParImpar(diccionarioOriginal1,'P'))
print(filtroParImpar(diccionarioOriginal1,'I'))
print(filtroParImpar(diccionarioOriginal2,'P'))
print(filtroParImpar(diccionarioOriginal2,'I'))




                    
    