#Funcion para el calculo de la potencia 
def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo

#Asignacion de los valores a la función
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)

etiqueta = "Elevar {0} a la potencia {1} da como resultado {3}"

"""Impresion del resultado con el cambio corregido
Anteriormente era "2,2" que daba error"""

print (etiqueta.format(2,3,resultado))