#Captura de datos para conocer el tamaño del cuadro
lado = int(input("Ingrese el tamaño del lado del cuadrado: "))

#For para didujar el cuadro ingresado por el usuario
#For para hacer la impresion de las filas del cuadro
for x in range(1, lado):
    #For para hacer la impresion de las columnas del cuadro
    for y in range (1):
       #Impresion de la cantidad de astericos del cuadro
       print("*" * (lado*2))
       
#Impresion para avisar del fin del dibujo 
print("\rFin del dibujo")     