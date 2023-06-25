#creamos funcion para elevar x numero a y potencia
def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo

resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)

#Define una cadena de texto que contiene espacios reservados {0}, {1}, y {2} para ser reemplazados posteriormente por valores.
etiqueta = "Elevar a {0} a la potencia {1} da como resultado {2}"

#Imprime en la consola la cadena de texto etiqueta con los valores reemplazados: 2 en lugar de {0}, 3 en lugar de {1}, y resultado en lugar de {2}. Esto muestra un mensaje que indica el numero que se elevo a la potencia y el resultado obtenido.
print(etiqueta.format(2,3,resultado))