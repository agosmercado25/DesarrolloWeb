# Tratamiento de errores
def errores():
    fichero = open('datos.txt','w')
    fichero.write("Estos son los datos para el fichero")
    fichero.close()

    try:
        fichero = open('datos2.txt','r')
        fichero.write("Estos son los datos para el fichero")
        fichero.close()
    except:
        print("Error. El fichero no existe")
    else:
        print("Tratamiento de fichero correcto")
    finally:
        print("Tratamiento de fichero finalizado")

    print("Continua el programa")

#errores()
# Expresiones regulares
import re
def expresiones():
    texto = "Este coche verde es muy rapido"
    print(texto)
    patron = 'verde'
    encontrado = re.search(patron,texto)
    if encontrado:
        print("Patrón {} ha sido encontrado en el texto".format(patron))
        ini = encontrado.start()
        fin = encontrado.end()
        print("Patrón {} empieza en la posición {} y termina en {}".format(patron,ini,fin))
    else:
        print("Patrón {} no encontrado".format(patron))

    print("-----------------------------------------------------------------------------------------------------")
    texto = "Me gusta el color verde y por eso he comprado pintura verde."
    patron = "verde"
    resultado = re.findall(patron,texto)
    print(resultado)
    veces = len(resultado)
    print(veces)

    print("-----------------------------------------------------------------------------------------------------")
    texto = "Me gusta el color verde y por eso he comprado pintura verde."
    print(texto)
    patrones = ['gusta',"pintura",'noto']
    for patron in patrones:
        print("Estamos buscando por el patrón {}".format(patron))
        resultado = re.findall(patron,texto)
        veces = len(resultado)
        print(veces)
#expresiones()

# Modulos
#import modulo as mod
def modulos():
    mod.funcion1()
    mod.funcion2()

#modulos()

#variables locales y globales
"""
numero = 30
texto = "Hola"
def variables():
    numero2 = 50
    saludo = "Buenos días"
    print(numero2)
    print(saludo)
    print(locals())

#variables()
print(numero)
print(texto)
print(globals())
print(globals()['__file__'])
"""

#Funciones decoradoras

def asteriscos(funcion):
    def poner_asteriscos():
        print("*******************")
        funcion()
        print("*******************")

    return poner_asteriscos

def imprimir():
    print("Hola, buenos días")
"""
imprimir = asteriscos(imprimir)
imprimir()
"""

# Programa principal
# Para que se ejecute el else, esta en el archivo modulo.py

print("Estamos en parte3.py")

def principal():
    print("Funcion1 del fichero parte3.py")

if __name__ == '__main__':
    print("Estamos ejecutando este código desde el fichero parte3.py")
else:
    print("Estamos ejecutando este código desde otro fichero")
