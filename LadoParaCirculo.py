import math
from quadrado import Quadrado

class LadoParaRaio:
    def __init__(self, quadrado):
        self.raio = quadrado.lado
    def area(self):
        return math.pi * (self.raio ** 2)
    
def calcular_area(forma):
    return forma.area()