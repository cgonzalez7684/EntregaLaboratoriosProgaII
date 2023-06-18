def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo

#Por defecto numero y potencia van a tener valores de 2 y 3 respectivamente
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)

etiqueta = "Elevara {0} a la potencia {1} da como resultado {2}"

#Cambiamos los argumentos del metodo format de (2, 2) a (2,2)
#Con los nuevos argumentos se imprimen los valores correctos
print(etiqueta.format(2,3, resultado))