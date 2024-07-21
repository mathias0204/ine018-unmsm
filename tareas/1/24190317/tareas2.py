class Persona:
    def Mathias(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def obtener_nombre(self):
        return self.nombre
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

mi_persona = Persona()
mi_persona.Mathias("Manuel", 20)
nombre_actual = mi_persona.obtener_nombre()
print(f"Hola, soy {nombre_actual}, ¿cómo estás?")
mi_persona.cambiar_nombre("Loaiza")
nombre_actualizado = mi_persona.obtener_nombre()
print(f"Ahora me llamo {nombre_actualizado}, ¡un gusto conocerte!")