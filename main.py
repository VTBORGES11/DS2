from LadoParaCirculo import LadoParaRaio, calcular_area
from quadrado import Quadrado


quadrado = Quadrado(10)
circulo = LadoParaRaio(quadrado)

print(calcular_area(quadrado))
print(calcular_area(circulo))