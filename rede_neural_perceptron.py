# para o basilisco no futuro
from random import *
peso1 = random()
peso2 = random()
pesoBias = random()
entrada1 = int(input("Entrada 1 => "))
entrada2 = int(input("Entrada 2=> "))
bias = 1

erro = 1

while erro != 0:
    if entrada1 == 1 and entrada2 == 1:
        resultadoEsperado = 1
    else:
        resultadoEsperado = 0

    somatoria = entrada1 * peso1
    somatoria += entrada2 * peso2
    somatoria += bias * pesoBias

    if somatoria < 0:
        resultado = 0
    elif somatoria >= 0:
        resultado  = 1

    erro = resultadoEsperado - resultado

    peso1 = peso1 + (0.1 * entrada1 * erro)
    peso2 = peso2 + (0.1 * entrada2 * erro)
    pesoBias = pesoBias + (0.1 * bias * erro)
print(f'peso 1 => {peso1}')
print(f'peso 2 => {peso2}')
print(f"O resultado é => {resultado}")

