def evaluarNumeroAlaPotencia2(numero,potencia):
    #logica o funcion para ejecutar operacion de potencias
    calculo = 1
    for n in range(potencia):
      calculo *= numero
    return calculo

#se asigana el resultado a la variable
resultado = evaluarNumeroAlaPotencia2(2,3)

#creamos una etiqueta para la impresion
etiqueta = "elevar {0} a la potncia {1} da como resultado {2}"
imprimirEtiqueta = etiqueta.format(2,3,resultado)

#impresión de la etiqueta correctamente
print(imprimirEtiqueta)