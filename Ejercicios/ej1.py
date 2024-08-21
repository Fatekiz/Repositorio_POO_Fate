
# Tomando el código que hemos estado trabajando en la última clase, se solicita agregar nuevas
# Propiedades a la clase Persona:
class Persona():

    # Constructor de clase
    def __init__(self, nombre, apellido, edad,altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)

    #Métodos (Comportamientos) (Deben estar dentro de la clase, ya que son 'comportamientos' de la clase creada)
    def hablar(self):
        print(f"{self.nombre} está hablando") 

    def caminar(self):
        print(f"{self.nombre} está caminando")

    def calcular_imc(self): 
        imc = (self.peso / (self.altura**2))

        if imc < 18.5:
            print(f" El imc de {self.nombre} es de {imc}. Según su imc se encuentra con un peso insuficiente.")
        elif imc >= 18.5 and imc < 25:
            print(f" El imc de {self.nombre} es de {imc}. Según su imc se encuentra con un peso ideal y dentro del rango saludable.")    
        else:
            print(f" El imc de {self.nombre} es: {imc}. Según su imc se encuentra sobre peso, lo cuál es peligroso para su salud.")
        return imc
    
    def promedio_asignatura(self):
        print(f"Ingrese las 3 notas de {self.nombre} para calcular su promedio y su estado de asignatura. \n")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 4.0:
            estado_asignatura = "Ha aprobado la asignatura"
        elif promedio < 4.0:
            estado_asignatura = "ha reprobado la asignatura"
        print(f" el promedio final de {self.nombre} es de: {promedio}, Por ende, {estado_asignatura}.")
        return promedio





    
# Creacion de un objeto de la clase  Persona / Instanciando clase

persona1 = Persona("Rocio", "Cardenas", 27, 1.53, 63)
persona2 = Persona("Benjamin", "Concha", 19, 1.71, 60)

# imprimiendo el calculo del imc en ambos casos

persona2.calcular_imc()
persona1.calcular_imc()

# Imprimiendo el promedio en ambos casos
persona1.promedio_asignatura()
persona2.promedio_asignatura()