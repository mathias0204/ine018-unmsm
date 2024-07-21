class León:
    def inicializar_leon(self, nombre, color_melena):
        self.nombre = nombre
        self.color_melena = color_melena

    def rugir(self):
        print("¡Rugido de león!")

mi_leon = León()
mi_leon.inicializar_leon("Mathias", "marrón")
mi_leon.rugir()