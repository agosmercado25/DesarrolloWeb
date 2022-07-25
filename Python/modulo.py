def funcion1():
    print("Esta es la funcion1 del modulo modulo.py")

def funcion2():
    print("Esta es la funcion2")

# Programa principal
import parte3

print("Estamos en modulo.py")

if __name__ == '__main__':
    print("Estamos ejecutando este código desde el fichero modulo.py")
else:
    print("Estamos ejecutando este código desde otro fichero")

parte3.principal()
