lista = [1,2,'Agostina','MERCADO',5,'Peliculas']
print(lista)

lista.pop()
print(lista)

lista.reverse()
print(lista)

lista = [5,6,3,1,2,4]
lista.sort()
print(lista)

lista = [5,6,0,['rojo','negro']]
print(lista)
elemento = lista[3][0]
print(elemento)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
lista_nueva = [elemento[0] for elemento in matriz]
print(lista_nueva)
