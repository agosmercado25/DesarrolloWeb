class Persona():
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self):
        self.texto = "Hola, mi nombre es " + self.nombre
        return self.texto

persona1 = Persona('Agostina')
print(type(persona1))
print(persona1.nombre)
print(persona1.saludar())

class Adulto(Persona):
    def __init__(self,nombre):
        Persona.__init__(self,nombre)
    def saludar(self):
        self.texto = "Hola, soy adulto"
        return self.texto
    def grabar_tarjeta(self,tarjeta):
        self.tarjeta = tarjeta
    def __str__(self):
        self.texto = "Adulto - Nombre: " + self.nombre
        return self.texto

adulto1 = Adulto("Agostina")
print(type(adulto1))
print(adulto1.saludar())
adulto1.grabar_tarjeta("312456789")
print(adulto1.tarjeta)
print(adulto1)
