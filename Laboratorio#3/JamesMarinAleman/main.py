#funcion para elevar un numero
def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo
#se asignan los valores
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)
#Se crea un etiq para saber que se va a inimprimir
etiqueta = "Elavara {0} a la potencia {1} da como resultado {2}"

#le asignamos a la etiqueta los valores
print(etiqueta.format(2,3,resultado))

