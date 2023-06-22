#El proposito que da el calculo  de 2 sea elevado a la 3
def elevarNumeroAlaPotencia2(numero,potencia):
    calculo = numero ** potencia
    return calculo

#Se les asignara a los valores de la variable y a los parametros para la ejecuccion del calculo
resultado = elevarNumeroAlaPotencia2(numero= 2, potencia=3)


#etiquetar con  los valores que se van a imprimir
etiqueta = "Elevara  {0}   a la potencia {1}  que da como resultado {2}"


#elaborar  con la impresion de la etiqueta se crearon con los valores que creamos
# Se les cambia de la potencia de que es 3 y no de 2
print(etiqueta.format(2,3,resultado))
