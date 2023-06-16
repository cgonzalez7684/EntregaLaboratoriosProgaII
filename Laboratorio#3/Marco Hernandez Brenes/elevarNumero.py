def elevarNumeroAlaPotencia2(numero, potencia):
    calculo = numero ** potencia
    return calculo
#Aqui los valores de la funcion no coinciden con los de la cadena de texto llamada etiqueta 
#Se esta psando el numero 2 y la potencia 3 pero la etiqueta no tiene sentido por que estoy diciendo que elevo el numero 2 a la potencia 2
resultado = elevarNumeroAlaPotencia2(numero = 2, potencia = 3)

etiqueta = "Elevara {0} a la potencia {1} da como resultado {2}"
#Linea numero 10 es el codigo original, mal hecho, voy a ponerlo como comentario y poner el codigo correcto en linea 12
#print(etiqueta.format(2,2,resultado)) ---> Codigo malo
#Codigo corregido en linea 12, cambio el segundo 2 por un 3 para que corresponda con los argumentos que vienen desde la funcion
print(etiqueta.format(2, 3, resultado))
