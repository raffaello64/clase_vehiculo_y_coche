class Vehiculo:
    def __init__(self, color, ruedas, puertas):

        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

coche = Vehiculo("rojo", 4, 4)

print('El vehículo es un coche y es de color ', coche.color, ', tiene ', coche.ruedas, 'ruedas y ', coche.puertas, 'puertas')

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return 'El vehículo es un coche y es de color ' + self.color + ', tiene ' + str(self.ruedas) + ' ruedas y ' + str(self.puertas) + ' puertas, tiene una velocidad de ' + str(self.velocidad) + ' km/h y una cilindrada de ' + str(self.cilindrada) + ' cc'
        
C = Coche("rojo", 4, 4, 200, 1200)

print(C)

        

