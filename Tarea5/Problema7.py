#7 Escribe un programa en Python para eliminar duplicados del diccionario.


diccionario=dict(a=1,b=10,c=10,d=60,g=0,e=5,f=60,t=80,z=30)

def eliminarduplicados(diccionario):
    diccionarioNoDup={}
    for key,value in diccionario.items():
        if value not in diccionarioNoDup.values():
            diccionarioNoDup[key]=value
    
    return diccionarioNoDup

diccionarioNoDup=eliminarduplicados(diccionario)

print(diccionarioNoDup)