def Elevar_Numero_A_la_Potencia_2(numero, potencia):
    #Siguiendo la nomenclatura estandarizada, si el nombre de una funcion consta de mas de una palabra, estas se tienen que separar con guion bajo (_).
    calculo = numero ** potencia
    return calculo


resultado = Elevar_Numero_A_la_Potencia_2(numero = 2, potencia = 3)

etiqueta = "Elevar {0} a la potencia {1} da como resultado {2}"

#El codigo en la linea 12 es incorrecto ya que al ejecutarse la linea de lectura diria Elevar 2 a la potencia 2 da como resultado 8, lo cual es incorrecto.
#print(etiqueta.format(2,2,resultado))
#Se realiza la sustitucion del segundo 2 por un 3 para que la leyenda ya sea correcta.
print(etiqueta.format(2,3,resultado))