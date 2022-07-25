conjunto = set()
print(conjunto)

#agregar elementos al conjunto
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add('Hola')
conjunto.add('Agostina')
print(conjunto)

#borrar elementos al conjunto
conjunto.discard('Agostina')
conjunto.discard(2)
print(conjunto)

conjunto.add(9)
conjunto.add(9)
conjunto.add(9)
conjunto.add(9)
print(conjunto)

lista = [1,2,2,2,3,1,2,3,1,2,3,2,2,2,1,2,3,2,1,3]
conjunto = set(lista)
print(conjunto)
