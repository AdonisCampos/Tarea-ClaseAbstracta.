from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractmethod
    def saludar(self):
        pass
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y soy estudiante de {self.grado}"
        
class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        
    def saludar(self):
        return f"Hola, soy el profesor {self.nombre} y mi especialidad es {self.especialidad}"
        
class Padre(Persona):
    def __init__(self, nombre, edad, hijos):
        super().__init__(nombre, edad)
        self.hijos = hijos
        
    def saludar(self):
        return f"Hola, soy el padre {self.nombre} y tengo {len(self.hijos)} hijos"
        

bernardo = Estudiante("Bernardo", 24, "Licenciatura en Ciencias de la Computacion")
adonis = Profesor("Adonis", 22, "Historia")
bernardoCampos = Padre("Bernardo Campos", 35, ("Janel", "Arturo","Mayra"))
print(bernardo.saludar())
print(adonis.saludar())
print(bernardoCampos.saludar())

