#6 Escribe un programa en Python para obtener un diccionario a partir de los campos de un objeto.

class Computadora:
    def __init__(self):
        self.marca='Apple'
        self.ram='16gb'
        self.procesador='Intel Core i7 de 4 núcleos y 1.2 GHz (Turbo Boost de hasta 3.8 GHz)'
        self.grafica='AMD Radeon™ Pro serie 5000'
        
computadora=Computadora()

#Usando vars
diccionarioCampos=vars(computadora)
print(diccionarioCampos)

#sin usar vars

def diccionarioOfCampos(objeto):
    return {
        'marca':objeto.marca,
        'ram':objeto.ram,
        'procesador':objeto.procesador,
        'gráfica':objeto.grafica
        
    }

print(diccionarioOfCampos(computadora))
        