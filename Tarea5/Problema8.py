#8 Escribe un programa en Python para verificar si un diccionario está vacío o no.

def estaVacioONo(diccionario):
    if diccionario:
        print('No está vacío')
    else:
        print('Está vacío')
        
dicVacio={}
dicVaciont={'a':1}

estaVacioONo(dicVacio)
estaVacioONo(dicVaciont)