lista = [1,2,3]
print(lista)

lista = ['Agostina','MERCADO',1,2,'Peliculas',3,25]
print(lista)

elemento = lista[1:3]
print(elemento)

nuevos_elementos = ['rojo','negro',6,3.5]
lista.append(nuevos_elementos)
print(lista)

elemento = lista[7]
print(elemento)

lista = ['Agostina','MERCADO',1,2,'Peliculas',3,25]
nuevos_elementos = ['rojo','negro',6,3.5]
lista.extend(nuevos_elementos)
print(lista)
