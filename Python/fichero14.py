def hola():
    print("Hola, buenos días")

hola()
hola()
hola()

def sumar(num1,num2):
    """
    Esta funcion suma dos numeros enteros
    Ejemplo de la llamada
        sumar(5,3)
    """
    if type(num1) == type(num2) == type(10):
        resultado = num1 + num2
    else:
        resultado = "Error. Deben ser numeros"
    return resultado

suma = sumar(5,'3')
print(suma)
