def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo

# Asigna los valores y llamar la función
numero = 2
potencia = 3
resultado = elevarNumeroAlaPotencia2(numero, potencia)

# Crea la etiqueta y muestra el resultado
etiqueta = f"Elevar a {numero} a la potencia {potencia} da como resultado {resultado}"
print(etiqueta)