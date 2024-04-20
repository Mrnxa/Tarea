#4 Escribe un programa en Python para ordenar un diccionario dado por clave.
#Suponiendo que pide orden de a-z en str exceptuando la ñ

diccionario={
    'Alan':11,
    'Roberto':10,
    'Ana':5,
    'Victoria':7,
    'Carlos':10,
    'Alberto':4,
    'Yesenia':6,
    'Cristian':3,
    'Jesus':11,
    'Edith':8
    
            }

diccionarioOrdenadoAlfabetico=dict(sorted(diccionario.items()))
diccionarioOrdenadoNumerico=dict(sorted(diccionario.items(),key=lambda x:x[1], reverse=True))

print(diccionarioOrdenadoAlfabetico)
print(diccionarioOrdenadoNumerico)