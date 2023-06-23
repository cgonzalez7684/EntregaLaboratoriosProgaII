#Elevar numeros a pontencia 2

#Proceso matematico para elevar cualquier numero a cualquier potencia
def elevarNumeroAlaPontencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo

resultado = elevarNumeroAlaPontencia2 (numero = 2, potencia = 3)

etiqueta = "Elevar {0} a la potencia {1} da como resultado {2}"
print (etiqueta.format(2,3,resultado))