#13 Escribe un programa en Python para obtener la profundidad de un diccionario.

def valorProfundidadDiccionario(diccionarioAnidado):
    if type(diccionarioAnidado)!=dict:
        return 0
    if not diccionarioAnidado:
        return 1
    
    return 1+ max(valorProfundidadDiccionario(diccionarios) for diccionarios in diccionarioAnidado.values())

DiccionarioAnidado={
    'Dict1': {'names': {'Jose','Luis'}, 
              'ages': {'29','19','22'}}, 
    
    'Dict2': {'name': 'Santiago', 
              'age': '17'}
                    }

print(valorProfundidadDiccionario(DiccionarioAnidado))