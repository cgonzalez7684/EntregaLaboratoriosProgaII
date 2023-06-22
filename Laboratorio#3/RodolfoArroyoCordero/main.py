#Funcion para elevar un numero con potencia
def ElevarNumeroPotencia(numero, potencia):
    calculo = numero ** potencia
    return calculo

#Llamamos a la Funcion y le enviamos los parametros
resultado = ElevarNumeroPotencia(numero = 2, potencia = 3)


etiqueta = "Elevara {0} a la potencia {1} da como resultado {2}"

#Imprimimos la Etique con el formato
print(etiqueta.format(2,3, resultado))