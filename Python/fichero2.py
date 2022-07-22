texto = "Hola, buenos días"
print(texto)

caracter = texto[0]
caracterF = texto[-1]
caracterL = texto[0:4]
caracterFinal = texto[6:]
#Muestra del 6 al final de 2 en 2
caracterFinal2 = texto[6::2]
print(caracter)
print(caracterF)
print(caracterL)
print(caracterFinal)
print(caracterFinal2)

mayusculas = texto.upper()
print(mayusculas)

minusculas = mayusculas.lower()
print(minusculas)

colores = "rojo,verde,azul,negro"
lista = colores.split(",")
print(lista)
