def elevarNumroAlaPotencia2(numero, potencia):
    calculo = numero** potencia
    return calculo


resultado = elevarNumroAlaPotencia2(numero = 2, potencia = 3)

etiqueta = "Elevar {0} a la potencia {1} da como resultado {2}"


"""el metodo formart permite darle formato al texto que tiene guardado la vaiable etiqueta
permitiendo ubicar los valores que se quieren pocisionar
este format es incorrecto los valores que se le pasan estan mal ya que 2 potencia 2 es 4
print(etiqueta.format(2,2,resultado))""" 


# lo correcto es usar este metodo format dandole los valores correctos con su pocisionamiento
print(etiqueta.format(2,3,resultado))    