def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero **potencia
    return calculo
"""Se asignan los valores para el calculo"""
resultado= elevarNumeroAlaPotencia2(numero=2,potencia=3)

etiqueta="Elevara {0} a la potencia {1} da como resultado {2}"
"""Se colocan bien los parametros para que la impresion salga correctamente"""
print(etiqueta.format(2,3,resultado))