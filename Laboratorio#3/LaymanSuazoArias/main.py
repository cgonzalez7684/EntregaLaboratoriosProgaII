# Funcion para calcular potencia
def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo

# llamado de la funcion
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)
# Impresion usando el metodo format
etiqueta = "Elevar {0} a la potencia {1} da como resultado {2}"
# Pasando variable para impresion
print(etiqueta.format(2,3,resultado))
