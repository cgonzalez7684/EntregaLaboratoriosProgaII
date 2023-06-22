#función que da el calculo de 2 elevado a la 3
def elevarNumeroAlaPotencia2 (numero, potencia):
    calculo= numero ** potencia
    return calculo

#Se asignan los valores a la variable y a los parametros para le calculo
resultado = elevarNumeroAlaPotencia2( numero = 2, potencia =  3)

#Etiqueta con los valores que se van a imprimir
etiqueta = "Elevar {0} a la potencia {1} da como resultado {2}"

#Imprime la etiqueta creada con los valores que deseamos imprimir
#Se cambia la potencia ya que es 3 y no 2
print(etiqueta.format(2,3,resultado))