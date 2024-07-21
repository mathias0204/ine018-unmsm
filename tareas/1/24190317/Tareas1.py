class BestiaJurásica:
    def sonido(self):
        pass

class TyrannosaurusRex(BestiaJurásica):
    def sonido(self):
        print("¡Escucha el rugido del T. rex!")

def hacer_sonar_bestia(bestia):
    bestia.sonido()

trex = TyrannosaurusRex()
hacer_sonar_bestia(trex)