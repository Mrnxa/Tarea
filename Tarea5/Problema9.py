# 9 Escribe un programa en Python para extraer una lista de valores de una lista dada de diccionarios. 
# Diccionario original: [{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}] 
# 10 
# Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Ciencias [92, 94, 88] 
# Diccionario original: [{'matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}] 
# 11 
# Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Matemáticas [90, 89, 92]

listDict1=[{'Matematicas': 80, 'ciencia': 82}, {'matematicas': 90, 'ciencia': 95}, {'Matematicas': 92, 'ciencia': 88}]

def fusionarDiccionarios(listaDiccionarios,asignatura):
    values=[]
    for diccionario in listaDiccionarios:
        for key,value in diccionario.items():
            if key.lower()==asignatura.lower():
                values.append(value)
                
    return values

cienciasVaues=fusionarDiccionarios(listDict1,'ciencia')
matematicasValues=fusionarDiccionarios(listDict1,'matematicas')

print(f'Ciencia {cienciasVaues}')
print(f'Matematicas {matematicasValues}')
