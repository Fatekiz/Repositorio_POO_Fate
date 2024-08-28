""" Crea la clase Coche que contenga las siguientes propiedades: 
marca (string): La marca del coche.
gasolina (float): La cantidad de gasolina disponible en el coche """

# Creando constructor de clase

class Coche():

    def __init__(self, marca, gasolina, kilometros_recorridos):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = kilometros_recorridos


    def conducir(self, kilometros):
        self.kilometros = kilometros
        
        print(f"El vehiculo de marca {self.marca} tiene {self.gasolina} Litros de gasolina, y irá a recorrer {self.kilometros} kilómetros.")



auto1 = Coche("Peugeot", 9, 0)

auto1.conducir(10)